# Context7 MCP

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `context7` |
| Repository | <https://github.com/upstash/context7> |
| Package | `npm:@upstash/context7-mcp; remote:https://mcp.context7.com/mcp` |
| Publisher | upstash (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 4.7.0 (2026-11-12) |
| Commit read | `5c4a4b43cd50` on `master` (2026-11-13) |
| GitHub stars | 64792 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C2, C3, C4, C5, C6, C7, C8, C10; partly meets C1; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The npm record for @upstash/context7-mcp@4.7.0 names the repository `git+https://github.com/upstash/context7.git`. The record carries no provenance attestation (`dist.attestations` is absent).

Source: <https://registry.npmjs.org/@upstash/context7-mcp/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/upstash/context7/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 4.7.0 is dated 2026-11-12; the newest commit on `master` is dated 2026-11-13; GitHub reports the last push on 2026-11-13.

Source: <https://api.github.com/repos/upstash/context7>, <https://registry.npmjs.org/@upstash/context7-mcp/latest>, <https://github.com/upstash/context7/commits/master> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/upstash/context7/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: meets

The two documented tools look up library documentation; no write or execute tool is documented. Quoted: “`query-docs`: Retrieves documentation for a library using a Context7-compatible library ID.”.

Source: <https://github.com/upstash/context7/blob/5c4a4b43cd5010f5678c6fceac3dd16865112e67/README.md?plain=1#L111> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The API key is passed in an Authorization header set in the client configuration, or obtained through an OAuth setup command. Quoted: “pass your API key via the `Authorization: Bearer YOUR_API_KEY` header”.

Source: <https://github.com/upstash/context7/blob/5c4a4b43cd5010f5678c6fceac3dd16865112e67/README.md?plain=1#L59> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/upstash/context7/blob/5c4a4b43cd5010f5678c6fceac3dd16865112e67/README.md> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`pnpm-lock.yaml`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/upstash/context7/blob/5c4a4b43cd5010f5678c6fceac3dd16865112e67/pnpm-lock.yaml>, <https://github.com/upstash/context7/blob/5c4a4b43cd5010f5678c6fceac3dd16865112e67/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial; `SECURITY.md` for: prompt-injection, untrusted.

Source: <https://github.com/upstash/context7/blob/5c4a4b43cd5010f5678c6fceac3dd16865112e67/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/server 2.3.1. Lower-bound version 2.3.1 of @modelcontextprotocol/server (npm) was published on 2026-10-05, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/@upstash/context7-mcp/latest>, <https://registry.npmjs.org/@modelcontextprotocol/server> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `context7`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
