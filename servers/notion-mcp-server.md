# Notion MCP Server (self-hosted)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `notion-mcp-server` |
| Repository | <https://github.com/makenotion/notion-mcp-server> |
| Package | `npm:@notionhq/notion-mcp-server` |
| Publisher | makenotion (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `unmaintained-per-publisher` - The README says this self-hosted server is no longer actively maintained or supported and points to the publisher's hosted server. The latest release (2.6.1) is dated 2026-10-29. |
| Latest release | 2.6.1 (2026-10-29) |
| Commit read | `cf16e5c20bfb` on `main` (2026-10-29) |
| GitHub stars | 4707 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-not-met` |

## Outcome

As of 2026-11-14: meets C1, C4, C6, C7, C10; partly meets C5, C8, C9; does not meet C2, C3.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for @notionhq/notion-mcp-server@2.6.1 names the repository `git+ssh://git@github.com/makenotion/notion-mcp-server.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/@notionhq/notion-mcp-server/latest> (verified 2026-11-14)

### C2. Published security policy: does not meet

GitHub's security-policy page for the repository says "No security policy detected" and offers no private vulnerability reporting; the README names no channel for security reports (searched for: security@, vulnerability, responsible disclosure, report security).

Source: <https://github.com/makenotion/notion-mcp-server/security/policy>, <https://github.com/makenotion/notion-mcp-server/blob/cf16e5c20bfbfb98ecec1227f210ef0ae3abebe5/README.md> (verified 2026-11-14)

### C3. Maintenance status: does not meet

The repository is not archived, but the README says the project is no longer maintained or supported. Quoted: “server implementation that is no longer actively maintained or supported.”. Latest release 2.6.1 is dated 2026-10-29; the newest commit on `main` is dated 2026-10-29; GitHub reports the last push on 2026-10-29.

Source: <https://github.com/makenotion/notion-mcp-server/blob/cf16e5c20bfbfb98ecec1227f210ef0ae3abebe5/README.md?plain=1#L7>, <https://api.github.com/repos/makenotion/notion-mcp-server>, <https://registry.npmjs.org/@notionhq/notion-mcp-server/latest> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/makenotion/notion-mcp-server/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The exposed tools include writes; the README documents restricting them through the capabilities of the integration token. Quoted: “For example, you can create a read-only integration token by giving only "Read content" access from the "Configuration" tab:”.

Source: <https://github.com/makenotion/notion-mcp-server/blob/cf16e5c20bfbfb98ecec1227f210ef0ae3abebe5/README.md?plain=1#L112> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The integration token is supplied through an environment variable. Quoted: “"NOTION_TOKEN": "ntn_****"”.

Source: <https://github.com/makenotion/notion-mcp-server/blob/cf16e5c20bfbfb98ecec1227f210ef0ae3abebe5/README.md?plain=1#L147> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/makenotion/notion-mcp-server/blob/cf16e5c20bfbfb98ecec1227f210ef0ae3abebe5/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/makenotion/notion-mcp-server/blob/cf16e5c20bfbfb98ecec1227f210ef0ae3abebe5/package-lock.json>, <https://github.com/makenotion/notion-mcp-server/tree/cf16e5c20bfbfb98ecec1227f210ef0ae3abebe5> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: partly meets

The README carries a general caution about exposing workspace data to language models; it does not name prompt injection or untrusted content. Quoted: “there is a non-zero risk to workspace data by exposing it to LLMs”.

Source: <https://github.com/makenotion/notion-mcp-server/blob/cf16e5c20bfbfb98ecec1227f210ef0ae3abebe5/README.md?plain=1#L110> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/sdk ^1.32.2. Lower-bound version 1.32.2 of @modelcontextprotocol/sdk (npm) was published on 2026-10-23, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/@notionhq/notion-mcp-server/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `notion-mcp-server`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
