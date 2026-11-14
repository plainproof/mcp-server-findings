# PostgreSQL (archived reference server)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-server-postgres-archived` |
| Repository | <https://github.com/modelcontextprotocol/servers-archived> (`src/postgres`) |
| Package | `npm:@modelcontextprotocol/server-postgres` |
| Publisher | modelcontextprotocol (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `archived-upstream` - The repository is archived (read-only) on GitHub. The npm record marks the package deprecated. Quoted: “Archived and unmaintained; no security guarantees. See https://github.com/modelcontextprotocol/servers-archived”. The repository's own README says it is no longer maintained. Quoted: “This repository is archived and no longer maintained.”. |
| Latest release | 0.6.2 (2024-12-04) |
| Commit read | `9be4674d1ddf` on `main` (2025-05-28) |
| GitHub stars | 306 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-not-met` |

## Outcome

As of 2026-11-14: meets C4, C5, C7; partly meets C1, C2, C8, C10; does not meet C3, C6, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The npm record for @modelcontextprotocol/server-postgres@0.6.2 has no repository field; its deprecation notice names the archive repository. The record carries no provenance attestation. Quoted: “Archived and unmaintained; no security guarantees. See https://github.com/modelcontextprotocol/servers-archived”.

Source: <https://registry.npmjs.org/@modelcontextprotocol/server-postgres/latest>, <https://github.com/modelcontextprotocol/servers-archived> (verified 2026-11-14)

### C2. Published security policy: partly meets

GitHub shows a security policy for the repository (`SECURITY.md`); the policy says the repository is no longer covered by a vulnerability disclosure programme. Quoted: “This archived repository is no longer covered by our vulnerability disclosure program.”.

Source: <https://github.com/modelcontextprotocol/servers-archived/security/policy>, <https://github.com/modelcontextprotocol/servers-archived/blob/9be4674d1ddf8c469e6461a27a337eeb65f76c2e/SECURITY.md?plain=1#L16> (verified 2026-11-14)

### C3. Maintenance status: does not meet

The repository is archived (read-only) on GitHub. The npm record marks the package deprecated. Quoted: “Archived and unmaintained; no security guarantees. See https://github.com/modelcontextprotocol/servers-archived”. The repository's own README says it is no longer maintained. Quoted: “This repository is archived and no longer maintained.”. Latest release 0.6.2 is dated 2024-12-04; the newest commit on `main` is dated 2025-05-28; GitHub reports the last push on 2025-05-28.

Source: <https://api.github.com/repos/modelcontextprotocol/servers-archived>, <https://registry.npmjs.org/@modelcontextprotocol/server-postgres/latest>, <https://github.com/modelcontextprotocol/servers-archived/commits/main>, <https://github.com/modelcontextprotocol/servers-archived/blob/9be4674d1ddf8c469e6461a27a337eeb65f76c2e/README.md?plain=1#L3> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list for @modelcontextprotocol/server-postgres.

Source: <https://github.com/modelcontextprotocol/servers-archived/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: meets

The README describes the single tool as read-only. Quoted: “All queries are executed within a READ ONLY transaction”.

Source: <https://github.com/modelcontextprotocol/servers-archived/blob/9be4674d1ddf8c469e6461a27a337eeb65f76c2e/src/postgres/README.md?plain=1#L12> (verified 2026-11-14)

### C6. Credential handling in the documented setup: does not meet

The only documented setup passes the database address as a command-line argument, and the README says the user name and password can be placed in it. Quoted: “username/password can be added to the postgresql url with `postgresql://user:password@host:port/db-name`”; “postgresql://localhost/mydb”.

Source: <https://github.com/modelcontextprotocol/servers-archived/blob/9be4674d1ddf8c469e6461a27a337eeb65f76c2e/src/postgres/README.md?plain=1#L32> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `src/postgres/README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/modelcontextprotocol/servers-archived/blob/9be4674d1ddf8c469e6461a27a337eeb65f76c2e/src/postgres/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/modelcontextprotocol/servers-archived/blob/9be4674d1ddf8c469e6461a27a337eeb65f76c2e/package-lock.json>, <https://github.com/modelcontextprotocol/servers-archived/tree/9be4674d1ddf8c469e6461a27a337eeb65f76c2e> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `src/postgres/README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial; `SECURITY.md` for: prompt-injection, untrusted.

Source: <https://github.com/modelcontextprotocol/servers-archived/blob/9be4674d1ddf8c469e6461a27a337eeb65f76c2e/src/postgres/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: partly meets

Declared MCP library: @modelcontextprotocol/sdk 1.0.1. Lower-bound version 1.0.1 of @modelcontextprotocol/sdk (npm) was published on 2024-11-26, between 12 and 24 months before 2026-11-14.

Source: <https://registry.npmjs.org/@modelcontextprotocol/server-postgres/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Reported elsewhere

These items are not part of any result above. Each is reported by the named source and is not confirmed in the project's own material.

- Reported by Datadog Security Labs, not confirmed in the project's own material: "MCP vulnerability case study: SQL injection in the Postgres MCP server". <https://securitylabs.datadoghq.com/articles/mcp-vulnerability-case-study-SQL-injection-in-the-postgresql-mcp-server/> (page read 2026-11-14)

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-server-postgres-archived`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
