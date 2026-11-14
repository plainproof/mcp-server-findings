# Playwright MCP Server (ExecuteAutomation)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `executeautomation-mcp-playwright` |
| Repository | <https://github.com/executeautomation/mcp-playwright> |
| Package | `npm:@executeautomation/playwright-mcp-server` |
| Publisher | executeautomation (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `inactive` - No release and no repository activity in the 180 days before 2026-11-14. |
| Latest release | 1.0.12 (2025-12-12) |
| Commit read | `2349c2891e7c` on `main` (2025-12-13) |
| GitHub stars | 5680 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-not-met` |

## Outcome

As of 2026-11-14: meets C4, C6, C10; partly meets C1, C7, C8; does not meet C2, C3, C5, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The npm record for @executeautomation/playwright-mcp-server@1.0.12 names the repository `git+https://github.com/executeautomation/mcp-playwright.git`. The record carries no provenance attestation (`dist.attestations` is absent).

Source: <https://registry.npmjs.org/@executeautomation/playwright-mcp-server/latest> (verified 2026-11-14)

### C2. Published security policy: does not meet

GitHub's security-policy page for the repository says "No security policy detected" and offers no private vulnerability reporting; the README names no channel for security reports (searched for: security@, vulnerability, responsible disclosure, report security).

Source: <https://github.com/executeautomation/mcp-playwright/security/policy>, <https://github.com/executeautomation/mcp-playwright/blob/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da/README.md> (verified 2026-11-14)

### C3. Maintenance status: does not meet

The repository is not archived, but there has been neither a release nor repository activity in the 180 days before 2026-11-14. Latest release 1.0.12 is dated 2025-12-12; the newest commit on `main` is dated 2025-12-13; GitHub reports the last push on 2025-12-13.

Source: <https://api.github.com/repos/executeautomation/mcp-playwright>, <https://registry.npmjs.org/@executeautomation/playwright-mcp-server/latest>, <https://github.com/executeautomation/mcp-playwright/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/executeautomation/mcp-playwright/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: does not meet

The README describes browser automation including JavaScript execution; no option to restrict navigation, script execution or tools was found in the README. Searched `README.md` for: read-only, allowlist, allowed-(origins, hosts, domains), restrict, disable (tool, script). Quoted: “This server enables LLMs to interact with web pages, take screenshots, generate test code, web scrapes the page and execute JavaScript in a real browser environment.”.

Source: <https://github.com/executeautomation/mcp-playwright/blob/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da/README.md?plain=1#L22>, <https://github.com/executeautomation/mcp-playwright/blob/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da/README.md> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The documented server setup takes no credential. Quoted: “claude mcp add --transport stdio playwright npx @executeautomation/playwright-mcp-server”.

Source: <https://github.com/executeautomation/mcp-playwright/blob/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da/README.md?plain=1#L80> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: partly meets

The documented function is driving a browser to arbitrary web pages. The README contains no reference to telemetry. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog. Quoted: “This server enables LLMs to interact with web pages”.

Source: <https://github.com/executeautomation/mcp-playwright/blob/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da/README.md?plain=1#L22>, <https://github.com/executeautomation/mcp-playwright/blob/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/executeautomation/mcp-playwright/blob/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da/package-lock.json>, <https://github.com/executeautomation/mcp-playwright/tree/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/executeautomation/mcp-playwright/blob/2349c2891e7c499c8c07b7d78c7f3fb4c797a1da/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/sdk 1.24.3. Lower-bound version 1.24.3 of @modelcontextprotocol/sdk (npm) was published on 2025-12-04, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/@executeautomation/playwright-mcp-server/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `executeautomation-mcp-playwright`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
