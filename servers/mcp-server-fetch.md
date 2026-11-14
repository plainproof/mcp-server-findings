# Fetch (reference server)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-server-fetch` |
| Repository | <https://github.com/modelcontextprotocol/servers> (`src/fetch`) |
| Package | `pypi:mcp-server-fetch` |
| Publisher | modelcontextprotocol (GitHub organisation account) |
| Licence detected by GitHub | NOASSERTION |
| Upstream status | `active` |
| Latest release | 2026.11.11 (2026-11-11) |
| Commit read | `e1dc4b18dbb9` on `main` (2026-11-11) |
| GitHub stars | 91986 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C5, C6, C10; partly meets C7, C8, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The PyPI record for mcp-server-fetch 2026.11.11 links the repository, and PyPI holds a provenance attestation for the release naming `modelcontextprotocol/servers` (workflow `release.yml`) as publisher.

Source: <https://pypi.org/pypi/mcp-server-fetch/json>, <https://pypi.org/integrity/mcp-server-fetch/2026.11.11/mcp_server_fetch-2026.11.11-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/modelcontextprotocol/servers/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 2026.11.11 is dated 2026-11-11; the newest commit on `main` is dated 2026-11-11; GitHub reports the last push on 2026-11-12.

Source: <https://api.github.com/repos/modelcontextprotocol/servers>, <https://pypi.org/pypi/mcp-server-fetch/json>, <https://github.com/modelcontextprotocol/servers/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

5 advisories are published in the repository's advisory list for mcp-server-fetch; each names a patched version at or below the latest release (2026.11.11). Most recent: GHSA-3rxj-6jhw-qfv7 (low, published 2026-11-11, patched in 2026.11.11).

Source: <https://github.com/modelcontextprotocol/servers/security/advisories>, <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-3rxj-6jhw-qfv7> (verified 2026-11-14)

### C5. Documented scope controls: meets

The single tool is documented as read-only. Quoted: “Annotations: `readOnlyHint: true`, `destructiveHint: false`, `idempotentHint: true`, `openWorldHint: true` (it only reads, and it reaches arbitrary hosts on the internet)”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/fetch/README.md?plain=1#L28> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The documented setup takes no credential. Searched `src/fetch/README.md` for: API_KEY, _TOKEN\b, password.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/fetch/README.md> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: partly meets

The documented function is retrieving arbitrary web addresses; the README documents a private-address guard and an optional host allowlist. It contains no reference to telemetry. Searched `src/fetch/README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog. Quoted: “By default the server may fetch from any host (subject to the private-address guard above).”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/fetch/README.md?plain=1#L210>, <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/fetch/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/package-lock.json>, <https://github.com/modelcontextprotocol/servers/tree/e1dc4b18dbb948921da37f3d4224a628730b43b0> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: partly meets

The README carries a caution about what the server can reach; it does not name prompt injection or untrusted content. Quoted: “This server can access local/internal IP addresses and may represent a security risk. Exercise caution when using this MCP server to ensure this does not expose any sensitive data.”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/fetch/README.md?plain=1#L12> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: mcp<3,>=2.3. Lower-bound version 2.3.0 of mcp (PyPI) was published on 2026-10-02, within the 12 months before 2026-11-14.

Source: <https://pypi.org/pypi/mcp-server-fetch/json>, <https://pypi.org/pypi/mcp/json> (verified 2026-11-14)

## Advisories published by the project

- GHSA-3rxj-6jhw-qfv7 (low, published 2026-11-11): mcp-server-fetch: IPv6 site-local fec0::/10 classified as public (SSRF guard classifier gap, CWE-918). Affected: >= 2026.10.10, < 2026.11.11. Patched: 2026.11.11. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-3rxj-6jhw-qfv7>
- GHSA-f9hh-cmx9-2f23 (low, published 2026-11-11): mcp-server-fetch: robots.txt path-canonicalization bypass (e.g. //private fetched while Disallow: /private). Affected: >= 0.6.1, < 2026.11.11. Patched: 2026.11.11. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-f9hh-cmx9-2f23>
- GHSA-3jqg-r5pp-rmp2 (low, published 2026-10-25): robots.txt enforcement bypass via HTTP redirects in mcp-server-fetch. Affected: >= 0.6.1, <= 2026.10.19. Patched: 2026.10.24. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-3jqg-r5pp-rmp2>
- GHSA-66qx-2266-pmj6 (low, published 2026-10-25): fetch server: SSRF guard treats the well-known NAT64 prefix 64:ff9b::/96 as public, so a metadata address is reachable on NAT64/DNS64 egress. Affected: >= 2026.10.10, <= 2026.10.19. Patched: 2026.10.24. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-66qx-2266-pmj6>
- GHSA-v38p-wf49-hx2j (medium, published 2026-10-25): fetch: private-address guard bypass via IDNA hostnames (check and connect resolve different names). Affected: >= 2026.10.10, <= 2026.10.19. Patched: 2026.10.24. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-v38p-wf49-hx2j>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-server-fetch`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
