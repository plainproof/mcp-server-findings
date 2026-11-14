# Azure MCP Server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `azure-mcp` |
| Repository | <https://github.com/microsoft/mcp> (`servers/Azure.Mcp.Server`) |
| Package | `npm:@azure/mcp` |
| Publisher | microsoft (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 4.0.0-beta.7 (2026-11-11) |
| Commit read | `d97c4ee2b743` on `main` (2026-11-14) |
| GitHub stars | 3853 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C2, C3, C4, C6, C8, C9, C10; partly meets C1, C5, C7.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The npm record for @azure/mcp@4.0.0-beta.7 names the repository `git+https://github.com/microsoft/mcp.git`. The record carries no provenance attestation (`dist.attestations` is absent).

Source: <https://registry.npmjs.org/@azure/mcp/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/microsoft/mcp/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 4.0.0-beta.7 is dated 2026-11-11; the newest commit on `main` is dated 2026-11-14; GitHub reports the last push on 2026-11-14.

Source: <https://api.github.com/repos/microsoft/mcp>, <https://registry.npmjs.org/@azure/mcp/latest>, <https://github.com/microsoft/mcp/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/microsoft/mcp/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Tools can create, modify and delete resources within the signed-in identity's Azure permissions; the security policy documents options that limit which tools are exposed and calls them operational guardrails, and the README advises least-privilege roles. Quoted: “MCP tools are designed to inspect, create, modify, and delete Azure resources”; “which MCP servers and tools are enabled (for example, via `--namespace`, `--tool`, `--mode`, `--read-only`, and `--disable-proxy-tools`)”; “You should review and apply least-privilege RBAC roles and implement safeguards before deployment.”.

Source: <https://github.com/microsoft/mcp/blob/d97c4ee2b74357c3e4353e30606656c3530fa0c9/SECURITY.md?plain=1#L98>, <https://github.com/microsoft/mcp/blob/d97c4ee2b74357c3e4353e30606656c3530fa0c9/servers/Azure.Mcp.Server/README.md?plain=1#L1593> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

Credentials are handled through the Azure Identity SDK. Quoted: “we never store or manage tokens directly”.

Source: <https://github.com/microsoft/mcp/blob/d97c4ee2b74357c3e4353e30606656c3530fa0c9/servers/Azure.Mcp.Server/README.md?plain=1#L1585> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: partly meets

Telemetry is documented as on by default, with an environment variable to turn it off. Quoted: “Telemetry collection is on by default.”; “set the environment variable `AZURE_MCP_COLLECT_TELEMETRY` to `false`”.

Source: <https://github.com/microsoft/mcp/blob/d97c4ee2b74357c3e4353e30606656c3530fa0c9/servers/Azure.Mcp.Server/README.md?plain=1#L1605> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`Directory.Packages.props` (central package-version file)) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/microsoft/mcp/blob/d97c4ee2b74357c3e4353e30606656c3530fa0c9/Directory.Packages.props>, <https://github.com/microsoft/mcp/blob/d97c4ee2b74357c3e4353e30606656c3530fa0c9/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: meets

The security policy names prompt injection and untrusted input, and states that callers and MCP hosts are responsible for inspecting and sanitising returned data. Quoted: “Reports involving AI-generated tool calls or prompt injection must demonstrate a violation of a security responsibility owned by the MCP server”; “It is the responsibility of callers, users, and MCP hosts to inspect, validate, and sanitize inputs and returned data before using them in ways that may impact their environment.”.

Source: <https://github.com/microsoft/mcp/blob/d97c4ee2b74357c3e4353e30606656c3530fa0c9/SECURITY.md?plain=1#L102> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: ModelContextProtocol 2.2.0 in Directory.Packages.props. Lower-bound version 2.2.0 of ModelContextProtocol (NuGet) was published on 2026-08-13, within the 12 months before 2026-11-14.

Source: <https://github.com/microsoft/mcp/blob/d97c4ee2b74357c3e4353e30606656c3530fa0c9/Directory.Packages.props?plain=1#L105>, <https://api.nuget.org/v3/registration5-gz-semver2/modelcontextprotocol/index.json> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `azure-mcp`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
