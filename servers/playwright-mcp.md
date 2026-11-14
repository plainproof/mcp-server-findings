# Playwright MCP (Microsoft)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `playwright-mcp` |
| Repository | <https://github.com/microsoft/playwright-mcp> |
| Package | `npm:@playwright/mcp` |
| Publisher | microsoft (GitHub organisation account) |
| Licence detected by GitHub | Apache-2.0 |
| Upstream status | `active` |
| Latest release | 0.0.85 (2026-11-09) |
| Commit read | `78eca85361ef` on `main` (2026-11-11) |
| GitHub stars | 39634 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C8, C10; partly meets C5, C7, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for @playwright/mcp@0.0.85 names the repository `git+https://github.com/microsoft/playwright-mcp.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/@playwright/mcp/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/microsoft/playwright-mcp/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 0.0.85 is dated 2026-11-09; the newest commit on `main` is dated 2026-11-11; GitHub reports the last push on 2026-11-13.

Source: <https://api.github.com/repos/microsoft/playwright-mcp>, <https://registry.npmjs.org/@playwright/mcp/latest>, <https://github.com/microsoft/playwright-mcp/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/microsoft/playwright-mcp/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Browser automation is the core function; the README documents file-access restriction by default, origin allow and block lists, and capabilities that must be switched on, and says the origin lists are not a security boundary. Quoted: “By default access to file system is restricted to workspace root directories (or cwd if no roots are configured) only, and navigation to file:// URLs is blocked.”.

Source: <https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/README.md?plain=1#L411> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The documented setup takes no credential; a secrets file option is documented. Quoted: “path to a file containing secrets in the dotenv format”.

Source: <https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/README.md?plain=1#L451> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: partly meets

The documented function is driving a browser to arbitrary pages. The README contains no reference to telemetry. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog. Quoted: “semicolon-separated list of TRUSTED origins to allow the browser to request. Default is to allow all.”.

Source: <https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/README.md?plain=1#L410>, <https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/README.md> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`package-lock.json`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/package-lock.json>, <https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: partly meets

The README carries a general security statement and a link to MCP security guidance; it does not name prompt injection or untrusted content. Quoted: “Playwright MCP is **not** a security boundary.”.

Source: <https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/README.md?plain=1#L861> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/sdk ^1.25.2 in the repository's package.json. Lower-bound version 1.25.2 of @modelcontextprotocol/sdk (npm) was published on 2026-01-07, within the 12 months before 2026-11-14.

Source: <https://github.com/microsoft/playwright-mcp/blob/78eca85361efb545a4c0f59b6140aef0721c5412/package.json?plain=1#L44>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `playwright-mcp`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
