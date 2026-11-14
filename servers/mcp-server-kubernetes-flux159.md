# MCP Server Kubernetes (Flux159)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-server-kubernetes-flux159` |
| Repository | <https://github.com/Flux159/mcp-server-kubernetes> |
| Package | `npm:mcp-server-kubernetes` |
| Publisher | Flux159 (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 4.2.3 (2026-11-13) |
| Commit read | `28fa39e2a633` on `main` (2026-11-13) |
| GitHub stars | 1612 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C7, C10; partly meets C5, C8; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for mcp-server-kubernetes@4.2.3 names the repository `git+https://github.com/Flux159/mcp-server-kubernetes.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/mcp-server-kubernetes/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/Flux159/mcp-server-kubernetes/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 4.2.3 is dated 2026-11-13; the newest commit on `main` is dated 2026-11-13; GitHub reports the last push on 2026-11-13.

Source: <https://api.github.com/repos/Flux159/mcp-server-kubernetes>, <https://registry.npmjs.org/mcp-server-kubernetes/latest>, <https://github.com/Flux159/mcp-server-kubernetes/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

11 advisories are published in the repository's advisory list; each names a patched version at or below the latest release (4.2.3). Most recent: GHSA-6963-p4fp-2wxw (high, published 2026-10-02, patched in >= 4.1.1).

Source: <https://github.com/Flux159/mcp-server-kubernetes/security/advisories>, <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-6963-p4fp-2wxw> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Destructive operations are available unless non-destructive mode is set. Quoted: “You can run the server in a non-destructive mode that disables all destructive operations (delete pods, delete deployments, delete namespaces, etc.):”.

Source: <https://github.com/Flux159/mcp-server-kubernetes/blob/28fa39e2a63332c6c12d78a2ca5209f56519ffaf/README.md?plain=1#L351> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The server uses the local kubeconfig. Quoted: “By default, the server loads kubeconfig from `~/.kube/config`.”.

Source: <https://github.com/Flux159/mcp-server-kubernetes/blob/28fa39e2a63332c6c12d78a2ca5209f56519ffaf/README.md?plain=1#L33> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

OpenTelemetry integration is documented as off by default. Quoted: “This feature is disabled by default and can be enabled via environment variables or Helm configuration.”.

Source: <https://github.com/Flux159/mcp-server-kubernetes/blob/28fa39e2a63332c6c12d78a2ca5209f56519ffaf/README.md?plain=1#L219> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`bun.lockb`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/Flux159/mcp-server-kubernetes/blob/28fa39e2a63332c6c12d78a2ca5209f56519ffaf/bun.lockb>, <https://github.com/Flux159/mcp-server-kubernetes/tree/28fa39e2a63332c6c12d78a2ca5209f56519ffaf> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial; `SECURITY.md` for: prompt-injection, untrusted.

Source: <https://github.com/Flux159/mcp-server-kubernetes/blob/28fa39e2a63332c6c12d78a2ca5209f56519ffaf/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/sdk 1.32.0. Lower-bound version 1.32.0 of @modelcontextprotocol/sdk (npm) was published on 2026-10-02, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/mcp-server-kubernetes/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

- GHSA-6963-p4fp-2wxw / CVE-2026-104776 (high, published 2026-10-02): kubectl_patch is missing the remote-transport path guard applied to every sibling tool, allowing server-side arbitrary file read via patchFile. Affected: <= 4.1.0. Patched: >= 4.1.1. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-6963-p4fp-2wxw>
- GHSA-9j3p-gvw3-h8r8 / CVE-2026-102735 (high, published 2026-09-29): Missing DNS Rebinding Protection in SSE Transport Leads to Unauthenticated Remote Cluster Compromise. Affected: >=0.4.0. Patched: >= 4.0.8. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-9j3p-gvw3-h8r8>
- GHSA-c257-86m4-m579 / CVE-2026-85986 (medium, published 2026-09-04): Incomplete fix of GHSA-6mx4-4h42-r8vh: kubectl/helm dangerous-flag guard is bypassed by the attached short-flag form -sURL, re-enabling API-server redirect and operator bearer-token exfiltration. Affected: <= 3.9.0. Patched: >= 4.0.6. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-c257-86m4-m579>
- GHSA-cmgv-rr9q-f7gw / CVE-2026-85753 (medium, published 2026-09-04): Security Advisory: Arbitrary File Read via Unvalidated valuesFile Path. Affected: <= 3.8.0. Patched: >= 4.0.5. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-cmgv-rr9q-f7gw>
- GHSA-x4x5-wv5h-jjf8 / CVE-2026-77441 (high, published 2026-08-28): Arbitrary Local File Read via `kubectl_create` `--from-file`. Affected: <= 3.9.1. Patched: >= 4.0.2. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-x4x5-wv5h-jjf8>
- GHSA-jjrr-53h8-h34w / CVE-2026-75603 (high, published 2026-08-28): Bare-positional flag injection in 14 kubectl/helm tools enables bearer token exfiltration. Affected: <= 3.8.0. Patched: >= 3.9.0. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-jjrr-53h8-h34w>
- GHSA-6mx4-4h42-r8vh / CVE-2026-47250 (medium, published 2026-05-22): kubectl-generic flag injection enables Kubernetes bearer token exfiltration. Affected: ≤ 3.6.2 (all versions). Patched: >= 3.7.0. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-6mx4-4h42-r8vh>
- GHSA-cr22-wjx7-2w6m / CVE-2026-46519 (high, published 2026-05-17): Tool Access Control Bypass: Presentation-Layer Filtering Without Execution-Layer Enforcement. Affected: < 3.6.0. Patched: >= 3.6.0. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-cr22-wjx7-2w6m>
- GHSA-4xqg-gf5c-ghwq / CVE-2026-39884 (high, published 2026-04-14): Argument Injection in port_forward tool via space-splitting. Affected: <= 3.4.0. Patched: >= 3.5.0. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-4xqg-gf5c-ghwq>
- GHSA-wvxp-jp4w-w8wg / CVE-2025-66404 (high, published 2025-12-03): mcp-server-kubernetes potential security issue in exec_in_pod tool. Affected: <= v2.9.7. Patched: >= v2.9.8. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-wvxp-jp4w-w8wg>
- GHSA-gjv4-ghm7-q58q / CVE-2025-53355 (high, published 2025-07-08): mcp-server-kubernetes vulnerable to command injection in several tools. Affected: <=2.4.9; <=v2.4.9. Patched: >=2.5.0, >=v2.5.0. <https://github.com/Flux159/mcp-server-kubernetes/security/advisories/GHSA-gjv4-ghm7-q58q>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-server-kubernetes-flux159`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
