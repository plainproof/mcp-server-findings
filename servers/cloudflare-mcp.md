# Cloudflare MCP servers

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `cloudflare-mcp` |
| Repository | <https://github.com/cloudflare/mcp-server-cloudflare> |
| Package | `remote:https://*.mcp.cloudflare.com/mcp` |
| Publisher | cloudflare (GitHub organisation account) |
| Licence detected by GitHub | Apache-2.0 |
| Upstream status | `active` |
| Latest release | workers-observability@0.6.0 (2026-10-22) |
| Commit read | `a21972e21928` on `main` (2026-10-22) |
| GitHub stars | 4465 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C2, C3, C4, C6, C7, C10; partly meets C1, C5, C8; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The source repository is public. The servers are offered as hosted endpoints listed in the README, so there is no released artefact to attest.

Source: <https://github.com/cloudflare/mcp-server-cloudflare>, <https://github.com/cloudflare/mcp-server-cloudflare/blob/a21972e219289337731a066befb5c66886b9ce7b/README.md> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository, and it describes how to report a vulnerability.

Source: <https://github.com/cloudflare/mcp-server-cloudflare/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release workers-observability@0.6.0 is dated 2026-10-22; the newest commit on `main` is dated 2026-10-22; GitHub reports the last push on 2026-10-22.

Source: <https://api.github.com/repos/cloudflare/mcp-server-cloudflare>, <https://github.com/cloudflare/mcp-server-cloudflare/releases/tag/workers-observability@0.6.0>, <https://github.com/cloudflare/mcp-server-cloudflare/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/cloudflare/mcp-server-cloudflare/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Hosted servers, one endpoint per product area; the README describes access as governed by the permissions of the API token. No read-only mode is described in the README. Quoted: “you will need to provide the Responses API with an API token that has the scopes (permissions) required for that particular MCP server”.

Source: <https://github.com/cloudflare/mcp-server-cloudflare/blob/a21972e219289337731a066befb5c66886b9ce7b/README.md?plain=1#L73> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The README documents an API token created in the Cloudflare dashboard with the permissions each server needs, and refers to OAuth. Quoted: “create an API token in the Cloudflare dashboard”; “OAuth, credentials, account selection, application caches, and product Durable Objects remain application/security state where required.”.

Source: <https://github.com/cloudflare/mcp-server-cloudflare/blob/a21972e219289337731a066befb5c66886b9ce7b/README.md?plain=1#L75> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/cloudflare/mcp-server-cloudflare/blob/a21972e219289337731a066befb5c66886b9ce7b/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`pnpm-lock.yaml`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/cloudflare/mcp-server-cloudflare/blob/a21972e219289337731a066befb5c66886b9ce7b/pnpm-lock.yaml>, <https://github.com/cloudflare/mcp-server-cloudflare/tree/a21972e219289337731a066befb5c66886b9ce7b> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/cloudflare/mcp-server-cloudflare/blob/a21972e219289337731a066befb5c66886b9ce7b/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/server 2.0.0 in the pnpm workspace catalog. Lower-bound version 2.0.0 of @modelcontextprotocol/server (npm) was published on 2026-07-27, within the 12 months before 2026-11-14.

Source: <https://github.com/cloudflare/mcp-server-cloudflare/blob/a21972e219289337731a066befb5c66886b9ce7b/pnpm-workspace.yaml?plain=1#L10>, <https://registry.npmjs.org/@modelcontextprotocol/server> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `cloudflare-mcp`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
