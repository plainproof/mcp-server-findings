# MCP Server for MySQL (benborla)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-server-mysql-benborla` |
| Repository | <https://github.com/benborla/mcp-server-mysql> |
| Package | `npm:@benborla29/mcp-server-mysql` |
| Publisher | benborla (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 2.0.9 (2026-06-19) |
| Commit read | `b9c714e18242` on `main` (2026-07-27) |
| GitHub stars | 2218 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C3, C4, C5, C6, C7; partly meets C1, C8, C10; does not meet C2, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The npm record for @benborla29/mcp-server-mysql@2.0.9 names the repository `git+https://github.com/benborla/mcp-server-mysql.git`. The record carries no provenance attestation (`dist.attestations` is absent).

Source: <https://registry.npmjs.org/@benborla29/mcp-server-mysql/latest> (verified 2026-11-14)

### C2. Published security policy: does not meet

GitHub's security-policy page for the repository says "No security policy detected" and offers no private vulnerability reporting; the README names no channel for security reports (searched for: security@, vulnerability, responsible disclosure, report security).

Source: <https://github.com/benborla/mcp-server-mysql/security/policy>, <https://github.com/benborla/mcp-server-mysql/blob/b9c714e182422b9f18437242b80cf003adf1c7ea/README.md> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 2.0.9 is dated 2026-06-19; the newest commit on `main` is dated 2026-07-27; GitHub reports the last push on 2026-07-27.

Source: <https://api.github.com/repos/benborla/mcp-server-mysql>, <https://registry.npmjs.org/@benborla29/mcp-server-mysql/latest>, <https://github.com/benborla/mcp-server-mysql/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/benborla/mcp-server-mysql/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: meets

The README describes the server as read-only by default, with write operations switched on by environment flags. Quoted: “**Read-only by default** — write operations opt-in via env flags”.

Source: <https://github.com/benborla/mcp-server-mysql/blob/b9c714e182422b9f18437242b80cf003adf1c7ea/README.md?plain=1#L19> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

Database credentials are supplied through environment variables. Quoted: “"MYSQL_PASS": "your_password",”.

Source: <https://github.com/benborla/mcp-server-mysql/blob/b9c714e182422b9f18437242b80cf003adf1c7ea/README.md?plain=1#L60> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/benborla/mcp-server-mysql/blob/b9c714e182422b9f18437242b80cf003adf1c7ea/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/benborla/mcp-server-mysql/blob/b9c714e182422b9f18437242b80cf003adf1c7ea/package-lock.json>, <https://github.com/benborla/mcp-server-mysql/tree/b9c714e182422b9f18437242b80cf003adf1c7ea> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/benborla/mcp-server-mysql/blob/b9c714e182422b9f18437242b80cf003adf1c7ea/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: partly meets

Declared MCP library: @modelcontextprotocol/sdk 1.15.1. Lower-bound version 1.15.1 of @modelcontextprotocol/sdk (npm) was published on 2025-07-10, between 12 and 24 months before 2026-11-14.

Source: <https://registry.npmjs.org/@benborla29/mcp-server-mysql/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-server-mysql-benborla`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
