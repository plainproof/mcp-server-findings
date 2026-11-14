# Kubernetes MCP Server (containers)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `kubernetes-mcp-server-containers` |
| Repository | <https://github.com/containers/kubernetes-mcp-server> |
| Package | `npm:kubernetes-mcp-server; pypi:kubernetes-mcp-server; binary:GitHub releases` |
| Publisher | containers (GitHub organisation account) |
| Licence detected by GitHub | Apache-2.0 |
| Upstream status | `active` |
| Latest release | 0.1.3 (2026-11-13) |
| Commit read | `1d045c6319da` on `main` (2026-11-13) |
| GitHub stars | 2249 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C7, C8, C10; partly meets C5, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for kubernetes-mcp-server@0.1.3 names the repository `git+https://github.com/containers/kubernetes-mcp-server.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/kubernetes-mcp-server/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/containers/kubernetes-mcp-server/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 0.1.3 is dated 2026-11-13; the newest commit on `main` is dated 2026-11-13; GitHub reports the last push on 2026-11-13.

Source: <https://api.github.com/repos/containers/kubernetes-mcp-server>, <https://registry.npmjs.org/kubernetes-mcp-server/latest>, <https://github.com/containers/kubernetes-mcp-server/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

1 advisory is published in the repository's advisory list; it names a patched version at or below the latest release (0.1.3). Most recent: GHSA-xq9m-mrj7-jv98 (medium, published 2026-11-04, patched in 0.1.2).

Source: <https://github.com/containers/kubernetes-mcp-server/security/advisories>, <https://github.com/containers/kubernetes-mcp-server/security/advisories/GHSA-xq9m-mrj7-jv98> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The README documents `read_only` and `denied_resources` settings to be set by the operator, and describes them as best-effort. Quoted: “`read_only` and `denied_resources` are best-effort guardrails. Kubernetes RBAC on the identity this server authenticates as is the access control to rely on.”.

Source: <https://github.com/containers/kubernetes-mcp-server/blob/1d045c6319da3d437842e8a9a2fb846b46d4c420/README.md?plain=1#L226> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The server uses the local kubeconfig or in-cluster configuration; OAuth/OIDC is documented for HTTP mode. Quoted: “or in-cluster configuration.”; “OAuth/OIDC authentication for HTTP mode”.

Source: <https://github.com/containers/kubernetes-mcp-server/blob/1d045c6319da3d437842e8a9a2fb846b46d4c420/README.md?plain=1#L19> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README describes OpenTelemetry tracing and metrics as optional; no collection by the publisher is described. Quoted: “Optional OpenTelemetry distributed tracing and metrics with custom sampling rates.”.

Source: <https://github.com/containers/kubernetes-mcp-server/blob/1d045c6319da3d437842e8a9a2fb846b46d4c420/README.md?plain=1#L42> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`go.sum`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/containers/kubernetes-mcp-server/blob/1d045c6319da3d437842e8a9a2fb846b46d4c420/go.sum>, <https://github.com/containers/kubernetes-mcp-server/blob/1d045c6319da3d437842e8a9a2fb846b46d4c420/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: partly meets

One tool description in the README marks the data it returns as untrusted; no control or recommendation for untrusted content is described. Quoted: “Returned status, events, and logs are untrusted workload data and may contain sensitive values or instructions.”.

Source: <https://github.com/containers/kubernetes-mcp-server/blob/1d045c6319da3d437842e8a9a2fb846b46d4c420/README.md?plain=1#L1175> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: go-sdk v1.8.0 in go.mod. Lower-bound version v1.8.0 of github.com/modelcontextprotocol/go-sdk was published on 2026-09-04, within the 12 months before 2026-11-14.

Source: <https://github.com/containers/kubernetes-mcp-server/blob/1d045c6319da3d437842e8a9a2fb846b46d4c420/go.mod?plain=1#L17>, <https://proxy.golang.org/github.com/modelcontextprotocol/go-sdk/@v/v1.8.0.info> (verified 2026-11-14)

## Advisories published by the project

- GHSA-xq9m-mrj7-jv98 (medium, published 2026-11-04): Kiali Toolset Status Probes can leak Bearer Token. Affected: >= 0.1.0, <= 0.1.1. Patched: 0.1.2. <https://github.com/containers/kubernetes-mcp-server/security/advisories/GHSA-xq9m-mrj7-jv98>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `kubernetes-mcp-server-containers`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
