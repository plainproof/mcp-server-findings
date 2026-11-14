# MCP Toolbox for Databases

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `genai-toolbox` |
| Repository | <https://github.com/googleapis/mcp-toolbox>; listed at selection as <https://github.com/googleapis/genai-toolbox> |
| Package | `binary:storage.googleapis.com/mcp-toolbox-for-databases; oci:us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox; npm:@toolbox-sdk/server` |
| Publisher | googleapis (GitHub organisation account) |
| Licence detected by GitHub | Apache-2.0 |
| Upstream status | `renamed` - The repository was renamed from googleapis/genai-toolbox to googleapis/mcp-toolbox; the old address redirects. Quoted: “The `genai-toolbox` repository has been officially renamed to `mcp-toolbox`.”. |
| Latest release | v1.17.0 (2026-11-13) |
| Commit read | `a313b10c4188` on `main` (2026-11-14) |
| GitHub stars | 16872 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C7, C8, C10; partly meets C5; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The source repository is public and release v1.17.0 is published from it. The release notes list a SHA256 hash for each platform binary and link a signature file for the linux/amd64 binary.

Source: <https://github.com/googleapis/mcp-toolbox/releases/tag/v1.17.0> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository (`SECURITY.md` in the repository), and it describes how to report a vulnerability.

Source: <https://github.com/googleapis/mcp-toolbox/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release v1.17.0 is dated 2026-11-13; the newest commit on `main` is dated 2026-11-14; GitHub reports the last push on 2026-11-14.

Source: <https://api.github.com/repos/googleapis/mcp-toolbox>, <https://github.com/googleapis/mcp-toolbox/releases/tag/v1.17.0>, <https://github.com/googleapis/mcp-toolbox/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/googleapis/mcp-toolbox/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Prebuilt database tools are enabled by a flag and can be narrowed to a toolset; other tools are defined by the operator. No read-only switch is described in the README. Quoted: “You can also specify a specific toolset using the `--prebuilt=<database>/<toolset>` syntax”.

Source: <https://github.com/googleapis/mcp-toolbox/blob/a313b10c4188a33d3a6ed982e9397813bb3a26a0/README.md?plain=1#L97> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

Prebuilt configurations take connection settings from environment variables. (The README's `tools.yaml` example also shows a `password` field in the configuration file.) Quoted: “Set the appropriate environment variables to connect”.

Source: <https://github.com/googleapis/mcp-toolbox/blob/a313b10c4188a33d3a6ed982e9397813bb3a26a0/README.md?plain=1#L95> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README describes OpenTelemetry export to an endpoint the operator sets with a flag; no collection by the publisher is described. Quoted: “Toolbox emits traces and metrics via OpenTelemetry. Use `--telemetry-otlp=<endpoint>`”.

Source: <https://github.com/googleapis/mcp-toolbox/blob/a313b10c4188a33d3a6ed982e9397813bb3a26a0/README.md?plain=1#L1098> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`go.sum`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/googleapis/mcp-toolbox/blob/a313b10c4188a33d3a6ed982e9397813bb3a26a0/go.sum>, <https://github.com/googleapis/mcp-toolbox/blob/a313b10c4188a33d3a6ed982e9397813bb3a26a0/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial; `SECURITY.md` for: prompt-injection, untrusted.

Source: <https://github.com/googleapis/mcp-toolbox/blob/a313b10c4188a33d3a6ed982e9397813bb3a26a0/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

`go.mod` declares no MCP library; the server implements the protocol in its own source tree, which contains a module for specification revision 2026-07-28 (`internal/server/mcp/v20260728`), published within the last 12 months.

Source: <https://github.com/googleapis/mcp-toolbox/tree/a313b10c4188a33d3a6ed982e9397813bb3a26a0/internal/server/mcp>, <https://github.com/googleapis/mcp-toolbox/blob/a313b10c4188a33d3a6ed982e9397813bb3a26a0/go.mod> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `genai-toolbox`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
