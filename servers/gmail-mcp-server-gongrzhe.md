# Gmail AutoAuth MCP Server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `gmail-mcp-server-gongrzhe` |
| Repository | <https://github.com/GongRzhe/Gmail-MCP-Server> |
| Package | `npm:@gongrzhe/server-gmail-autoauth-mcp` |
| Publisher | GongRzhe (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `archived-upstream` - The repository is archived (read-only) on GitHub. |
| Latest release | 1.1.11 (2025-08-06) |
| Commit read | `a890d19189bb` on `main` (2025-08-06) |
| GitHub stars | 1169 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-not-met` |

## Outcome

As of 2026-11-14: meets C4, C6, C7; partly meets C8; does not meet C1, C2, C3, C5, C9, C10.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: does not meet

The npm record for @gongrzhe/server-gmail-autoauth-mcp@1.1.11 names the repository `git+https://github.com/gongrzhe/server-gmail-autoauth-mcp.git`. That address returned HTTP 404 on the verification date. The record carries no provenance attestation. (The repository reviewed here, GongRzhe/Gmail-MCP-Server, declares the same package name in its package.json.)

Source: <https://registry.npmjs.org/@gongrzhe/server-gmail-autoauth-mcp/latest>, <https://github.com/gongrzhe/server-gmail-autoauth-mcp>, <https://github.com/GongRzhe/Gmail-MCP-Server/blob/a890d19189bbc1325b8728fab830fc278cfd8804/package.json> (verified 2026-11-14)

### C2. Published security policy: does not meet

GitHub's security-policy page for the repository says "No security policy detected" and offers no private vulnerability reporting; the README names no channel for security reports (searched for: security@, vulnerability, responsible disclosure, report security).

Source: <https://github.com/GongRzhe/Gmail-MCP-Server/security/policy>, <https://github.com/GongRzhe/Gmail-MCP-Server/blob/a890d19189bbc1325b8728fab830fc278cfd8804/README.md> (verified 2026-11-14)

### C3. Maintenance status: does not meet

The repository is archived (read-only) on GitHub. Latest release 1.1.11 is dated 2025-08-06; the newest commit on `main` is dated 2025-08-06; GitHub reports the last push on 2025-08-06.

Source: <https://api.github.com/repos/GongRzhe/Gmail-MCP-Server>, <https://registry.npmjs.org/@gongrzhe/server-gmail-autoauth-mcp/latest>, <https://github.com/GongRzhe/Gmail-MCP-Server/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/GongRzhe/Gmail-MCP-Server/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: does not meet

The README documents tools that send, modify and delete email; no read-only mode or tool restriction was found in the README. Searched `README.md` for: read-only, readonly, restrict, disable. Quoted: “Sends a new email immediately.”; “Permanently deletes an email.”.

Source: <https://github.com/GongRzhe/Gmail-MCP-Server/blob/a890d19189bbc1325b8728fab830fc278cfd8804/README.md?plain=1#L188>, <https://github.com/GongRzhe/Gmail-MCP-Server/blob/a890d19189bbc1325b8728fab830fc278cfd8804/README.md> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

OAuth client keys and tokens are kept in a key file under the user's home directory. Quoted: “OAuth credentials are stored securely in your local environment (`~/.gmail-mcp/`)”.

Source: <https://github.com/GongRzhe/Gmail-MCP-Server/blob/a890d19189bbc1325b8728fab830fc278cfd8804/README.md?plain=1#L694> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/GongRzhe/Gmail-MCP-Server/blob/a890d19189bbc1325b8728fab830fc278cfd8804/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/GongRzhe/Gmail-MCP-Server/blob/a890d19189bbc1325b8728fab830fc278cfd8804/package-lock.json>, <https://github.com/GongRzhe/Gmail-MCP-Server/tree/a890d19189bbc1325b8728fab830fc278cfd8804> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/GongRzhe/Gmail-MCP-Server/blob/a890d19189bbc1325b8728fab830fc278cfd8804/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: does not meet

Declared MCP library: @modelcontextprotocol/sdk ^0.4.0. Lower-bound version 0.4.0 of @modelcontextprotocol/sdk (npm) was published on 2024-11-11, more than 24 months before 2026-11-14.

Source: <https://registry.npmjs.org/@gongrzhe/server-gmail-autoauth-mcp/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `gmail-mcp-server-gongrzhe`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
