#!/usr/bin/env python3
"""Validate servers/*.json, render servers/*.md from them, and write the exports.

Usage:
  python build_export.py           validate, render markdown entries, write allowlist.json / allowlist.csv
  python build_export.py --check   validate only; write nothing

The JSON file of an entry is its source. The markdown file beside it is generated
from the JSON by this script and must not be edited by hand. Standard library only.
"""
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SERVERS = ROOT / "servers"

DATASET = "plainproof-mcp-server-review"
VERSION = "0.2.0"
# Placeholder until the repository exists; PUBLISH.md says where to change it.
REPO_URL = "https://github.com/plainproof/mcp-server-findings"
ISSUES_URL = REPO_URL + "/issues/new"

CRITERIA = {
    "C1": "Source and release provenance",
    "C2": "Published security policy",
    "C3": "Maintenance status",
    "C4": "Published advisories",
    "C5": "Documented scope controls",
    "C6": "Credential handling in the documented setup",
    "C7": "Telemetry and outbound data, as documented",
    "C8": "Dependency management files",
    "C9": "Documentation of untrusted-content risk",
    "C10": "Currency of the declared MCP library",
}
ORDER = list(CRITERIA)
RESULTS = ("meets", "partly meets", "does not meet")
GATING = ("C1", "C3", "C4")
OUTCOMES = ("criteria-met", "criteria-partly-met", "criteria-not-met")
STATUSES = ("active", "renamed", "transferred", "superseded-upstream",
            "unmaintained-per-publisher", "inactive", "archived-upstream", "withdrawn")
REQUIRED = [
    "slug", "name", "repository", "publisher", "publisher_account_type", "package",
    "upstream_status", "latest_release", "commit", "stars", "verified", "results",
    "outcome", "outcome_statement", "findings", "advisories", "third_party_reports",
    "not_reverified",
]
OUTCOME_RULE = (
    "criteria-not-met: 'does not meet' on C1, C3 or C4, or on three or more criteria. "
    "criteria-met: no 'does not meet', C4 'meets', at most four 'partly meets'. "
    "criteria-partly-met: every other combination. See METHODOLOGY.md section 5."
)
NOTICE = (
    "Point-in-time findings read from each project's own public material on the 'verified' date, "
    "measured against the criteria in METHODOLOGY.md. Not a scan, not a certification, not a "
    "guarantee, and not a statement about any project's maintainers. Findings can be disputed: "
    "see CONTESTING.md."
)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def outcome_of(results: dict) -> str:
    """METHODOLOGY.md section 5.2, applied mechanically."""
    no = [c for c in ORDER if results[c] == "does not meet"]
    partly = [c for c in ORDER if results[c] == "partly meets"]
    if any(c in no for c in GATING) or len(no) >= 3:
        return "criteria-not-met"
    if not no and results["C4"] == "meets" and len(partly) <= 4:
        return "criteria-met"
    return "criteria-partly-met"


def statement_of(results: dict, verified: str) -> str:
    """METHODOLOGY.md section 5.1."""
    parts = []
    for label in RESULTS:
        cs = [c for c in ORDER if results[c] == label]
        if cs:
            parts.append(f"{label} {', '.join(cs)}")
    return f"As of {verified}: " + "; ".join(parts) + "."


def load_records():
    records, problems = [], []
    for path in sorted(SERVERS.glob("*.json")):
        name = path.name
        try:
            rec = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            problems.append(f"{name}: invalid JSON ({e})")
            continue
        missing = [k for k in REQUIRED if k not in rec]
        if missing:
            problems.append(f"{name}: missing fields {missing}")
            continue
        if rec["slug"] != path.stem:
            problems.append(f"{name}: slug '{rec['slug']}' does not match file name")
        if not DATE_RE.match(str(rec["verified"])):
            problems.append(f"{name}: 'verified' is not a date")
        if rec["upstream_status"] not in STATUSES:
            problems.append(f"{name}: unknown upstream_status '{rec['upstream_status']}'")
        results = rec["results"]
        if list(results) != ORDER or any(v not in RESULTS for v in results.values()):
            problems.append(f"{name}: results must be C1..C10 with values {RESULTS}")
            continue
        if rec["outcome"] != outcome_of(results):
            problems.append(f"{name}: outcome '{rec['outcome']}' != rule result '{outcome_of(results)}'")
        if rec["outcome_statement"] != statement_of(results, rec["verified"]):
            problems.append(f"{name}: outcome_statement does not match results")
        fs = rec["findings"]
        if [f.get("criterion") for f in fs] != ORDER:
            problems.append(f"{name}: findings must cover C1..C10 in order")
            continue
        for f in fs:
            c = f["criterion"]
            if f.get("result") != results[c]:
                problems.append(f"{name}: {c} finding result differs from results")
            if not f.get("finding"):
                problems.append(f"{name}: {c} has no finding text")
            srcs = f.get("sources") or []
            if not srcs or any(not str(s).startswith("https://") for s in srcs):
                problems.append(f"{name}: {c} needs at least one https source")
            marker = str(f.get("verified", ""))
            if not (DATE_RE.match(marker) or marker.startswith("not re-verified ")):
                problems.append(f"{name}: {c} needs a verified date or a 'not re-verified <date>' marker")
            if marker.startswith("not re-verified") and c not in " ".join(rec["not_reverified"]):
                problems.append(f"{name}: {c} is not re-verified but not listed in not_reverified")
        for a in rec["advisories"]:
            if not all(k in a for k in ("id", "severity", "published", "affected", "patched", "url")):
                problems.append(f"{name}: advisory record incomplete")
        for t in rec["third_party_reports"]:
            if not all(k in t for k in ("reported_by", "title", "url", "status", "verified")):
                problems.append(f"{name}: third-party report record incomplete")
        records.append(rec)
    return records, problems


def render_markdown(r: dict) -> str:
    acct = {"Organization": "GitHub organisation account", "User": "GitHub user account"}.get(
        r["publisher_account_type"], r["publisher_account_type"])
    rel = r["latest_release"]
    repo = f"<{r['repository']}>"
    if r.get("path_in_repository"):
        repo += f" (`{r['path_in_repository']}`)"
    if r.get("repository_at_selection"):
        repo += f"; listed at selection as <{r['repository_at_selection']}>"
    status = f"`{r['upstream_status']}`"
    if r.get("upstream_status_note"):
        status += f" - {r['upstream_status_note']}"
    lines = [
        f"# {r['name']}",
        "",
        f"> Findings as of {r['verified']}, read from the project's own public material and measured "
        "against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, "
        "not a scan, a certification or a guarantee, and it says nothing about the people who maintain "
        "the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| Slug | `{r['slug']}` |",
        f"| Repository | {repo} |",
        f"| Package | `{r['package']}` |",
        f"| Publisher | {r['publisher']} ({acct}) |",
        f"| Licence detected by GitHub | {r.get('license_spdx') or 'none detected'} |",
        f"| Upstream status | {status} |",
        f"| Latest release | {rel['version']} ({rel['date']}) |",
        f"| Commit read | `{r['commit'][:12]}` on `{r.get('default_branch', '')}` ({r.get('commit_date', '')}) |",
        f"| GitHub stars | {r['stars']} |",
        f"| Verified | {r['verified']} |",
        f"| Outcome group | `{r['outcome']}` |",
        "",
        "## Outcome",
        "",
        r["outcome_statement"],
        "",
        "The group above is computed from these ten results by the rule in "
        "[METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).",
        "",
        "## Findings",
        "",
    ]
    for f in r["findings"]:
        lines.append(f"### {f['criterion']}. {f['title']}: {f['result']}")
        lines.append("")
        lines.append(f["finding"])
        lines.append("")
        srcs = ", ".join(f"<{s}>" for s in f["sources"])
        lines.append(f"Source: {srcs} ({'verified ' + f['verified'] if DATE_RE.match(f['verified']) else f['verified']})")
        lines.append("")
    lines += ["## Advisories published by the project", ""]
    if r["advisories"]:
        for a in r["advisories"]:
            ident = a["id"] + (f" / {a['cve']}" if a.get("cve") else "")
            summary = (a.get("summary") or "").rstrip(". ")
            lines.append(
                f"- {ident} ({a['severity']}, published {a['published']}): {summary}. "
                f"Affected: {a['affected']}. Patched: {a['patched'] or 'no patched version named'}. <{a['url']}>")
    else:
        lines.append(f"None in the repository's advisory list for this server on {r['verified']}.")
    lines.append("")
    if r["third_party_reports"]:
        lines += ["## Reported elsewhere", "",
                  "These items are not part of any result above. Each is reported by the named source and "
                  "is not confirmed in the project's own material.", ""]
        for t in r["third_party_reports"]:
            lines.append(f"- Reported by {t['reported_by']}, not confirmed in the project's own material: "
                         f"\"{t['title']}\". <{t['url']}> (page read {t['verified']})")
        lines.append("")
    if r["not_reverified"]:
        lines += ["## Not re-verified", ""] + [f"- {x}" for x in r["not_reverified"]] + [""]
    if r.get("open_disputes"):
        lines += ["## Disputed", "",
                  "One or more findings in this entry are disputed and under review:", ""]
        lines += [f"- <{u}>" for u in r["open_disputes"]] + [""]
    lines += [
        "## Dispute or update this entry",
        "",
        f"Open an issue at <{ISSUES_URL}> with the slug `{r['slug']}`, the criterion, and a link to the "
        "project's own material that shows the finding is wrong or out of date. "
        "The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    check_only = "--check" in sys.argv
    records, problems = load_records()
    for p in problems:
        print("PROBLEM:", p)
    print(f"{len(records)} entries loaded, {len(problems)} problems")
    if problems:
        return 1
    if check_only:
        stale = [r["slug"] for r in records
                 if not (SERVERS / f"{r['slug']}.md").exists()
                 or (SERVERS / f"{r['slug']}.md").read_text(encoding="utf-8") != render_markdown(r)]
        if stale:
            print("markdown out of date for:", ", ".join(stale))
            return 1
        return 0

    records.sort(key=lambda r: r["slug"])
    for r in records:
        (SERVERS / f"{r['slug']}.md").write_text(render_markdown(r), encoding="utf-8", newline="\n")

    counts = {o: sum(1 for r in records if r["outcome"] == o) for o in OUTCOMES}
    export = {
        "dataset": DATASET,
        "published_by": "Plainproof",
        "version": VERSION,
        "generated_at": date.today().isoformat(),
        "verified_dates": sorted({r["verified"] for r in records}),
        "methodology": "METHODOLOGY.md",
        "contesting": "CONTESTING.md",
        "issues": ISSUES_URL,
        "notice": NOTICE,
        "criteria": CRITERIA,
        "result_values": list(RESULTS),
        "outcome_rule": OUTCOME_RULE,
        "outcome_counts": counts,
        "entries": len(records),
        "servers": [dict(r, record=f"servers/{r['slug']}.md") for r in records],
    }
    (ROOT / "allowlist.json").write_text(
        json.dumps(export, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

    with (ROOT / "allowlist.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow([
            "slug", "name", "repository", "package", "publisher", "publisher_account_type",
            "license_spdx", "upstream_status", "latest_version", "latest_release_date", "stars",
            "outcome", "outcome_statement", *ORDER, "advisories_published", "verified", "record",
        ])
        for r in records:
            w.writerow([
                r["slug"], r["name"], r["repository"], r["package"], r["publisher"],
                r["publisher_account_type"], r.get("license_spdx") or "", r["upstream_status"],
                r["latest_release"]["version"], r["latest_release"]["date"], r["stars"],
                r["outcome"], r["outcome_statement"], *[r["results"][c] for c in ORDER],
                len(r["advisories"]), r["verified"], f"servers/{r['slug']}.md",
            ])
    print("wrote", len(records), "markdown entries, allowlist.json and allowlist.csv:", counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
