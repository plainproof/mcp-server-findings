# Framelink MCP for Figma

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `figma-context-mcp` |
| Repository | <https://github.com/GLips/Figma-Context-MCP> |
| Package | `npm:figma-developer-mcp` |
| Publisher | GLips (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 0.13.2 (2026-06-18) |
| Commit read | `c083d65c7e00` on `main` (2026-06-24) |
| GitHub stars | 16206 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C5, C7, C10; partly meets C6, C8; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for figma-developer-mcp@0.13.2 names the repository `git+https://github.com/GLips/Figma-Context-MCP.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/figma-developer-mcp/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/GLips/Figma-Context-MCP/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 0.13.2 is dated 2026-06-18; the newest commit on `main` is dated 2026-06-24; GitHub reports the last push on 2026-10-27.

Source: <https://api.github.com/repos/GLips/Figma-Context-MCP>, <https://registry.npmjs.org/figma-developer-mcp/latest>, <https://github.com/GLips/Figma-Context-MCP/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

1 advisory is published in the repository's advisory list; it names a patched version at or below the latest release (0.13.2). Most recent: GHSA-gxw4-4fc5-9gr5 (high, published 2025-09-29, patched in 0.6.3).

Source: <https://github.com/GLips/Figma-Context-MCP/security/advisories>, <https://github.com/GLips/Figma-Context-MCP/security/advisories/GHSA-gxw4-4fc5-9gr5> (verified 2026-11-14)

### C5. Documented scope controls: meets

The README describes the server as fetching Figma design data for the model; no write or execute tool is documented in the README. Quoted: “it simplifies and translates the response so only the most relevant layout and styling information is provided to the model.”.

Source: <https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/README.md?plain=1#L47> (verified 2026-11-14)

### C6. Credential handling in the documented setup: partly meets

The README's configuration examples pass the Figma key as a command-line argument; an environment-variable alternative is mentioned. Quoted: “"args": ["-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]”; “Or you can set `FIGMA_API_KEY` and `PORT` in the `env` field.”.

Source: <https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/README.md?plain=1#L66> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`pnpm-lock.yaml`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/pnpm-lock.yaml>, <https://github.com/GLips/Figma-Context-MCP/tree/c083d65c7e002923e7cb98f4e3bdafb105e90f6d> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial; `SECURITY.md` for: prompt-injection, untrusted.

Source: <https://github.com/GLips/Figma-Context-MCP/blob/c083d65c7e002923e7cb98f4e3bdafb105e90f6d/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/sdk 1.29.0. Lower-bound version 1.29.0 of @modelcontextprotocol/sdk (npm) was published on 2026-03-30, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/figma-developer-mcp/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

- GHSA-gxw4-4fc5-9gr5 / CVE-2025-53967 (high, published 2025-09-29): figma-developer-mcp vulnerable to command injection in get_figma_data tool. Affected: <=0.6.2. Patched: 0.6.3. <https://github.com/GLips/Figma-Context-MCP/security/advisories/GHSA-gxw4-4fc5-9gr5>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `figma-context-mcp`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
