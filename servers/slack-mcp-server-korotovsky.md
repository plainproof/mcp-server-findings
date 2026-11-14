# Slack MCP Server (korotovsky)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `slack-mcp-server-korotovsky` |
| Repository | <https://github.com/korotovsky/slack-mcp-server> |
| Package | `npm:slack-mcp-server; binary:GitHub releases` |
| Publisher | korotovsky (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 1.3.0 (2026-05-14) |
| Commit read | `b88c0de3f706` on `master` (2026-05-14) |
| GitHub stars | 1898 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C2, C4, C5, C6, C7, C8, C10; partly meets C1, C3; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The npm record for slack-mcp-server@1.3.0 names the repository `git+https://github.com/korotovsky/slack-mcp-server.git`. The record carries no provenance attestation (`dist.attestations` is absent).

Source: <https://registry.npmjs.org/slack-mcp-server/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/korotovsky/slack-mcp-server/security/policy> (verified 2026-11-14)

### C3. Maintenance status: partly meets

The repository is not archived. The latest release is 184 days old (more than 180); repository activity falls within the last 180 days. Latest release 1.3.0 is dated 2026-05-14; the newest commit on `master` is dated 2026-05-14; GitHub reports the last push on 2026-07-16.

Source: <https://api.github.com/repos/korotovsky/slack-mcp-server>, <https://registry.npmjs.org/slack-mcp-server/latest>, <https://github.com/korotovsky/slack-mcp-server/commits/master> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/korotovsky/slack-mcp-server/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: meets

The README documents the message-posting tool as disabled by default. Quoted: “The `conversations_add_message` tool is disabled by default for safety.”.

Source: <https://github.com/korotovsky/slack-mcp-server/blob/b88c0de3f706f4f07337c9eda7133c736d1c9524/README.md?plain=1#L18> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

Tokens are supplied through environment variables. The README documents two token types: Slack browser session tokens and OAuth tokens. Quoted: “`SLACK_MCP_XOXC_TOKEN` | Yes* | `nil` | Slack browser token (`xoxc-...`) |”; “`SLACK_MCP_XOXP_TOKEN` | Yes* | `nil` | User OAuth token (`xoxp-...`) — alternative to xoxc/xoxd |”.

Source: <https://github.com/korotovsky/slack-mcp-server/blob/b88c0de3f706f4f07337c9eda7133c736d1c9524/README.md?plain=1#L277> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/korotovsky/slack-mcp-server/blob/b88c0de3f706f4f07337c9eda7133c736d1c9524/README.md> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`go.sum`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/korotovsky/slack-mcp-server/blob/b88c0de3f706f4f07337c9eda7133c736d1c9524/go.sum>, <https://github.com/korotovsky/slack-mcp-server/blob/b88c0de3f706f4f07337c9eda7133c736d1c9524/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial; `SECURITY.md` for: prompt-injection, untrusted.

Source: <https://github.com/korotovsky/slack-mcp-server/blob/b88c0de3f706f4f07337c9eda7133c736d1c9524/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: mcp-go v0.44.0 in go.mod. Lower-bound version v0.44.0 of github.com/mark3labs/mcp-go was published on 2026-02-15, within the 12 months before 2026-11-14.

Source: <https://github.com/korotovsky/slack-mcp-server/blob/b88c0de3f706f4f07337c9eda7133c736d1c9524/go.mod?plain=1#L8>, <https://proxy.golang.org/github.com/mark3labs/mcp-go/@v/v0.44.0.info> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `slack-mcp-server-korotovsky`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
