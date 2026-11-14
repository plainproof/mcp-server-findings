# Filesystem (reference server)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-server-filesystem` |
| Repository | <https://github.com/modelcontextprotocol/servers> (`src/filesystem`) |
| Package | `npm:@modelcontextprotocol/server-filesystem` |
| Publisher | modelcontextprotocol (GitHub organisation account) |
| Licence detected by GitHub | NOASSERTION |
| Upstream status | `active` |
| Latest release | 2.3.0 (2026-11-11) |
| Commit read | `e1dc4b18dbb9` on `main` (2026-11-11) |
| GitHub stars | 91986 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C7, C10; partly meets C5, C8; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for @modelcontextprotocol/server-filesystem@2.3.0 names the repository `git+https://github.com/modelcontextprotocol/servers.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/@modelcontextprotocol/server-filesystem/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/modelcontextprotocol/servers/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 2.3.0 is dated 2026-11-11; the newest commit on `main` is dated 2026-11-11; GitHub reports the last push on 2026-11-12.

Source: <https://api.github.com/repos/modelcontextprotocol/servers>, <https://registry.npmjs.org/@modelcontextprotocol/server-filesystem/latest>, <https://github.com/modelcontextprotocol/servers/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

8 advisories are published in the repository's advisory list for @modelcontextprotocol/server-filesystem; each names a patched version at or below the latest release (2.3.0). Most recent: GHSA-7m4x-rv66-mxhh (medium, published 2026-11-11, patched in 2.3.0).

Source: <https://github.com/modelcontextprotocol/servers/security/advisories>, <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-7m4x-rv66-mxhh> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Access is confined to the directories given at start-up; write tools are served unless `--read-only` is added. Quoted: “The server may touch only its **allowed directories**.”; “Add `--read-only` to serve only the tools that cannot change the filesystem:”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/filesystem/README.md?plain=1#L19> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The documented setup takes no credential. Searched `src/filesystem/README.md` for: API_KEY, _TOKEN\b, password.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/filesystem/README.md> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `src/filesystem/README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/filesystem/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/package-lock.json>, <https://github.com/modelcontextprotocol/servers/tree/e1dc4b18dbb948921da37f3d4224a628730b43b0> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `src/filesystem/README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial; `SECURITY.md` for: prompt-injection, untrusted.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/filesystem/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/server ^2.3.1. Lower-bound version 2.3.1 of @modelcontextprotocol/server (npm) was published on 2026-10-05, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/@modelcontextprotocol/server-filesystem/latest>, <https://registry.npmjs.org/@modelcontextprotocol/server> (verified 2026-11-14)

## Advisories published by the project

- GHSA-7m4x-rv66-mxhh (medium, published 2026-11-11): server-filesystem: `move_file`'s same-device rename leaves the source unpinned — a swapped source parent moves an outside file into the allowed directories, where it becomes readable. Affected: < 2.3.0; >= 2025.1.14, <= 2026.8.31. Patched: 2.3.0. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-7m4x-rv66-mxhh>
- GHSA-p9cv-8g75-4xcg (medium, published 2026-11-11): Symlink swap after validation lets read_text_file return files outside allowedDirectories. Affected: < 2.3.0; >= 2025.1.14, <= 2026.8.31. Patched: 2.3.0. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-p9cv-8g75-4xcg>
- GHSA-4gxg-m5jx-9j57 (medium, published 2026-10-25): Case-variant path bypasses symlink check and allows creating files outside allowed directories in server-filesystem. Affected: = 2026.8.31; >= 1.0.0, < 2.0.1. Patched: 2.0.1. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-4gxg-m5jx-9j57>
- GHSA-7rgq-gccq-qphx (medium, published 2026-10-25): Path traversal via trailing quote/whitespace in validatePath (Check/Use Mismatch). Affected: >= 1.0.0, < 2.0.1; >= 2025.8.21, <= 2026.8.31. Patched: 2.0.1. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-7rgq-gccq-qphx>
- GHSA-53mr-w429-c597 (low, published 2026-10-25): Parent-Directory Fallback TOCTOU in @modelcontextprotocol/server-filesystem Permits Arbitrary File Write Outside allowedDirectories. Affected: < 2.0.1; >= 2025.1.14, <= 2026.8.31. Patched: 2.0.1. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-53mr-w429-c597>
- GHSA-hhwq-wxfx-cj7g (low, published 2026-10-25): @modelcontextprotocol/server-filesystem list_directory_with_sizes follows symlinks and leaks outside-directory file metadata. Affected: >= 1.0.0, < 2.0.1; >= 2025.7.1, <= 2026.8.31. Patched: 2.0.1. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-hhwq-wxfx-cj7g>
- GHSA-hc55-p739-j48w / CVE-2025-53110 (high, published 2025-07-01): Path validation bypass via colliding path prefix. Affected: < 0.6.3, < 2025.3.28. Patched: 0.6.3, 2025.7.01. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-hc55-p739-j48w>
- GHSA-q66q-fx2p-7w4m / CVE-2025-53109 (high, published 2025-07-01): Path validation bypass via symlink handling. Affected: < 0.6.3, < 2025.3.28. Patched: 0.6.3, 2025.7.01. <https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-q66q-fx2p-7w4m>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-server-filesystem`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
