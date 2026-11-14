# Desktop Commander MCP

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `desktop-commander` |
| Repository | <https://github.com/wonderwhy-er/DesktopCommanderMCP> |
| Package | `npm:@wonderwhy-er/desktop-commander` |
| Publisher | wonderwhy-er (GitHub user account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 0.3.3 (2026-11-12) |
| Commit read | `bce370e9395f` on `main` (2026-11-12) |
| GitHub stars | 10307 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C9, C10; partly meets C5, C7, C8.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for @wonderwhy-er/desktop-commander@0.3.3 names the repository `git+https://github.com/wonderwhy-er/DesktopCommanderMCP.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/@wonderwhy-er/desktop-commander/latest> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/wonderwhy-er/DesktopCommanderMCP/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 0.3.3 is dated 2026-11-12; the newest commit on `main` is dated 2026-11-12; GitHub reports the last push on 2026-11-12.

Source: <https://api.github.com/repos/wonderwhy-er/DesktopCommanderMCP>, <https://registry.npmjs.org/@wonderwhy-er/desktop-commander/latest>, <https://github.com/wonderwhy-er/DesktopCommanderMCP/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/wonderwhy-er/DesktopCommanderMCP/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Terminal commands and file edits are core functions; the README documents directory and command restrictions and states their limits. Quoted: “Directory restrictions and command blocking can be bypassed through various methods including symlinks, command substitution, and absolute paths or code execution”.

Source: <https://github.com/wonderwhy-er/DesktopCommanderMCP/blob/bce370e9395f5bc74eda34913e5ae1dee48df8f8/README.md?plain=1#L832> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The documented local setup takes no API key or token. Searched `README.md` for: API_KEY, _TOKEN\b.

Source: <https://github.com/wonderwhy-er/DesktopCommanderMCP/blob/bce370e9395f5bc74eda34913e5ae1dee48df8f8/README.md> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: partly meets

Telemetry is documented as collected by default, with a documented opt-out. The npm record declares a `postinstall` script that runs `dist/track-installation.js`. Quoted: “Desktop Commander collects limited, pseudonymous telemetry to improve the tool.”; “**Opt-out:** Ask Claude to "disable Desktop Commander telemetry" or set `"telemetryEnabled": false` in your config.”; “node dist/track-installation.js”.

Source: <https://github.com/wonderwhy-er/DesktopCommanderMCP/blob/bce370e9395f5bc74eda34913e5ae1dee48df8f8/README.md?plain=1#L1141>, <https://registry.npmjs.org/@wonderwhy-er/desktop-commander/latest> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/wonderwhy-er/DesktopCommanderMCP/blob/bce370e9395f5bc74eda34913e5ae1dee48df8f8/package-lock.json>, <https://github.com/wonderwhy-er/DesktopCommanderMCP/tree/bce370e9395f5bc74eda34913e5ae1dee48df8f8> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: meets

The security policy names prompt injection and recommends OS-level isolation for that case. Quoted: “Desktop Commander does not protect against a compromised AI account or prompt injection reaching a trusted client. For that threat model, use OS-level isolation.”.

Source: <https://github.com/wonderwhy-er/DesktopCommanderMCP/blob/bce370e9395f5bc74eda34913e5ae1dee48df8f8/SECURITY.md?plain=1#L44> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/sdk ^1.32.1. Lower-bound version 1.32.1 of @modelcontextprotocol/sdk (npm) was published on 2026-10-05, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/@wonderwhy-er/desktop-commander/latest>, <https://registry.npmjs.org/@modelcontextprotocol/sdk> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `desktop-commander`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
