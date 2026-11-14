# MCP Atlassian

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-atlassian-sooperset` |
| Repository | <https://github.com/sooperset/mcp-atlassian> |
| Package | `pypi:mcp-atlassian; oci:ghcr.io/sooperset/mcp-atlassian` |
| Publisher | sooperset (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 0.24.4 (2026-11-13) |
| Commit read | `a633020248d6` on `main` (2026-11-14) |
| GitHub stars | 6119 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C2, C3, C4, C6, C7, C10; partly meets C1, C5, C8; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The PyPI record for mcp-atlassian 0.24.4 lists no project or repository URL; the repository's `pyproject.toml` declares the package name `mcp-atlassian`. PyPI holds no provenance attestation for the release (the integrity record returned HTTP 404).

Source: <https://pypi.org/pypi/mcp-atlassian/json>, <https://github.com/sooperset/mcp-atlassian/blob/a633020248d6e559c5719c6bcb8f668f76273fd9/pyproject.toml>, <https://pypi.org/integrity/mcp-atlassian/0.24.4/mcp_atlassian-0.24.4-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/sooperset/mcp-atlassian/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 0.24.4 is dated 2026-11-13; the newest commit on `main` is dated 2026-11-14; GitHub reports the last push on 2026-11-14.

Source: <https://api.github.com/repos/sooperset/mcp-atlassian>, <https://pypi.org/pypi/mcp-atlassian/json>, <https://github.com/sooperset/mcp-atlassian/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

55 advisories are published in the repository's advisory list; each names a patched version at or below the latest release (0.24.4). Most recent: GHSA-qx5g-fhgg-wm59 (low, published 2026-11-12, patched in 0.24.2).

Source: <https://github.com/sooperset/mcp-atlassian/security/advisories>, <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-qx5g-fhgg-wm59> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The project's configuration documentation describes a read-only mode that the operator can set. Quoted: “Read-only mode (disables all write operations)”.

Source: <https://mcp-atlassian.soomiles.com/docs/configuration> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

API tokens are supplied through environment variables. Quoted: “"JIRA_API_TOKEN": "your_api_token"”.

Source: <https://github.com/sooperset/mcp-atlassian/blob/a633020248d6e559c5719c6bcb8f668f76273fd9/README.md?plain=1#L42> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/sooperset/mcp-atlassian/blob/a633020248d6e559c5719c6bcb8f668f76273fd9/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`uv.lock`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/sooperset/mcp-atlassian/blob/a633020248d6e559c5719c6bcb8f668f76273fd9/uv.lock>, <https://github.com/sooperset/mcp-atlassian/tree/a633020248d6e559c5719c6bcb8f668f76273fd9> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial; `SECURITY.md` for: prompt-injection, untrusted.

Source: <https://github.com/sooperset/mcp-atlassian/blob/a633020248d6e559c5719c6bcb8f668f76273fd9/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: fastmcp<4.0.0,>=3.4.7 (also mcp<2.0.0,>=1.27.0). Lower-bound version 3.4.7 of fastmcp (PyPI) was published on 2026-08-10, within the 12 months before 2026-11-14.

Source: <https://pypi.org/pypi/mcp-atlassian/json>, <https://pypi.org/pypi/fastmcp/json> (verified 2026-11-14)

## Advisories published by the project

- GHSA-qx5g-fhgg-wm59 (low, published 2026-11-12): Residual JIRA_PROJECTS_FILTER leak through epic cross-reference fetch in get_issue; create_issue's parent field remains unscoped. Affected: < 0.24.2. Patched: 0.24.2. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-qx5g-fhgg-wm59>
- GHSA-2w5r-h8v2-c9cx (medium, published 2026-11-08): SSE auth gate in v0.23.1 misses most of the message endpoint. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-2w5r-h8v2-c9cx>
- GHSA-cf68-pxw7-c8fr (critical, published 2026-11-08): Unvalidated `attachment_id` in the Confluence `download_attachment` tool allows authenticated path injection and credential-forwarded fetches(SSRF). Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-cf68-pxw7-c8fr>
- GHSA-qh7q-jmc7-rc7j / CVE-2026-124503 (high, published 2026-11-08): mcp-atlassian: upload guard boundary is the process CWD — remote HTTP/SSE deployments started from a wide working directory (systemd default root) restore the arbitrary file read closed by the #1448 batch (CWE-22). Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-qh7q-jmc7-rc7j>
- GHSA-7876-w4xp-76fv (medium, published 2026-11-08): Reflected XSS in standalone OAuth authorization script callback handler. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-7876-w4xp-76fv>
- GHSA-cffg-pgvw-r443 (low, published 2026-11-08): Debug authentication failure logging exposes lowercase and custom secret HTTP headers. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-cffg-pgvw-r443>
- GHSA-3qhx-3fh4-8w9v (medium, published 2026-11-08): Attachment retrieval can forward service credentials to off-origin URLs and custom headers across redirects. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-3qhx-3fh4-8w9v>
- GHSA-3c6h-qwx8-hjcm (high, published 2026-11-08): SsrfPinningAdapter proxy-stripping trusts user-supplied hostnames, enabling DNS-rebinding SSRF via operator proxy. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-3c6h-qwx8-hjcm>
- GHSA-pwx2-x8g8-prvm (medium, published 2026-11-08): SSRF: Forms API PAT/basic-auth branch bypasses SSRF redirect and DNS-pinning protections. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-pwx2-x8g8-prvm>
- GHSA-jpxv-989p-f3pf (medium, published 2026-11-08): SSRF + credential exfiltration via the request URL header in external-auth mode. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-jpxv-989p-f3pf>
- GHSA-rh5v-38gg-q3jj (high, published 2026-11-08): Unauthenticated SSRF and authentication-gate bypass via X-Atlassian-{Jira,Confluence}-Url request headers in multi-user HTTP transport. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-rh5v-38gg-q3jj>
- GHSA-q2h8-fm7r-v7f2 (high, published 2026-11-08): jira_add_comment silently posts JSM internal notes as customer-visible, emailing them to the customer. Affected: >= 0.22.0, <= 0.23.1. Patched: 0.24.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-q2h8-fm7r-v7f2>
- GHSA-823g-2jmv-9gmc (medium, published 2026-11-08): Confluence download paths missing the GHSA-6vmq cwd-root overwrite guard — residual CWE-22/94 gap from CVE-2026-77271. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-823g-2jmv-9gmc>
- GHSA-5w8q-mmhc-55fp (medium, published 2026-11-08): mcp-atlassian OAuth Setup Callback Listens on 0.0.0.0 Enabling Remote Callback Hijacking. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-5w8q-mmhc-55fp>
- GHSA-xv8h-26ch-vfh9 (high, published 2026-11-08): Project/space allowlist enforced on only 2 of ~15 tools: all writes and all read-by-key tools (except Jira get_issue) bypass JIRA_PROJECTS_FILTER / CONFLUENCE_SPACES_FILTER. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-xv8h-26ch-vfh9>
- GHSA-7vjf-5wh5-87q7 (medium, published 2026-11-08): JQL/CQL injection bypasses the JIRA_PROJECTS_FILTER / CONFLUENCE_SPACES_FILTER allowlist (access-control bypass). Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-7vjf-5wh5-87q7>
- GHSA-rwqj-c54w-32jr (low, published 2026-11-08): Sensitive OAuth data written to logs (authorization URL with CSRF state; token-endpoint response body). Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-rwqj-c54w-32jr>
- GHSA-8ffx-6c2g-75cc (low, published 2026-11-08): Path traversal in jira_remove_issue_link allows issue deletion. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-8ffx-6c2g-75cc>
- GHSA-85p8-f4j5-j5jp (medium, published 2026-11-08): SSRF filter bypass via NAT64 IPv6-transition prefix (64:ff9b::/96) reaches internal / cloud-metadata endpoints. Affected: < 0.24.1. Patched: 0.24.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-85p8-f4j5-j5jp>
- GHSA-5j8j-256g-vvp5 (critical, published 2026-08-19): Unauthenticated tool execution as operator via `--transport sse` (UserTokenMiddleware never matches SSE paths). Affected: <= 0.23.0. Patched: 0.23.1. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-5j8j-256g-vvp5>
- GHSA-g5r6-gv6m-f5jv / CVE-2026-73498 (high, published 2026-07-10): Arbitrary file read via missing path validation in confluence_upload_attachment. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-g5r6-gv6m-f5jv>
- GHSA-489g-7rxv-6c8q / CVE-2026-73497 (high, published 2026-07-10): DNS-rebinding TOCTOU bypass of the SSRF fix (GHSA-7r34): unauthenticated SSRF to cloud metadata on patched ≥0.17.0. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-489g-7rxv-6c8q>
- GHSA-72fm-whvq-jghf / CVE-2026-77242 (high, published 2026-07-10): Incomplete fix for CVE-2026-27826: DNS rebinding bypasses SSRF validation (validated IP not pinned). Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-72fm-whvq-jghf>
- GHSA-wm45-qh3g-v83f / CVE-2026-73496 (high, published 2026-07-10): Arbitrary server-side file read via attachment upload in mcp-atlassian. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-wm45-qh3g-v83f>
- GHSA-3r68-hf9h-887v / CVE-2026-77243 (high, published 2026-07-10): ENABLED_TOOLS / Toolset authorization bypass in mcp-atlassian. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-3r68-hf9h-887v>
- GHSA-cc5h-2pwp-pvcc / CVE-2026-77248 (high, published 2026-07-10): Unauthenticated arbitrary local file read via upload_attachment file_path, chained with missing auth on streamable-http transport. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-cc5h-2pwp-pvcc>
- GHSA-f6pj-qv47-g96w / CVE-2026-77247 (high, published 2026-07-10): Arbitrary server-local file upload to Jira/Confluence attachments via unrestricted file_path parameters. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-f6pj-qv47-g96w>
- GHSA-v9m3-wfh8-5646 / CVE-2026-77249 (medium, published 2026-07-10): Incomplete fix for GHSA-7r34-79r5-rcc9 (CVE-2026-27826): redirect-based SSRF via unhooked requests session in Jira user-permission lookup. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-v9m3-wfh8-5646>
- GHSA-wv8v-v4c5-v75j / CVE-2026-77246 (high, published 2026-07-10): MCP HTTP Client Server-Local File Exfiltration via Unvalidated Attachment Upload Path. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-wv8v-v4c5-v75j>
- GHSA-wrhw-j3f9-8vc6 / CVE-2026-77244 (critical, published 2026-07-10): [mcp-atlassian] Authentication bypass in HTTP transport: AtlassianOpaqueTokenVerifier accepts any non-empty token; server falls back to env-var credentials, allowing unauthenticated use of operator's Jira/Confluence access. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-wrhw-j3f9-8vc6>
- GHSA-6rrj-86cw-gg9j / CVE-2026-77245 (high, published 2026-07-10): Multiple vulnerabilities: SSRF via icon_url + attachment URL, JQL injection, Stored XSS. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-6rrj-86cw-gg9j>
- GHSA-w66g-j6c4-hcfc / CVE-2026-77251 (medium, published 2026-07-10): Three sub-bugs in JIRA_PROJECTS_FILTER / CONFLUENCE_SPACES_FILTER allow forbidden-project content exfiltration (one LIVE-proven on Atlassian Cloud). Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-w66g-j6c4-hcfc>
- GHSA-g5xv-mhgm-v5f6 / CVE-2026-77250 (medium, published 2026-07-10): OAuth fallback token storage writes plaintext access and refresh tokens with group-readable permissions. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-g5xv-mhgm-v5f6>
- GHSA-rqwg-9346-fjjv / CVE-2026-77252 (medium, published 2026-07-10): JIRA_PROJECTS_FILTER and CONFLUENCE_SPACES_FILTER can be bypassed in search tools. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-rqwg-9346-fjjv>
- GHSA-vc25-24vv-fxxm / CVE-2026-77253 (high, published 2026-07-10): Jira and Confluence attachment upload tools can read arbitrary server-local files. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-vc25-24vv-fxxm>
- GHSA-vc8m-84rp-53hx / CVE-2026-77254 (critical, published 2026-07-10): Unauthenticated HTTP MCP requests can use globally configured Jira and Confluence credentials. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-vc8m-84rp-53hx>
- GHSA-hgcf-4mq8-5266 / CVE-2026-77274 (high, published 2026-07-10): SSRF Protection Bypass. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-hgcf-4mq8-5266>
- GHSA-2xj6-xx86-cwwc / CVE-2026-77255 (high, published 2026-07-10): Arbitrary File Read & Exfiltration (Confused Deputy) in JIRA update_issue. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-2xj6-xx86-cwwc>
- GHSA-76pr-5669-3xf5 / CVE-2026-77256 (medium, published 2026-07-10): OAuth refresh-token backup file is world-readable under default Unix umask. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-76pr-5669-3xf5>
- GHSA-mrq8-fv7v-hhjg / CVE-2026-77257 (high, published 2026-07-10): HTTP upload tools accept arbitrary server-local file paths. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-mrq8-fv7v-hhjg>
- GHSA-6cr4-ccf3-x7h4 / CVE-2026-77259 (high, published 2026-07-10): Arbitrary file read via confluence_upload_attachment allows exfiltration of server credentials. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-6cr4-ccf3-x7h4>
- GHSA-93xw-j965-9mx3 / CVE-2026-77258 (high, published 2026-07-10): Arbitrary file read/exfiltration via upload_attachment missing validate_safe_path(). Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-93xw-j965-9mx3>
- GHSA-f4p7-qx46-wc5j / CVE-2026-77260 (high, published 2026-07-10): Arbitrary local file READ via unconstrained file_path in upload_attachment (Confluence + Jira) — mirror of patched CVE-2026-27825. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-f4p7-qx46-wc5j>
- GHSA-6529-c226-h328 / CVE-2026-77261 (high, published 2026-07-10): SSRF redirect protection missing for basic-auth and OAuth authentication branches. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-6529-c226-h328>
- GHSA-mfv2-4wvm-9pgp / CVE-2026-77266 (medium, published 2026-07-10): Path traversal in upload_attachment allows arbitrary file read and exfiltration via MCP tool call. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-mfv2-4wvm-9pgp>
- GHSA-5wf4-jqxh-8gm3 / CVE-2026-77267 (medium, published 2026-07-10): Incomplete fix for CVE-2026-27826 in mcp-atlassian. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-5wf4-jqxh-8gm3>
- GHSA-p6hp-93wp-fh6p / CVE-2026-77262 (high, published 2026-07-10): Path Traversal / Arbitrary File Read in confluence_upload_attachment MCP tool (incomplete fix of GHSA-xjgw-4wvw-rgm4). Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-p6hp-93wp-fh6p>
- GHSA-h7wj-5v37-59r2 / CVE-2026-77269 (high, published 2026-07-10): Path traversal in upload_attachment allows arbitrary file read (incomplete fix for CVE-2026-27825). Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-h7wj-5v37-59r2>
- GHSA-f26r-j276-ggg4 / CVE-2026-77270 (medium, published 2026-07-10): Arbitrary File Read via Upload Attachment Tools. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-f26r-j276-ggg4>
- GHSA-49xv-9743-pw8w / CVE-2026-77265 (medium, published 2026-07-10): SSRF via DNS Rebinding in Header-Based Authentication Flow. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-49xv-9743-pw8w>
- GHSA-4596-2p6p-28cv / CVE-2026-77268 (medium, published 2026-07-10): Insecure File Permissions on OAuth Token Storage. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-4596-2p6p-28cv>
- GHSA-g2r2-3j32-j27x / CVE-2026-77272 (medium, published 2026-07-10): Reflected XSS in OAuth Setup Callback Handler. Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-g2r2-3j32-j27x>
- GHSA-6vmq-24h2-pj7j / CVE-2026-77271 (high, published 2026-07-10): Incomplete path traversal fix allows intra-CWD module overwrite and RCE (bypass of GHSA-xjgw-4wvw-rgm4). Affected: < 0.22.0. Patched: 0.22.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-6vmq-24h2-pj7j>
- GHSA-xjgw-4wvw-rgm4 / CVE-2026-27825 (critical, published 2026-02-24): Arbitrary file write leading to arbitrary code execution via unconstrained download_path in confluence_download_attachment. Affected: <0.17.0. Patched: >=0.17.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-xjgw-4wvw-rgm4>
- GHSA-7r34-79r5-rcc9 / CVE-2026-27826 (high, published 2026-02-24): SSRF via unvalidated X-Atlassian-Jira-Url / X-Atlassian-Confluence-Url headers allows unauthenticated access to internal services and cloud metadata. Affected: <0.17.0. Patched: >=0.17.0. <https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-7r34-79r5-rcc9>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-atlassian-sooperset`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
