# Git (reference server)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-server-git` |
| Repository | <https://github.com/modelcontextprotocol/servers> (`src/git`) |
| Package | `pypi:mcp-server-git` |
| Publisher | modelcontextprotocol (GitHub organisation account) |
| Licence detected by GitHub | NOASSERTION |
| Upstream status | `active` |
| Latest release | 2026.11.11 (2026-11-11) |
| Commit read | `e1dc4b18dbb9` on `main` (2026-11-11) |
| GitHub stars | 91986 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C7, C10; partly meets C5, C8, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The PyPI record for mcp-server-git 2026.11.11 links the repository, and PyPI holds a provenance attestation for the release naming `modelcontextprotocol/servers` (workflow `release.yml`) as publisher.

Source: <https://pypi.org/pypi/mcp-server-git/json>, <https://pypi.org/integrity/mcp-server-git/2026.11.11/mcp_server_git-2026.11.11-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/modelcontextprotocol/servers/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 2026.11.11 is dated 2026-11-11; the newest commit on `main` is dated 2026-11-11; GitHub reports the last push on 2026-11-12.

Source: <https://api.github.com/repos/modelcontextprotocol/servers>, <https://pypi.org/pypi/mcp-server-git/json>, <https://github.com/modelcontextprotocol/servers/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

7 advisories are published in the repository's advisory list for mcp-server-git; each names a patched version at or below the latest release (2026.11.11). Most recent: GHSA-6hqx-gqrx-c5r2 (high, published 2026-11-11, patched in 2026.11.11).

Source: <https://github.com/modelcontextprotocol/servers/security/advisories>, <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-6hqx-gqrx-c5r2> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Tools that change a repository are available by default; `--repository` confines the server to one repository. Quoted: “**Without `--repository`, the server reads and writes any Git repository the server process can reach.**”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/git/README.md?plain=1#L172> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The documented setup takes no credential; the README notes that credentials embedded in remote addresses are redacted from tool output. Quoted: “A credential embedded in a URL is never returned”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/git/README.md?plain=1#L116> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `src/git/README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/git/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/package-lock.json>, <https://github.com/modelcontextprotocol/servers/tree/e1dc4b18dbb948921da37f3d4224a628730b43b0> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: partly meets

The README describes a control for configuration and hooks carried inside a repository; it does not name prompt injection or untrusted content. Quoted: “so the server never runs a program they name, with or without `--repository`”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/git/README.md?plain=1#L183> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: mcp<3,>=2.3. Lower-bound version 2.3.0 of mcp (PyPI) was published on 2026-10-02, within the 12 months before 2026-11-14.

Source: <https://pypi.org/pypi/mcp-server-git/json>, <https://pypi.org/pypi/mcp/json> (verified 2026-11-14)

## Advisories published by the project

- GHSA-6hqx-gqrx-c5r2 (high, published 2026-11-11): mcp-server-git: arbitrary command execution via a repository's own Git configuration (core.fsmonitor) during read-only tools. Affected: < 2026.11.11. Patched: 2026.11.11. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-6hqx-gqrx-c5r2>
- GHSA-q74p-4wrc-q7w6 (medium, published 2026-11-11): mcp-server-git: Incomplete Fix for GHSA-w766-5x43-whvw in validate_opened_repo() Allows --repository Confinement Bypass via objects/info/alternates and Linked-Worktree common_dir Confusion. Affected: >= 2026.10.28, < 2026.11.11. Patched: 2026.11.11. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-q74p-4wrc-q7w6>
- GHSA-w766-5x43-whvw (medium, published 2026-10-28): mcp-server-git: nested gitdir file bypasses --repository confinement. Affected: < 2026.10.28. Patched: 2026.10.28. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-w766-5x43-whvw>
- GHSA-vjqx-cfc4-9h6v / CVE-2026-27735 (medium, published 2026-02-25): Path traversal in git_add allows staging files outside repository boundaries in mcp-server-git. Affected: < 2026.1.14. Patched: 2026.1.14. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-vjqx-cfc4-9h6v>
- GHSA-5cgr-j3jf-jw3v / CVE-2025-68143 (medium, published 2025-12-17): Unrestricted git_init tool allows repository creation at arbitrary filesystem locations in mcp-server-git. Affected: < 2025.9.25. Patched: 2025.9.25. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-5cgr-j3jf-jw3v>
- GHSA-9xwc-hfwc-8w59 / CVE-2025-68144 (medium, published 2025-12-17): Argument injection in git_diff and git_checkout functions for mcp-server-git allows overwriting local files. Affected: < 2025.12.18. Patched: 2025.12.18. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-9xwc-hfwc-8w59>
- GHSA-j22h-9j4x-23w5 / CVE-2025-68145 (medium, published 2025-12-17): Missing path validation when using --repository flag in mcp-server-git. Affected: < 2025.12.18. Patched: 2025.12.18. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-j22h-9j4x-23w5>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-server-git`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
