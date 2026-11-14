# Neo4j Cypher MCP server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-neo4j` |
| Repository | <https://github.com/neo4j-contrib/mcp-neo4j> (`servers/mcp-neo4j-cypher`) |
| Package | `pypi:mcp-neo4j-cypher` |
| Publisher | neo4j-contrib (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 0.6.0 (2026-04-10) |
| Commit read | `1c7ad0793b5f` on `main` (2026-09-09) |
| GitHub stars | 989 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C2, C4, C7; partly meets C1, C3, C5, C6, C8, C9, C10.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The PyPI record for mcp-neo4j-cypher 0.6.0 lists no project or repository URL; the repository's `servers/mcp-neo4j-cypher/pyproject.toml` declares the package name `mcp-neo4j-cypher`. PyPI holds no provenance attestation for the release (the integrity record returned HTTP 404).

Source: <https://pypi.org/pypi/mcp-neo4j-cypher/json>, <https://github.com/neo4j-contrib/mcp-neo4j/blob/1c7ad0793b5f06b42b9c44f855c23eb2064c3bb7/servers/mcp-neo4j-cypher/pyproject.toml>, <https://pypi.org/integrity/mcp-neo4j-cypher/0.6.0/mcp_neo4j_cypher-0.6.0-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/neo4j-contrib/mcp-neo4j/security/policy> (verified 2026-11-14)

### C3. Maintenance status: partly meets

The repository is not archived. The latest release is 218 days old (more than 180); repository activity falls within the last 180 days. Latest release 0.6.0 is dated 2026-04-10; the newest commit on `main` is dated 2026-09-09; GitHub reports the last push on 2026-09-09.

Source: <https://api.github.com/repos/neo4j-contrib/mcp-neo4j>, <https://pypi.org/pypi/mcp-neo4j-cypher/json>, <https://github.com/neo4j-contrib/mcp-neo4j/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

2 advisories are published in the repository's advisory list for mcp-neo4j-cypher; each names a patched version at or below the latest release (0.6.0). Most recent: GHSA-x3cv-r3g3-fpg9 (low, published 2026-04-17, patched in 0.6.0).

Source: <https://github.com/neo4j-contrib/mcp-neo4j/security/advisories>, <https://github.com/neo4j-contrib/mcp-neo4j/security/advisories/GHSA-x3cv-r3g3-fpg9> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The write tool is available unless read-only mode is set. Quoted: “**Availability**: May be disabled by supplying --read-only as cli flag or `NEO4J_READ_ONLY=true` environment variable”.

Source: <https://github.com/neo4j-contrib/mcp-neo4j/blob/1c7ad0793b5f06b42b9c44f855c23eb2064c3bb7/servers/mcp-neo4j-cypher/README.md?plain=1#L48> (verified 2026-11-14)

### C6. Credential handling in the documented setup: partly meets

Environment variables are the preferred route; passing the password as a command-line argument is also documented. Quoted: “Syntax with `--db-url`, `--username`, `--password`, `--read-timeout` and other command line arguments is still supported but environment variables are preferred:”.

Source: <https://github.com/neo4j-contrib/mcp-neo4j/blob/1c7ad0793b5f06b42b9c44f855c23eb2064c3bb7/servers/mcp-neo4j-cypher/README.md?plain=1#L352> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `servers/mcp-neo4j-cypher/README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/neo4j-contrib/mcp-neo4j/blob/1c7ad0793b5f06b42b9c44f855c23eb2064c3bb7/servers/mcp-neo4j-cypher/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`servers/mcp-neo4j-cypher/uv.lock`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/neo4j-contrib/mcp-neo4j/blob/1c7ad0793b5f06b42b9c44f855c23eb2064c3bb7/servers/mcp-neo4j-cypher/uv.lock>, <https://github.com/neo4j-contrib/mcp-neo4j/tree/1c7ad0793b5f06b42b9c44f855c23eb2064c3bb7> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: partly meets

The README has security guidance for the HTTP transport; it does not name prompt injection or untrusted content returned by tools. Quoted: “Malicious websites cannot trick browsers into accessing your local server”.

Source: <https://github.com/neo4j-contrib/mcp-neo4j/blob/1c7ad0793b5f06b42b9c44f855c23eb2064c3bb7/servers/mcp-neo4j-cypher/README.md?plain=1#L218> (verified 2026-11-14)

### C10. Currency of the declared MCP library: partly meets

Declared MCP library: fastmcp<2.14,>=2.10.5. Lower-bound version 2.10.5 of fastmcp (PyPI) was published on 2025-07-11, between 12 and 24 months before 2026-11-14.

Source: <https://pypi.org/pypi/mcp-neo4j-cypher/json>, <https://pypi.org/pypi/fastmcp/json> (verified 2026-11-14)

## Advisories published by the project

- GHSA-x3cv-r3g3-fpg9 / CVE-2026-35402 (low, published 2026-04-17): SSRF and Data Modification via read_only Mode Bypass through CALL Procedures. Affected: <0.6.0. Patched: 0.6.0. <https://github.com/neo4j-contrib/mcp-neo4j/security/advisories/GHSA-x3cv-r3g3-fpg9>
- GHSA-vcqx-v2mg-7chx / CVE-2025-10193 (high, published 2025-09-11): DNS rebinding vulnerability in Neo4j Cypher MCP server. Affected: >= 0.2.2, <= 0.3.1. Patched: v0.4.0. <https://github.com/neo4j-contrib/mcp-neo4j/security/advisories/GHSA-vcqx-v2mg-7chx>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-neo4j`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
