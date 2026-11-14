# Sentry MCP server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `sentry-mcp` |
| Repository | <https://github.com/getsentry/toolkit>; listed at selection as <https://github.com/getsentry/sentry-mcp> |
| Package | `npm:@sentry/mcp-server; remote:https://mcp.sentry.dev/mcp` |
| Publisher | getsentry (GitHub organisation account) |
| Licence detected by GitHub | NOASSERTION |
| Upstream status | `renamed` - The repository was renamed from getsentry/sentry-mcp to getsentry/toolkit; the old address redirects. The npm package name is unchanged. Quoted: “ships the same server, bundled without the rest of the CLI, for clients that”. |
| Latest release | 0.49.0 (2026-11-07) |
| Commit read | `f8464f814cd3` on `main` (2026-11-14) |
| GitHub stars | 964 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C2, C3, C4, C6, C7, C10; partly meets C1, C5, C8; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The npm record for @sentry/mcp-server@0.49.0 names the repository `git+https://github.com/getsentry/toolkit.git`. The record carries no provenance attestation (`dist.attestations` is absent).

Source: <https://registry.npmjs.org/@sentry/mcp-server/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository, and it describes how to report a vulnerability.

Source: <https://github.com/getsentry/toolkit/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 0.49.0 is dated 2026-11-07; the newest commit on `main` is dated 2026-11-14; GitHub reports the last push on 2026-11-14.

Source: <https://api.github.com/repos/getsentry/toolkit>, <https://registry.npmjs.org/@sentry/mcp-server/latest>, <https://github.com/getsentry/toolkit/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/getsentry/toolkit/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The token scopes listed in the README include write scopes; the README documents limiting calls to one organisation or project and disabling skills. Quoted: “Pass `<org>/` or `<org>/<project>` to limit every call to one organization or”; “You can also disable any other skill to prevent unsupported tools from being”; “project:write”.

Source: <https://github.com/getsentry/toolkit/blob/f8464f814cd3582e9b09abce8452f7e582fce77c/README.md?plain=1#L75> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

Authentication is by a stored login or a token in an environment variable; the README marks the older command-line token flag as deprecated. Quoted: “SENTRY_AUTH_TOKEN=sentry-user-token npx @sentry/mcp-server@latest”; “`--access-token` / `SENTRY_ACCESS_TOKEN` from older releases still work but are”.

Source: <https://github.com/getsentry/toolkit/blob/f8464f814cd3582e9b09abce8452f7e582fce77c/README.md?plain=1#L133> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/getsentry/toolkit/blob/f8464f814cd3582e9b09abce8452f7e582fce77c/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`pnpm-lock.yaml`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/getsentry/toolkit/blob/f8464f814cd3582e9b09abce8452f7e582fce77c/pnpm-lock.yaml>, <https://github.com/getsentry/toolkit/tree/f8464f814cd3582e9b09abce8452f7e582fce77c> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/getsentry/toolkit/blob/f8464f814cd3582e9b09abce8452f7e582fce77c/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/server 2.4.0 (and @modelcontextprotocol/sdk 1.32.2) in the pnpm workspace catalog. Lower-bound version 2.4.0 of @modelcontextprotocol/server (npm) was published on 2026-10-23, within the 12 months before 2026-11-14.

Source: <https://github.com/getsentry/toolkit/blob/f8464f814cd3582e9b09abce8452f7e582fce77c/pnpm-workspace.yaml?plain=1#L51>, <https://registry.npmjs.org/@modelcontextprotocol/server> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `sentry-mcp`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
