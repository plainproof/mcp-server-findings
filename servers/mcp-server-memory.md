# Memory (reference server)

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-server-memory` |
| Repository | <https://github.com/modelcontextprotocol/servers> (`src/memory`) |
| Package | `npm:@modelcontextprotocol/server-memory` |
| Publisher | modelcontextprotocol (GitHub organisation account) |
| Licence detected by GitHub | NOASSERTION |
| Upstream status | `active` |
| Latest release | 2.1.1 (2026-11-11) |
| Commit read | `e1dc4b18dbb9` on `main` (2026-11-11) |
| GitHub stars | 91986 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C5, C6, C7, C9, C10; partly meets C8.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for @modelcontextprotocol/server-memory@2.1.1 names the repository `git+https://github.com/modelcontextprotocol/servers.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/@modelcontextprotocol/server-memory/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/modelcontextprotocol/servers/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 2.1.1 is dated 2026-11-11; the newest commit on `main` is dated 2026-11-11; GitHub reports the last push on 2026-11-12.

Source: <https://api.github.com/repos/modelcontextprotocol/servers>, <https://registry.npmjs.org/@modelcontextprotocol/server-memory/latest>, <https://github.com/modelcontextprotocol/servers/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list for @modelcontextprotocol/server-memory.

Source: <https://github.com/modelcontextprotocol/servers/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: meets

The tools read and write only the server's own knowledge-graph file. Quoted: “`MEMORY_FILE_PATH`: Path to the memory storage JSONL file”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/memory/README.md?plain=1#L252> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The documented setup takes no credential. Searched `src/memory/README.md` for: API_KEY, _TOKEN\b, password.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/memory/README.md> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `src/memory/README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/memory/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/package-lock.json>, <https://github.com/modelcontextprotocol/servers/tree/e1dc4b18dbb948921da37f3d4224a628730b43b0> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: meets

The documented tools return only data the client stored through the server. Quoted: “`MEMORY_FILE_PATH`: Path to the memory storage JSONL file”.

Source: <https://github.com/modelcontextprotocol/servers/blob/e1dc4b18dbb948921da37f3d4224a628730b43b0/src/memory/README.md?plain=1#L252> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/server ^2.3.1. Lower-bound version 2.3.1 of @modelcontextprotocol/server (npm) was published on 2026-10-05, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/@modelcontextprotocol/server-memory/latest>, <https://registry.npmjs.org/@modelcontextprotocol/server> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-server-memory`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
