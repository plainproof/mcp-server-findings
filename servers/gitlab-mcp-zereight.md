# GitLab MCP (zereight)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `gitlab-mcp-zereight` |
| Repository | <https://github.com/zereight/gitlab-mcp> |
| Package | `npm:@zereight/mcp-gitlab` |
| Publisher | zereight (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 2.3.27 (2026-11-13) |
| Commit read | `fdd70b75a164` on `main` (2026-11-14) |
| GitHub stars | 2105 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C7, C8, C9, C10; partly meets C5.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for @zereight/mcp-gitlab@2.3.27 names the repository `git+https://github.com/zereight/gitlab-mcp.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/@zereight/mcp-gitlab/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/zereight/gitlab-mcp/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 2.3.27 is dated 2026-11-13; the newest commit on `main` is dated 2026-11-14; GitHub reports the last push on 2026-11-14.

Source: <https://api.github.com/repos/zereight/gitlab-mcp>, <https://registry.npmjs.org/@zereight/mcp-gitlab/latest>, <https://github.com/zereight/gitlab-mcp/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

31 advisories are published in the repository's advisory list; each names a patched version at or below the latest release (2.3.27). Most recent: GHSA-mfp5-5gv8-2ph2 (high, published 2026-11-13, patched in 2.3.27).

Source: <https://github.com/zereight/gitlab-mcp/security/advisories>, <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-mfp5-5gv8-2ph2> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The README documents permission modes; the default is `full`. Quoted: “`--permission-mode` - Permission level: `readonly`, `modify` (no delete or teardown tools), or `full` (replaces `GITLAB_PERMISSION_MODE`, default `full`)”.

Source: <https://github.com/zereight/gitlab-mcp/blob/fdd70b75a1641034f496729b00e6ff8b0f0681b2/README.md?plain=1#L299> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The token is supplied through an environment variable, or OAuth. Quoted: “read -rs GITLAB_PERSONAL_ACCESS_TOKEN && export GITLAB_PERSONAL_ACCESS_TOKEN”.

Source: <https://github.com/zereight/gitlab-mcp/blob/fdd70b75a1641034f496729b00e6ff8b0f0681b2/README.md?plain=1#L51> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README describes an opt-in local audit log; no usage collection by the publisher is described. Quoted: “Opt-in NDJSON audit log of MCP tool calls for SIEM ingestion”.

Source: <https://github.com/zereight/gitlab-mcp/blob/fdd70b75a1641034f496729b00e6ff8b0f0681b2/README.md?plain=1#L315> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`package-lock.json`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/zereight/gitlab-mcp/blob/fdd70b75a1641034f496729b00e6ff8b0f0681b2/package-lock.json>, <https://github.com/zereight/gitlab-mcp/blob/fdd70b75a1641034f496729b00e6ff8b0f0681b2/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: meets

The README names prompt injection as a risk for the raw API tool and documents that the tool is only enabled explicitly. Quoted: “Prompt injection can drive it. Enable it only by listing `api` in `GITLAB_TOOLSETS`.”.

Source: <https://github.com/zereight/gitlab-mcp/blob/fdd70b75a1641034f496729b00e6ff8b0f0681b2/README.md?plain=1#L135> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/sdk ^1.29.0. Lower-bound version 1.29.0 of @modelcontextprotocol/sdk (npm) was published on 2026-03-30, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/@zereight/mcp-gitlab/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

- GHSA-mfp5-5gv8-2ph2 (high, published 2026-11-13): Command injection in @zereight/mcp-gitlab CLI replay command. Affected: >= 2.1.69, <= 2.3.26. Patched: 2.3.27. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-mfp5-5gv8-2ph2>
- GHSA-wgqr-h4c5-gw82 (medium, published 2026-11-13): ReDoS in @zereight/mcp-gitlab diff filtering can block the entire server. Affected: >= 1.0.60, <= 2.3.26. Patched: 2.3.27. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-wgqr-h4c5-gw82>
- GHSA-582m-wh92-4vhr (high, published 2026-11-12): GITLAB_PERMISSION_MODE=modify delete guard bypassed by a comma between mutation variables and the selection set. Affected: <= 2.3.25. Patched: 2.3.26. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-582m-wh92-4vhr>
- GHSA-m9qr-545q-8xc6 (high, published 2026-10-30): Docker image ships Node.js 22.21.1, vulnerable to CVE-2026-111497 (Brotli decoder RCE), reachable before authentication. Affected: <= 2.3.15. Patched: 2.3.16. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-m9qr-545q-8xc6>
- GHSA-rr94-3mff-76gg (high, published 2026-10-27): Startup version check sends GitLab credentials from the environment to a registry chosen by the working directory's `.npmrc`. Affected: >= 2.1.55, <= 2.3.11. Patched: 2.3.12. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-rr94-3mff-76gg>
- GHSA-2p72-j379-vmm3 (medium, published 2026-10-25): Missing session owner binding in REMOTE_AUTHORIZATION mode and GITLAB_DOWNLOAD_DIR confinement/exclusive-write bypass in download_job_artifacts. Affected: <= 2.3.9. Patched: 2.3.10. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-2p72-j379-vmm3>
- GHSA-q96h-922g-m3h3 (medium, published 2026-10-24): Remote download capability URLs bypass the per-session project allowlist (ENABLE_DYNAMIC_PROJECT_SCOPE). Affected: >= 2.1.58, <= 2.3.7. Patched: 2.3.8. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-q96h-922g-m3h3>
- GHSA-5xhm-p3jx-2fmc (medium, published 2026-10-23): gitlab_api_request: project allowlist is silently skipped for any GitLab API path that has no parseable project ID. Affected: >= 2.2.5, <= 2.3.6. Patched: 2.3.7. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-5xhm-p3jx-2fmc>
- GHSA-g4cw-m236-q72h (low, published 2026-10-15): Session IDs are logged in plaintext and MCP OAuth sessions are not bound to their owner. Affected: >= 2.0.8, <= 2.2.6. Patched: 2.3.0. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-g4cw-m236-q72h>
- GHSA-2jv7-p2g4-9f2h (medium, published 2026-10-15): GITLAB_OAUTH_ALLOWED_GROUPS is only checked at OAuth code exchange. Affected: >= 2.1.19, <= 2.2.6. Patched: 2.3.0. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-2jv7-p2g4-9f2h>
- GHSA-3gfg-wh5g-cf74 (medium, published 2026-10-15): GITLAB_TOOL_POLICY_HIDDEN makes tools from disabled toolsets callable. Affected: >= 2.1.0, <= 2.2.6. Patched: 2.3.0. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-3gfg-wh5g-cf74>
- GHSA-64g9-hrwx-9g6m (medium, published 2026-10-15): Local OAuth callback server returns GitLab tokens to any local caller. Affected: >= 2.0.11, <= 2.2.6. Patched: 2.3.0. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-64g9-hrwx-9g6m>
- GHSA-ffr3-5f57-gf93 (medium, published 2026-10-15): Project allowlist bypass through target_project_id and work item note emoji tools. Affected: >= 1.0.77, <= 2.2.6. Patched: 2.3.0. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-ffr3-5f57-gf93>
- GHSA-vhp9-2xfv-rrfv (high, published 2026-10-15): download_attachment overwrites files in the working directory, including in readonly mode. Affected: >= 1.0.77, <= 2.2.6. Patched: 2.3.0. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-vhp9-2xfv-rrfv>
- GHSA-5w3p-qj7g-79v5 (high, published 2026-10-15): OAuth callback proxy lets any registered client receive a victim's GitLab tokens. Affected: >= 2.1.4, <= 2.2.6. Patched: 2.3.0. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-5w3p-qj7g-79v5>
- GHSA-qcj2-qcc2-5fg4 (high, published 2026-10-14): Project Scope Authorization Bypass. Affected: >= 2.1.58, <= 2.2.5. Patched: 2.2.6. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-qcj2-qcc2-5fg4>
- GHSA-7cr4-55f8-p36f (medium, published 2026-09-23): GITLAB_PERMISSION_MODE=modify delete-ban bypassed: comma-separated GraphQL operations make mutations invisible to graphqlQueryContainsDeleteOperation (distinct mechanism from GHSA-f492). Affected: <= 2.1.63. Patched: 2.1.65. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-7cr4-55f8-p36f>
- GHSA-v279-9wq4-63rm (high, published 2026-09-23): GITLAB_PERMISSION_MODE=modify exposes destructive stop/cancel pipeline and environment tools missing from the deleteTools registry (REST-tool layer sibling of GHSA-f492). Affected: <= 2.1.63. Patched: 2.1.65. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-v279-9wq4-63rm>
- GHSA-m682-5gg2-5rc9 (high, published 2026-09-23): encodeGitLabPath never blocks '../': GHSA-4rm9 patch bypass leads to path traversal (4 call sites). Affected: >= 0.0.1. Patched: 2.1.65. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-m682-5gg2-5rc9>
- GHSA-cjfw-chc3-4r4v (high, published 2026-09-23): Server GitLab credential exfiltration: Private-Token/JOB-TOKEN forwarded across an unvalidated download redirect. Affected: <= 2.1.62. Patched: 2.1.65. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-cjfw-chc3-4r4v>
- GHSA-frxm-jmmc-j2xh (high, published 2026-09-23): SSRF: download proxy follows an attacker-set GitLab redirect to internal hosts without re-validating the target. Affected: <= 2.1.62. Patched: 2.1.65. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-frxm-jmmc-j2xh>
- GHSA-ph8m-54rc-77fp (medium, published 2026-09-23): Session-exhaustion DoS in @zereight/mcp-gitlab SSE transport: /sse lacks the session cap, rate limit, and idle timeout. Affected: <= 2.1.62. Patched: 2.1.65. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-ph8m-54rc-77fp>
- GHSA-f492-qxqp-m79r (high, published 2026-09-23): GITLAB_PERMISSION_MODE=modify delete-ban bypassed: destructive GraphQL mutations with non-delete verb names (environmentStop, clusterAgentTokenRevoke, pipelineCancel) pass graphqlQueryContainsDeleteOperation and execute against the operator's GitLab instance. Affected: >= 2.1.30. Patched: 2.1.65. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-f492-qxqp-m79r>
- GHSA-24vp-rch2-gjqq (high, published 2026-09-19): Unauthenticated session exhaustion denies service to legitimate clients. Affected: < 2.1.30. Patched: 2.1.30. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-24vp-rch2-gjqq>
- GHSA-64mg-3vx9-g74j (high, published 2026-09-19): execute_graphql defeats read-only mode and GITLAB_ALLOWED_PROJECT_IDS. Affected: < 2.1.30. Patched: 2.1.30. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-64mg-3vx9-g74j>
- GHSA-4rm9-rfp2-j39q (high, published 2026-07-19): Path escape in download_release_asset via direct_asset_path enables same-host project-scope bypass. Affected: < 2.1.41. Patched: 2.1.41. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-4rm9-rfp2-j39q>
- GHSA-7c3w-fxgh-frc7 (high, published 2026-07-19): Path traversal in job_id turns a job tool into an arbitrary GitLab API request under the operator token. Affected: < 2.1.32. Patched: 2.1.32. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-7c3w-fxgh-frc7>
- GHSA-5648-rgj9-v224 (high, published 2026-07-05): Multiple safety-control bypasses in @zereight/mcp-gitlab: execute_graphql read-only + allow-list bypass, unauthenticated transports, session-exhaustion DoS. Affected: < 2.1.30. Patched: 2.1.30. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-5648-rgj9-v224>
- GHSA-vmp7-252j-cwp7 / CVE-2026-61568 (critical, published 2026-07-03): DNS rebinding reaches local Streamable HTTP MCP transport. Affected: < 2.1.30. Patched: 2.1.30. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-vmp7-252j-cwp7>
- GHSA-2h44-8472-frjj / CVE-2026-61559 (critical, published 2026-07-01): Server-Side Request Forgery (SSRF) in zereight/mcp-gitlab. Affected: >= 0.0.1. Patched: 2.1.27. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-2h44-8472-frjj>
- GHSA-cv3r-c5h8-f4g5 / CVE-2026-61560 (critical, published 2026-06-22): Unauthenticated arbitrary file read via `upload_markdown` enables PAT exfiltration and full account takeover. Affected: < 2.1.27. Patched: 2.1.27. <https://github.com/zereight/gitlab-mcp/security/advisories/GHSA-cv3r-c5h8-f4g5>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `gitlab-mcp-zereight`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
