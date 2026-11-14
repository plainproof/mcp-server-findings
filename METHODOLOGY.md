# Methodology

Plainproof MCP server review dataset, version 0.2 (all entries verified 2026-11-14).

This document defines, once, everything an entry refers to: which sources count, the ten criteria, how a result is worded, and how results are grouped. Every file in `servers/` follows it. If an entry and this document disagree, this document is right and the entry is a defect to report (see [CONTESTING.md](CONTESTING.md)).

## 1. What an entry is

One entry describes **one MCP server implementation as its publisher presented it on the verification date**: one repository (or one package inside a monorepo) at its latest released version.

An entry is a list of **findings**. Each finding states what a named public page said on the verification date, measured against one criterion. An entry is not a statement about the people who maintain a project, about their intent or ability, or about whether the software is safe to run.

## 2. Sources

### 2.1 What counts

Findings rest only on the project's **own public material**:

- its source repository (files, release pages, the repository metadata GitHub publishes for it);
- its README, documentation site and security policy;
- security advisories published in the repository's own advisory list;
- the package-registry record the publisher uploaded (npm, PyPI, NuGet, the Go module proxy, the publisher's own release site).

### 2.2 What does not count

Blog posts, scanner output, directory scores, news articles and research write-ups by anyone other than the publisher are **not** used to decide a result. Where such a report is listed at all, it sits in a separate `third_party_reports` block, worded "reported by <source>, not confirmed in the project's own material", and it changes no result.

### 2.3 How a source is recorded

Every finding carries:

- `source` — a URL that returned the content on the verification date. Repository files are linked at the exact commit that was read (a permalink), with a line number where a line is quoted;
- `verified` — the date the page was read;
- a short quotation where the finding depends on wording.

Where a finding says something is **absent** ("the README does not mention telemetry"), it means the listed file was searched for the listed terms and none was found. It does not mean the software was audited.

If a source could not be reached, the finding is marked `not re-verified <date>` and the entry lists it under `not_reverified`. Nothing is carried forward silently.

## 3. Selection

The set of 37 servers was frozen on 2026-08-23 and has not been changed since. It was drawn from public popularity lists (a search-demand ranking of MCP servers, a star-ranked GitHub list, and the reference-server list of the `modelcontextprotocol` organisation), taking for each popular category the publisher's own server where one exists and otherwise the most-starred dedicated implementation. Two reference servers that had already been archived were included on purpose, because archived packages can still be installed.

Being in the set says nothing about a project except that many people look for it. Not being in the set means "not reviewed".

Servers stay in the dataset when they are archived, renamed, transferred or withdrawn. The entry then records the upstream status (section 6) and what was observed.

## 4. The ten criteria

Each criterion has three possible results: **meets**, **partly meets**, **does not meet**. The definitions below are the whole test; nothing else is taken into account.

"Latest release" means the newest version on the package registry the project publishes to, or the newest GitHub release where there is no registry package. "The verification date" is the `verified` date of the entry.

### C1. Source and release provenance

- **Meets** — the source repository is public; the registry record of the latest release names that repository; and the release carries a provenance attestation or signature published by the project (npm provenance, a PyPI attestation naming the repository, signature files beside the release artefacts).
- **Partly meets** — the source repository is public and linked to the released artefact (the registry record names the repository, or, where the registry record has no repository field, the repository's own manifest declares the package), but no attestation or signature was found. Also used for servers offered only as a hosted endpoint, where there is no artefact to attest.
- **Does not meet** — the registry record names a repository address that does not resolve, or no public source repository is identified for the released artefact.
- **Read from** — registry record; PyPI integrity record; release asset list; the publisher's release site.

### C2. Published security policy

- **Meets** — GitHub shows a security policy for the repository (a `SECURITY.md` in the repository or one inherited from the owning organisation), and the policy describes how to report a vulnerability.
- **Partly meets** — no security policy is shown, but the repository's security page offers private vulnerability reporting, or the README names a channel for security reports; or a policy is shown that says reports for this repository are no longer covered.
- **Does not meet** — none of the above was found.
- **Read from** — `https://github.com/<owner>/<repo>/security/policy`; README.

### C3. Maintenance status

- **Meets** — the repository is not archived; the package is not marked deprecated on its registry; the project's own material does not describe it as superseded, deprecated, unmaintained or no longer supported; and a versioned release was published in the 180 days before the verification date.
- **Partly meets** — the repository is not archived and the package is not marked deprecated, and either (a) the latest release is older than 180 days while the repository shows activity (a commit on the default branch, or a push to any branch as reported by GitHub) within those 180 days, or (b) the project's own material says the server is superseded by, or deprecated in favour of, a successor while releases continue.
- **Does not meet** — the repository is archived; or the package is marked deprecated on its registry; or the project's own material says it is unmaintained or no longer supported; or there has been neither a release nor repository activity in the 180 days before the verification date.
- **Read from** — repository metadata (`archived`, `pushed_at`); default-branch commit list; release list; registry record; README.

### C4. Published advisories

Only advisories published in the repository's own advisory list are considered. For a monorepo, only advisories naming the reviewed package.

- **Meets** — no advisory is published for the server; or every published advisory names a patched version and the latest release is at or above it.
- **Partly meets** — a published advisory names no patched version, and its stated affected range does not clearly include the latest release (or is of low or moderate severity).
- **Does not meet** — a published advisory of high or critical severity names no patched version and its stated affected range includes the latest release.
- **Read from** — `https://github.com/<owner>/<repo>/security/advisories` and the individual advisory pages.

An advisory that is published and patched counts toward "meets": publishing and fixing is what the criterion asks for. The number of advisories is recorded but is not scored.

### C5. Documented scope controls

- **Meets** — the documentation describes the server as restricted by default (read-only by default, write tools off by default, or tools that only read or compute), so that write, delete or execute capability is absent or has to be switched on.
- **Partly meets** — the documentation describes write, delete or execute capability that is available by default, together with a documented way to restrict it (a read-only switch, tool or toolset selection, directory or project scoping, or scoping through the permissions of the credential).
- **Does not meet** — the documentation describes write, delete or execute capability and no way to restrict it was found in the README.
- **Read from** — README; the repository's security policy; documentation pages the README links to.

### C6. Credential handling in the documented setup

- **Meets** — the documented setup supplies credentials through environment variables, a credential or profile store, a key file, or an OAuth sign-in; or the server needs no credentials.
- **Partly meets** — the documentation shows both such a route and a route that places a secret in a command-line argument or in a connection address passed as an argument.
- **Does not meet** — the only documented setup places the secret in a command-line argument or in a connection address passed as an argument.
- **Read from** — README setup instructions.

### C7. Telemetry and outbound data, as documented

- **Meets** — the documentation states that no usage data is sent, or that telemetry is opt-in, or it contains no reference to telemetry or usage collection; and the server's documented function is to contact only the service the user configures.
- **Partly meets** — the documentation states that telemetry or usage reporting is on by default with a documented way to turn it off; or the server's documented function is to retrieve arbitrary web addresses or drive a browser to arbitrary pages.
- **Does not meet** — the documentation states that usage data is collected and documents no way to turn it off.
- **Read from** — README; privacy or telemetry sections it links to.

### C8. Dependency management files

- **Meets** — a dependency lockfile (or, for .NET, a central package-version file) is committed, and an automated dependency-update configuration (Dependabot or Renovate) is present in the repository.
- **Partly meets** — one of the two is present.
- **Does not meet** — neither is present.
- **Read from** — the repository tree at the verified commit. Paths checked: `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lock`, `bun.lockb`, `uv.lock`, `poetry.lock`, `go.sum`, `Cargo.lock`, `Directory.Packages.props`; `.github/dependabot.yml`, `.github/dependabot.yaml`, `renovate.json`, `renovate.json5`, `.github/renovate.json`, `.github/renovate.json5`, `.renovaterc`, `.renovaterc.json`. Update automation that is configured only in repository settings is not visible publicly and is not counted.

### C9. Documentation of untrusted-content risk

- **Meets** — the README, security policy or first-party documentation names prompt injection or untrusted content as a risk and describes a control or a recommendation for it; or the documented tools return only values the server computes or data the same client stored through it.
- **Partly meets** — the documentation carries a general security caution that bears on model-driven use (for example "not a security boundary", or a warning about what the server can reach) without naming prompt injection or untrusted content; or it names untrusted content without describing a control or recommendation.
- **Does not meet** — no such statement was found. Terms searched in the README: "prompt injection", "untrusted", "malicious", "attacker", "adversarial"; in the security policy: "prompt injection", "untrusted".
- **Read from** — README; `SECURITY.md`; documentation pages the README links to for security.

### C10. Currency of the declared MCP library

The MCP library is whatever protocol library the released package declares: an official MCP SDK or another MCP framework. Where a range is declared, its **lower bound** is used; where several MCP libraries are declared, the most recently released lower bound is used. Where the server implements the protocol itself, the newest specification revision named in its source tree is used instead.

- **Meets** — that library version (or specification revision) was published within the 12 months before the verification date.
- **Partly meets** — published between 12 and 24 months before the verification date.
- **Does not meet** — published more than 24 months before the verification date, or no MCP library or protocol revision could be identified.
- **Read from** — the registry record's dependency list, or the manifest in the repository; the library's own registry record for its release date.

No conformance test was run. This criterion says how recent the declared library is, not whether the server conforms to any specification revision.

## 5. How an outcome is worded and grouped

### 5.1 The outcome statement

Every entry carries one sentence built mechanically from its ten results:

> As of 2026-11-14: meets C1, C2, C6; partly meets C5, C8; does not meet C3.

That sentence, together with the ten findings behind it, is the outcome. Nothing in an entry says more than that.

### 5.2 Groups

For filtering, entries are placed in one of three groups. The group is computed from the ten results by the rule below and by nothing else. A group label describes the findings on the verification date; it does not describe the project or the people behind it, and it is not a recommendation.

| Group (`outcome`) | Rule |
| --- | --- |
| `criteria-met` | No criterion is "does not meet"; C4 is "meets"; at most four criteria are "partly meets". |
| `criteria-not-met` | "Does not meet" on C1, C3 or C4, or on three or more criteria. |
| `criteria-partly-met` | Every other combination. |

C1, C3 and C4 are singled out because they describe whether the thing installed can be tied to public source, is still published by someone, and has no open published advisory; the other seven describe how it is configured and documented.

There are no overrides. If the rule gives a result that looks wrong, the fix is a correction to a finding or a change to this document, both of which are recorded in [CHANGELOG.md](CHANGELOG.md).

## 6. Upstream status

`upstream_status` records what the publisher's own pages show about the project's state:

| Value | Meaning |
| --- | --- |
| `active` | Not archived, not deprecated, no statement of discontinuation. |
| `renamed` / `transferred` | The repository address used when the set was selected now redirects to another name or owner. The entry gives both. |
| `superseded-upstream` | The project's README says a successor replaces it, while releases continue (C3 "partly meets"). |
| `unmaintained-per-publisher` | The project's README says it is no longer maintained or supported. |
| `inactive` | Not archived, but no release and no repository activity in 180 days. |
| `archived-upstream` | The repository is archived (read-only) on GitHub, or the package is marked deprecated on its registry. |
| `withdrawn` | The repository or package no longer resolves. |

## 7. Procedure

For each server, on the verification date:

1. Read the repository metadata; note redirects, the archived flag, the default branch and its newest commit.
2. Read the release list and the registry record of the latest release.
3. Read the repository's security-policy page and its published advisories.
4. Read the README at the newest commit, and the documentation pages it points to for scope, credentials, telemetry and security.
5. Check the dependency-management paths listed under C8.
6. Read the declared MCP library version and look up when that version was published.
7. Write the ten findings with their sources; compute the outcome statement and group.

Entries are compiled with AI assistance: every source page is fetched and read on the verification date, quotations are checked mechanically against the fetched text, and absence findings are checked by searching the fetched text. `build_export.py` then validates each entry and regenerates the exports.

## 8. Limits

- **Snapshot.** Everything is as of the `verified` date. Projects release, patch, rename and archive continuously; an entry can be out of date the day after it is written.
- **Documentation, not behaviour.** Criteria C5, C6, C7 and C9 describe what the documentation says. No code was executed, no network traffic was observed, no source audit was performed.
- **Not a scan.** No vulnerability scanner, dependency scanner or conformance suite was run.
- **Advisories.** Only advisories in the repository's own list are counted. A vulnerability that has not been published there is invisible to C4.
- **Monorepos.** Repository-level facts (stars, commits, security policy) are shared by every package in a monorepo.
- **Absence findings** are bounded by the files and terms listed in the finding.
- **Selection** reflects popularity lists from August 2026.

## 9. Corrections

Anyone, and in particular the maintainers of a listed project, can dispute or update a finding. The route, what to send and what happens next are in [CONTESTING.md](CONTESTING.md).

## 10. Changes to this document

| Version | Date | Change |
| --- | --- | --- |
| 0.2 | 2026-11-14 | Sources restricted to the project's own public material. Criteria redefined so each result is a documented, checkable finding. Outcome wording changed to "meets / partly meets / does not meet"; groups renamed and computed by rule only; numeric totals and reviewer overrides removed. Upstream status added. |
| 0.1 | 2026-08-28 | First internal build (not published). |
