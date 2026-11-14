# GitHub MCP Server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `github-mcp-server` |
| Repository | <https://github.com/github/github-mcp-server> |
| Package | `oci:ghcr.io/github/github-mcp-server; binary:GitHub releases; remote:https://api.githubcopilot.com/mcp/` |
| Publisher | github (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | v2.1.0 (2026-11-03) |
| Commit read | `0663b830582a` on `main` (2026-11-13) |
| GitHub stars | 34455 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C2, C3, C6, C7, C8, C9, C10; partly meets C1, C4, C5.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The source repository is public and release v2.1.0 is published from it. Its assets are platform archives and a checksums file (`github-mcp-server_2.1.0_checksums.txt`); no signature or attestation file is among the release assets, and the README does not describe verifying one (searched for: cosign, sigstore, attestation, provenance).

Source: <https://github.com/github/github-mcp-server/releases/tag/v2.1.0>, <https://github.com/github/github-mcp-server/blob/0663b830582af923e30fb14cb2e10dd3248baa86/README.md> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/github/github-mcp-server/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release v2.1.0 is dated 2026-11-03; the newest commit on `main` is dated 2026-11-13; GitHub reports the last push on 2026-11-13.

Source: <https://api.github.com/repos/github/github-mcp-server>, <https://github.com/github/github-mcp-server/releases/tag/v2.1.0>, <https://github.com/github/github-mcp-server/commits/main> (verified 2026-11-14)

### C4. Published advisories: partly meets

2 advisories are published in the repository's advisory list. GHSA-w4q6-qw23-4rg7 (high, published 2026-07-20) names no patched version; its stated affected range is "<= 0.33.0 (also affects latest main)", which does not clearly include or exclude the latest release (v2.1.0). The other advisory names a patched version below the latest release.

Source: <https://github.com/github/github-mcp-server/security/advisories>, <https://github.com/github/github-mcp-server/security/advisories/GHSA-w4q6-qw23-4rg7> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The README documents an opt-in read-only mode and toolset selection; without the flag, write tools in the enabled toolsets are offered. Quoted: “To run the server in read-only mode, you can use the `--read-only` flag. This will only offer read-only tools, preventing any modifications to repositories, issues, pull requests, etc.”.

Source: <https://github.com/github/github-mcp-server/blob/0663b830582af923e30fb14cb2e10dd3248baa86/README.md?plain=1#L1717> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

Authentication is by OAuth sign-in or a personal access token supplied through an environment variable. Quoted: “use the `github-mcp-server stdio` command with the `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable set to your token”.

Source: <https://github.com/github/github-mcp-server/blob/0663b830582af923e30fb14cb2e10dd3248baa86/README.md?plain=1#L418> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/github/github-mcp-server/blob/0663b830582af923e30fb14cb2e10dd3248baa86/README.md> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`go.sum`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/github/github-mcp-server/blob/0663b830582af923e30fb14cb2e10dd3248baa86/go.sum>, <https://github.com/github/github-mcp-server/blob/0663b830582af923e30fb14cb2e10dd3248baa86/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: meets

The README names prompt injection from untrusted repository content and documents lockdown mode as a filter for it, stating its limits. Quoted: “Lockdown mode is a best-effort content filter intended to reduce the risk of prompt injection from untrusted repository content”.

Source: <https://github.com/github/github-mcp-server/blob/0663b830582af923e30fb14cb2e10dd3248baa86/README.md?plain=1#L1736> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: go-sdk v1.8.0 in go.mod. Lower-bound version v1.8.0 of github.com/modelcontextprotocol/go-sdk was published on 2026-09-04, within the 12 months before 2026-11-14.

Source: <https://github.com/github/github-mcp-server/blob/0663b830582af923e30fb14cb2e10dd3248baa86/go.mod?plain=1#L13>, <https://proxy.golang.org/github.com/modelcontextprotocol/go-sdk/@v/v1.8.0.info> (verified 2026-11-14)

## Advisories published by the project

- GHSA-w4q6-qw23-4rg7 / CVE-2026-47427 (high, published 2026-07-20): Nil Pointer Dereference DoS in completion/complete Handler. Affected: <= 0.33.0 (also affects latest main). Patched: no patched version named. <https://github.com/github/github-mcp-server/security/advisories/GHSA-w4q6-qw23-4rg7>
- GHSA-pjp5-fpmr-3349 / CVE-2026-48529 (medium, published 2026-06-09): Lockdown mode singleton in HTTP server causes cross-user GraphQL client confusion. Affected: >= 0.22.0, < 1.1.2. Patched: 1.1.2. <https://github.com/github/github-mcp-server/security/advisories/GHSA-pjp5-fpmr-3349>

## Reported elsewhere

These items are not part of any result above. Each is reported by the named source and is not confirmed in the project's own material.

- Reported by Invariant Labs, not confirmed in the project's own material: "GitHub MCP Exploited: Accessing private repositories via MCP". <https://invariantlabs.ai/blog/mcp-github-vulnerability> (page read 2026-11-14)

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `github-mcp-server`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
