# Task Master

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `claude-task-master` |
| Repository | <https://github.com/eyaltoledano/claude-task-master> |
| Package | `npm:task-master-ai` |
| Publisher | eyaltoledano (GitHub user account) |
| Licence detected by GitHub | NOASSERTION |
| Upstream status | `inactive` - No release and no repository activity in the 180 days before 2026-11-14. |
| Latest release | 0.43.1 (2026-03-31) |
| Commit read | `c0c98d367c55` on `main` (2026-04-23) |
| GitHub stars | 28359 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-not-met` |

## Outcome

As of 2026-11-14: meets C1, C4, C6, C7, C10; partly meets C2, C5, C8; does not meet C3, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for task-master-ai@0.43.1 names the repository `git+https://github.com/eyaltoledano/claude-task-master.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/task-master-ai/latest> (verified 2026-11-14)

### C2. Published security policy: partly meets

GitHub's security-policy page for the repository says "No security policy detected"; the same page offers private vulnerability reporting ("Report a vulnerability").

Source: <https://github.com/eyaltoledano/claude-task-master/security/policy> (verified 2026-11-14)

### C3. Maintenance status: does not meet

The repository is not archived, but there has been neither a release nor repository activity in the 180 days before 2026-11-14. Latest release 0.43.1 is dated 2026-03-31; the newest commit on `main` is dated 2026-04-23; GitHub reports the last push on 2026-04-28.

Source: <https://api.github.com/repos/eyaltoledano/claude-task-master>, <https://registry.npmjs.org/task-master-ai/latest>, <https://github.com/eyaltoledano/claude-task-master/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/eyaltoledano/claude-task-master/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

All tools are loaded by default; the README documents an environment variable that loads a subset. Quoted: “By default, all 36 tools are loaded (~21,000 tokens) to maintain backward compatibility with existing installations.”.

Source: <https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/README.md?plain=1#L301> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

Provider API keys are supplied in the MCP client's `env` block. Quoted: “"ANTHROPIC_API_KEY": "YOUR_ANTHROPIC_API_KEY_HERE"”.

Source: <https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/README.md?plain=1#L136> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection; the documented function calls the model providers the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`package-lock.json`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/package-lock.json>, <https://github.com/eyaltoledano/claude-task-master/tree/c0c98d367c55296bfe69e65680625b6db437af02> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/eyaltoledano/claude-task-master/blob/c0c98d367c55296bfe69e65680625b6db437af02/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: fastmcp ^3.23.1. Lower-bound version 3.23.1 of fastmcp (npm) was published on 2025-11-17, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/task-master-ai/latest>, <https://registry.npmjs.org/fastmcp> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `claude-task-master`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
