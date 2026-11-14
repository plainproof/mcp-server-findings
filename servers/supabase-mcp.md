# Supabase MCP Server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `supabase-mcp` |
| Repository | <https://github.com/supabase/mcp>; listed at selection as <https://github.com/supabase-community/supabase-mcp> |
| Package | `npm:@supabase/mcp-server-supabase; remote:https://mcp.supabase.com/mcp` |
| Publisher | supabase (GitHub organisation account) |
| Licence detected by GitHub | Apache-2.0 |
| Upstream status | `transferred` - The repository moved from supabase-community/supabase-mcp to supabase/mcp; the old address redirects. The npm package name is unchanged. |
| Latest release | 0.17.0 (2026-11-13) |
| Commit read | `9092ab905550` on `main` (2026-11-13) |
| GitHub stars | 3010 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C7, C8, C9, C10; partly meets C5.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for @supabase/mcp-server-supabase@0.17.0 names the repository `git+https://github.com/supabase/mcp.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/@supabase/mcp-server-supabase/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/supabase/mcp/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 0.17.0 is dated 2026-11-13; the newest commit on `main` is dated 2026-11-13; GitHub reports the last push on 2026-11-14.

Source: <https://api.github.com/repos/supabase/mcp>, <https://registry.npmjs.org/@supabase/mcp-server-supabase/latest>, <https://github.com/supabase/mcp/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/supabase/mcp/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The publisher's documentation describes project scoping, a read-only mode and feature-group selection as options to set. Quoted: “Use project scoping, read-only mode, restricted feature groups, and the narrowest data query that can answer the question.”.

Source: <https://supabase.com/docs/guides/ai-tools/mcp> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The hosted server is reached through a Supabase sign-in prompted by the MCP client; no token is placed in the documented configuration. Quoted: “Your MCP client will automatically prompt you to log in to Supabase during setup.”.

Source: <https://github.com/supabase/mcp/blob/9092ab9055509fcdfbedcb75edf02d9412feed37/README.md?plain=1#L22> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/supabase/mcp/blob/9092ab9055509fcdfbedcb75edf02d9412feed37/README.md> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`pnpm-lock.yaml`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/supabase/mcp/blob/9092ab9055509fcdfbedcb75edf02d9412feed37/pnpm-lock.yaml>, <https://github.com/supabase/mcp/blob/9092ab9055509fcdfbedcb75edf02d9412feed37/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: meets

The README points to the publisher's security guidance, which names prompt injection and gives recommendations. Quoted: “we recommend you read our [security best practices](https://supabase.com/docs/guides/ai-tools/mcp#security-risks)”; “The primary attack vector unique to LLMs is prompt injection”.

Source: <https://github.com/supabase/mcp/blob/9092ab9055509fcdfbedcb75edf02d9412feed37/README.md?plain=1#L15>, <https://supabase.com/docs/guides/ai-tools/mcp> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/node ^2.0.0. Lower-bound version 2.0.0 of @modelcontextprotocol/node (npm) was published on 2026-07-27, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/@supabase/mcp-server-supabase/latest>, <https://registry.npmjs.org/@modelcontextprotocol/node> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `supabase-mcp`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
