# Changelog

All changes to entries, criteria and format are recorded here. Corrections made after a dispute link to the issue that prompted them (see [CONTESTING.md](CONTESTING.md)).

## 0.2 (2026-11-14)

First version prepared for publication. Version 0.1 (2026-08-28) was an internal draft and was never published.

### What was done

- **All 37 entries re-read on 2026-11-14** from each project's repository, release list, registry record, security policy, advisory list and README. Every finding carries a source and `verified: 2026-11-14`. No entry was carried forward from the draft. Findings not re-verified: none.
- **Sources restricted to the project's own public material.** Findings that rested on third-party articles, trackers or scanners were dropped. Two third-party articles are kept in a separate "Reported elsewhere" block, marked as not confirmed in the project's own material; they change no result.
- **Criteria redefined** so that each result is a checkable statement about a public page (METHODOLOGY.md, section 4). C2 no longer considers who the maintainer is, only whether a security policy is published. C4 counts only advisories in the repository's own list. C7, C8, C9 and C10 are defined by what is documented or declared, not by inspection of code.
- **Outcome wording changed** to "meets / partly meets / does not meet" per criterion, with one summary sentence per entry. Groups renamed to `criteria-met`, `criteria-partly-met`, `criteria-not-met` and computed by rule only. Numeric totals, reviewer overrides, per-entry conditions and recommendations of alternative projects were removed.
- **Upstream status added** (`active`, `renamed`, `transferred`, `superseded-upstream`, `unmaintained-per-publisher`, `inactive`, `archived-upstream`, `withdrawn`). No server was removed.
- **Format.** The JSON file is now the source of each entry and the markdown page is generated from it. Reviewer and sign-off fields were removed. `CONTESTING.md`, `LICENSE` (CC BY-SA 4.0), `LICENSE-CODE` (MIT) and this file were added. `build_export.py` was rewritten for the new schema.

### Group counts

The draft's three groups are given here in v0.2 vocabulary (draft "allowlist" = `criteria-met`, "conditional" = `criteria-partly-met`, "deny" = `criteria-not-met`). Because the criteria were redefined, a move between groups can come from a changed fact, a changed definition, or both; the table below says which facts changed.

| Group | 0.1 draft (2026-08-28) | 0.2 (2026-11-14) |
| --- | ---: | ---: |
| `criteria-met` | 13 | 14 |
| `criteria-partly-met` | 20 | 17 |
| `criteria-not-met` | 4 | 6 |

11 of 37 entries are in a different group than in the draft; 26 are in the same group.

### Upstream changes observed since the draft

- `awslabs-aws-api-mcp`: `superseded-upstream`. The README says the server is superseded by another AWS MCP server and that a deprecation notice is shown at start-up; releases continued (1.6.0 on 2026-10-27). Quoted: “This MCP server is superseded by the official [AWS MCP server]”.
- `claude-task-master`: `inactive`. No release and no repository activity in the 180 days before 2026-11-14.
- `executeautomation-mcp-playwright`: `inactive` (already without activity at the time of the draft). No release and no repository activity in the 180 days before 2026-11-14.
- `genai-toolbox`: `renamed`. The repository was renamed from googleapis/genai-toolbox to googleapis/mcp-toolbox; the old address redirects. Quoted: “The `genai-toolbox` repository has been officially renamed to `mcp-toolbox`.”.
- `gmail-mcp-server-gongrzhe`: `archived-upstream` (already archived at the time of the draft). The repository is archived (read-only) on GitHub.
- `mcp-server-postgres-archived`: `archived-upstream` (already archived at the time of the draft). The repository is archived (read-only) on GitHub. The npm record marks the package deprecated. Quoted: “Archived and unmaintained; no security guarantees. See https://github.com/modelcontextprotocol/servers-archived”. The repository's own README says it is no longer maintained. Quoted: “This repository is archived and no longer maintained.”.
- `mcp-server-puppeteer-archived`: `archived-upstream` (already archived at the time of the draft). The repository is archived (read-only) on GitHub. The npm record marks the package deprecated. Quoted: “Archived and unmaintained; no security guarantees. See https://github.com/modelcontextprotocol/servers-archived”. The repository's own README says it is no longer maintained. Quoted: “This repository is archived and no longer maintained.”.
- `notion-mcp-server`: `unmaintained-per-publisher`. The README says this self-hosted server is no longer actively maintained or supported and points to the publisher's hosted server. The latest release (2.6.1) is dated 2026-10-29.
- `sentry-mcp`: `renamed`. The repository was renamed from getsentry/sentry-mcp to getsentry/toolkit; the old address redirects. The npm package name is unchanged. Quoted: “ships the same server, bundled without the rest of the CLI, for clients that”.
- `supabase-mcp`: `transferred`. The repository moved from supabase-community/supabase-mcp to supabase/mcp; the old address redirects. The npm package name is unchanged.

### Entry by entry

"Results" lists the criteria that are not simply "meets". "Advisories" counts those in the repository's own list for the server; "new" means published after 2026-08-28.

| Entry | Latest release: draft → now | Group: draft → now | Results now | Advisories | What changed |
| --- | --- | --- | --- | --- | --- |
| `awslabs-aws-api-mcp` | 1.5.3 → 1.6.0 (2026-10-27) | criteria-met (same) | partly meets: C3, C5, C7 | 4 (2 new) | The README now states that the server is superseded by another AWS MCP server. Stars 9640 → 9919. |
| `azure-mcp` | 3.0.0-beta.38 → 4.0.0-beta.7 (2026-11-11) | criteria-met (same) | partly meets: C1, C5, C7 | 0 | Third-party sources not carried over: api.osv.dev, osv.dev. Stars 3613 → 3853. |
| `claude-task-master` | 0.43.1, no newer release | criteria-partly-met → **criteria-not-met** | partly meets: C2, C5, C8; does not meet: C3, C9 | 0 | No release and no repository activity in the 180 days before 2026-11-14. Group follows from C3. Stars 28023 → 28359. |
| `cloudflare-mcp` | containers-mcp@0.2.19 → workers-observability@0.6.0 (2026-10-22) | criteria-met → **criteria-partly-met** | partly meets: C1, C5, C8; does not meet: C9 | 0 | Group follows from unmet C9 under the v0.2 definitions. Stars 4121 → 4465. |
| `context7` | 4.0.3 → 4.7.0 (2026-11-12) | criteria-partly-met (same) | partly meets: C1; does not meet: C9 | 0 | The v0.1 draft counted a CVE and an incident described on third-party sites. The repository's own advisory list showed no published advisory on 2026-11-14, so neither is used. Third-party sources not carried over: www.digitalapplied.com, www.noma.security. Stars 61302 → 64792. |
| `desktop-commander` | 0.2.47 → 0.3.3 (2026-11-12) | criteria-partly-met → **criteria-met** | partly meets: C5, C7, C8 | 0 | The v0.1 draft counted CVE entries from third-party trackers. The repository's own advisory list showed no published advisory on 2026-11-14, so they are not used. No criterion is unmet under the v0.2 definitions. Third-party sources not carried over: cve.threatint.eu, feedly.com, secalerts.co, vulnerability.circl.lu. Stars 9416 → 10307. |
| `executeautomation-mcp-playwright` | 1.0.12, no newer release | criteria-not-met (same) | partly meets: C1, C7, C8; does not meet: C2, C3, C5, C9 | 0 | Third-party sources not carried over: intel.aikido.dev. Stars 5637 → 5680. |
| `figma-context-mcp` | 0.13.2, no newer release | criteria-partly-met (same) | partly meets: C6, C8; does not meet: C9 | 1 | Stars 15723 → 16206. |
| `firecrawl-mcp-server` | 3.24.0 → 3.40.0 (2026-11-12) | criteria-partly-met (same) | partly meets: C5, C7, C8; does not meet: C2, C9 | 0 | Third-party sources not carried over: cve.imfht.com. Stars 7331 → 7817. |
| `genai-toolbox` | v1.9.0 → v1.17.0 (2026-11-13) | criteria-partly-met (same) | partly meets: C5; does not meet: C9 | 0 | Repository now at googleapis/mcp-toolbox (was googleapis/genai-toolbox). Repository renamed upstream; advisories cited in the v0.1 draft from third-party sites are not in the repository's own advisory list and are not used. Third-party sources not carried over: cyberpress.org, www.secure-iss.com. Stars 16266 → 16872. |
| `github-mcp-server` | v1.11.0 → v2.1.0 (2026-11-03) | criteria-partly-met (same) | partly meets: C1, C4, C5 | 2 | A third-party article cited in the v0.1 draft is now listed under "Reported elsewhere" and changes no result. Stars 32561 → 34455. |
| `gitlab-mcp-zereight` | 2.1.53 → 2.3.27 (2026-11-13) | criteria-partly-met → **criteria-met** | partly meets: C5 | 31 (25 new) | The v0.1 draft relied on third-party vulnerability reports. The repository now publishes its own advisories, each naming a patched version at or below the latest release. No criterion is unmet under the v0.2 definitions. Third-party sources not carried over: intel.aikido.dev. Stars 1928 → 2105. |
| `gmail-mcp-server-gongrzhe` | 1.1.11, no newer release | criteria-not-met (same) | partly meets: C8; does not meet: C1, C2, C3, C5, C9, C10 | 0 | Stars 1165 → 1169. |
| `kubernetes-mcp-server-containers` | v0.0.66 → 0.1.3 (2026-11-13) | criteria-met (same) | partly meets: C5, C9 | 1 (1 new) | Stars 2032 → 2249. |
| `mcp-atlassian-sooperset` | 0.23.1 → 0.24.4 (2026-11-13) | criteria-partly-met (same) | partly meets: C1, C5, C8; does not meet: C9 | 55 (19 new) | Third-party sources not carried over: arcticwolf.com, raxe.ai, www.sentinelone.com. Stars 5802 → 6119. |
| `mcp-grafana` | v1.2.0 → v2.3.0 (2026-11-10) | criteria-met → **criteria-partly-met** | partly meets: C5, C7; does not meet: C9 | 0 | Group follows from unmet C9 under the v0.2 definitions. Stars 3398 → 3668. |
| `mcp-neo4j` | 0.6.0, no newer release | criteria-partly-met (same) | partly meets: C1, C3, C5, C6, C8, C9, C10 | 2 | Stars 979 → 989. |
| `mcp-redis` | 0.5.1, no newer release | criteria-partly-met (same) | partly meets: C5, C6; does not meet: C2, C9 | 0 | Stars 605 → 642. |
| `mcp-server-fetch` | 2026.8.18 → 2026.11.11 (2026-11-11) | criteria-partly-met → **criteria-met** | partly meets: C7, C8, C9 | 5 (5 new) | The v0.1 draft cited a mailing-list disclosure as unfixed. The repository's own advisory list now carries advisories for the fetch server, each patched at or below the latest release. No criterion is unmet under the v0.2 definitions. Third-party sources not carried over: seclists.org. Stars 89909 → 91986. |
| `mcp-server-filesystem` | 2026.7.10 → 2.3.0 (2026-11-11) | criteria-met → **criteria-partly-met** | partly meets: C5, C8; does not meet: C9 | 8 (6 new) | Group follows from unmet C9 under the v0.2 definitions. Third-party sources not carried over: cymulate.com. Stars 89909 → 91986. |
| `mcp-server-git` | 2026.8.18 → 2026.11.11 (2026-11-11) | criteria-met (same) | partly meets: C5, C8, C9 | 7 (3 new) | Third-party sources not carried over: api.osv.dev. Stars 89909 → 91986. |
| `mcp-server-kubernetes-flux159` | 4.1.4 → 4.2.3 (2026-11-13) | criteria-partly-met (same) | partly meets: C5, C8; does not meet: C9 | 11 (4 new) | The v0.1 draft lowered this entry by reviewer override. Overrides no longer exist; the group follows from the rule alone. Third-party sources not carried over: osv.dev. Stars 1577 → 1612. |
| `mcp-server-memory` | 2026.7.4 → 2.1.1 (2026-11-11) | criteria-met (same) | partly meets: C8 | 0 | Third-party sources not carried over: app.opencve.io. Stars 89909 → 91986. |
| `mcp-server-mysql-benborla` | 2.0.9, no newer release | criteria-partly-met (same) | partly meets: C1, C8, C10; does not meet: C2, C9 | 0 | Third-party sources not carried over: www.pulsemcp.com. Stars 2081 → 2218. |
| `mcp-server-postgres-archived` | 0.6.2, no newer release | criteria-not-met (same) | partly meets: C1, C2, C8, C10; does not meet: C3, C6, C9 | 0 | The v0.1 draft based C4 on a third-party article. C4 now counts only advisories in the repository's own list (none); the article is listed under "Reported elsewhere" and changes no result. Third-party sources not carried over: www.trendmicro.com. |
| `mcp-server-puppeteer-archived` | 2025.5.12, no newer release | criteria-not-met (same) | partly meets: C1, C2, C7, C8, C9, C10; does not meet: C3, C5 | 0 | Third-party sources not carried over: api.osv.dev. |
| `mcp-server-qdrant` | 0.8.1, no newer release | criteria-partly-met (same) | partly meets: C1, C2, C3, C5, C10; does not meet: C9 | 0 | Stars 1516 → 1570. |
| `mcp-server-sequential-thinking` | 2026.7.4 → 2.1.1 (2026-11-04) | criteria-met (same) | partly meets: C8 | 0 | Third-party sources not carried over: api.osv.dev. Stars 89909 → 91986. |
| `mcp-server-time` | 2026.8.18 → 2026.11.11 (2026-11-11) | criteria-met (same) | partly meets: C8 | 0 | Third-party sources not carried over: api.osv.dev. Stars 89909 → 91986. |
| `notion-mcp-server` | 2.5.1 → 2.6.1 (2026-10-29) | criteria-partly-met → **criteria-not-met** | partly meets: C5, C8, C9; does not meet: C2, C3 | 0 | The README now states that this self-hosted server is no longer actively maintained or supported. Group follows from C3. Stars 4611 → 4707. |
| `playwright-mcp` | 0.0.79 → 0.0.85 (2026-11-09) | criteria-met (same) | partly meets: C5, C7, C9 | 0 | Third-party sources not carried over: seclists.org, www.vulncheck.com. Stars 36542 → 39634. |
| `postgres-mcp-pro` | 0.3.0, no newer release | criteria-partly-met (same) | partly meets: C1, C3, C5, C6, C8, C9, C10; does not meet: C2 | 0 | Third-party sources not carried over: dbhub.ai. Stars 3231 → 3475. |
| `sentry-mcp` | 0.39.0 → 0.49.0 (2026-11-07) | criteria-met → **criteria-partly-met** | partly meets: C1, C5, C8; does not meet: C9 | 0 | Repository now at getsentry/toolkit (was getsentry/sentry-mcp). Repository renamed upstream. Group follows from unmet C9 under the v0.2 definitions. Stars 830 → 964. |
| `serena` | 1.7.0 → 2.1.0 (2026-10-19) | criteria-partly-met → **criteria-met** | partly meets: C1, C2, C5, C8 | 3 (1 new) | No criterion is unmet under the v0.2 definitions. Third-party sources not carried over: about.gitlab.com. Stars 28545 → 31374. |
| `slack-mcp-server-korotovsky` | 1.3.0, no newer release | criteria-partly-met (same) | partly meets: C1, C3; does not meet: C9 | 0 | The v0.1 draft counted the documented browser-session-token mode against C6. In v0.2, C6 concerns only where a secret is placed in the documented setup; the README's description of the token types is quoted without assessment. Stars 1799 → 1898. |
| `supabase-mcp` | 0.11.0 → 0.17.0 (2026-11-13) | criteria-partly-met → **criteria-met** | partly meets: C5 | 0 | Repository now at supabase/mcp (was supabase-community/supabase-mcp). The v0.1 draft result rested on third-party research. It is not used; the publisher's own documentation on prompt injection is cited under C9 instead. No criterion is unmet under the v0.2 definitions. Third-party sources not carried over: generalanalysis.com. Stars 2874 → 3010. |
| `terraform-mcp-server` | v1.3.0 → v1.4.1 (2026-10-23) | criteria-met (same) | partly meets: C9 | 0 | Stars 1513 → 1562. |

### Removed from the dataset folder

- The internal review-sample note and the hand-written entry template of the draft (entries are now generated from JSON).

## 0.1 (2026-08-28)

Internal draft, not published.
