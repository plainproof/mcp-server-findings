# Terraform MCP Server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `terraform-mcp-server` |
| Repository | <https://github.com/hashicorp/terraform-mcp-server> |
| Package | `binary:releases.hashicorp.com/terraform-mcp-server; oci:hashicorp/terraform-mcp-server` |
| Publisher | hashicorp (GitHub organisation account) |
| Licence detected by GitHub | MPL-2.0 |
| Upstream status | `active` |
| Latest release | v1.4.1 (2026-10-23) |
| Commit read | `3e38ca694399` on `main` (2026-11-11) |
| GitHub stars | 1562 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C5, C6, C7, C8, C10; partly meets C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The source repository is public. The publisher's release site lists version 1.4.1 with a checksums file and signature files (`terraform-mcp-server_1.4.1_SHA256SUMS.sig`).

Source: <https://releases.hashicorp.com/terraform-mcp-server/1.4.1/>, <https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.4.1> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository, and it describes how to report a vulnerability.

Source: <https://github.com/hashicorp/terraform-mcp-server/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release v1.4.1 is dated 2026-10-23; the newest commit on `main` is dated 2026-11-11; GitHub reports the last push on 2026-11-13.

Source: <https://api.github.com/repos/hashicorp/terraform-mcp-server>, <https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.4.1>, <https://github.com/hashicorp/terraform-mcp-server/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/hashicorp/terraform-mcp-server/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: meets

Tools that require explicit approval are documented as off by default; toolset and tool selection are documented. Quoted: “`ENABLE_TF_OPERATIONS` | Enable tools that require explicit approval | `false` |”.

Source: <https://github.com/hashicorp/terraform-mcp-server/blob/3e38ca6943992c108b7b83c3a06b0c1b6f4902ac/README.md?plain=1#L135> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The API token is supplied through an environment variable. Quoted: “`TFE_TOKEN` | Terraform Enterprise API token”.

Source: <https://github.com/hashicorp/terraform-mcp-server/blob/3e38ca6943992c108b7b83c3a06b0c1b6f4902ac/README.md?plain=1#L108> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README describes OpenTelemetry metrics as a feature the operator enables; no collection by the publisher is described. Quoted: “Integration with open telemetry meters to track tool-call volume, latency and failures in Streamable HTTP mode.”.

Source: <https://github.com/hashicorp/terraform-mcp-server/blob/3e38ca6943992c108b7b83c3a06b0c1b6f4902ac/README.md?plain=1#L87> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`go.sum`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/hashicorp/terraform-mcp-server/blob/3e38ca6943992c108b7b83c3a06b0c1b6f4902ac/go.sum>, <https://github.com/hashicorp/terraform-mcp-server/blob/3e38ca6943992c108b7b83c3a06b0c1b6f4902ac/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: partly meets

The README carries a security note about untrusted clients and models; it does not name prompt injection or untrusted content returned by tools. Quoted: “Do not use the MCP server with untrusted MCP clients or LLMs.”.

Source: <https://github.com/hashicorp/terraform-mcp-server/blob/3e38ca6943992c108b7b83c3a06b0c1b6f4902ac/README.md?plain=1#L90> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: go-sdk v1.8.0 (and mark3labs/mcp-go v0.58.0) in go.mod. Lower-bound version v1.8.0 of github.com/modelcontextprotocol/go-sdk was published on 2026-09-04, within the 12 months before 2026-11-14.

Source: <https://github.com/hashicorp/terraform-mcp-server/blob/3e38ca6943992c108b7b83c3a06b0c1b6f4902ac/go.mod?plain=1#L13>, <https://proxy.golang.org/github.com/modelcontextprotocol/go-sdk/@v/v1.8.0.info> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `terraform-mcp-server`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
