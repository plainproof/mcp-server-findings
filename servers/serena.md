# Serena

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `serena` |
| Repository | <https://github.com/oraios/serena> |
| Package | `pypi:serena-agent` |
| Publisher | oraios (GitHub organisation account) |
| Licence detected by GitHub | NOASSERTION |
| Upstream status | `active` |
| Latest release | 2.1.0 (2026-10-19) |
| Commit read | `6b39542bb108` on `main` (2026-11-14) |
| GitHub stars | 31374 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C3, C4, C6, C7, C9, C10; partly meets C1, C2, C5, C8.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The PyPI record for serena-agent 2.1.0 links the repository. PyPI holds no provenance attestation for the release (the integrity record returned HTTP 404).

Source: <https://pypi.org/pypi/serena-agent/json>, <https://pypi.org/integrity/serena-agent/2.1.0/serena_agent-2.1.0-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: partly meets

GitHub's security-policy page for the repository says "No security policy detected"; the same page offers private vulnerability reporting ("Report a vulnerability").

Source: <https://github.com/oraios/serena/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 2.1.0 is dated 2026-10-19; the newest commit on `main` is dated 2026-11-14; GitHub reports the last push on 2026-11-14.

Source: <https://api.github.com/repos/oraios/serena>, <https://pypi.org/pypi/serena-agent/json>, <https://github.com/oraios/serena/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

3 advisories are published in the repository's advisory list; each names a patched version at or below the latest release (2.1.0). Most recent: GHSA-pp6p-xvxf-8hhx (high, published 2026-10-14, patched in 2.0.0).

Source: <https://github.com/oraios/serena/security/advisories>, <https://github.com/oraios/serena/security/advisories/GHSA-pp6p-xvxf-8hhx> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

A shell-command tool and file-editing tools are documented; the README says such tools are typically disabled by default inside agentic harnesses, and the security documentation recommends restricting the allowed tools through configuration. Quoted: “**`execute_shell_command`** – run shell commands (e.g. builds, tests, linters)”; “When Serena is used inside an agentic harness such as Claude Code or Codex, these tools are typically disabled by default,”; “restrict the set of allowed tools via the configuration”.

Source: <https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/README.md?plain=1#L193>, <https://oraios.github.io/serena/02-usage/070_security.html> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The documented setup takes no credential. Searched `README.md` for: API_KEY, _TOKEN\b, password.

Source: <https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/README.md> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`uv.lock`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/uv.lock>, <https://github.com/oraios/serena/tree/6b39542bb108ce77901072deac699d770b302d52> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: meets

The project's security documentation says the contents of a repository can influence the model, documents a project-trust setting, and recommends sandboxing for repositories that are not trusted. Quoted: “the repository’s contents can influence the LLM”; “If a repository is not trustworthy, sandboxing is the answer, not the trust configuration.”.

Source: <https://oraios.github.io/serena/02-usage/070_security.html> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: mcp==2.2.0. Lower-bound version 2.2.0 of mcp (PyPI) was published on 2026-09-07, within the 12 months before 2026-11-14.

Source: <https://pypi.org/pypi/serena-agent/json>, <https://pypi.org/pypi/mcp/json> (verified 2026-11-14)

## Advisories published by the project

- GHSA-pp6p-xvxf-8hhx (high, published 2026-10-14): Remote Code Execution via insecure pickle deserialization of LSP symbol cache (malicious repository → RCE on project activation). Affected: <= 1.7.1. Patched: 2.0.0. <https://github.com/oraios/serena/security/advisories/GHSA-pp6p-xvxf-8hhx>
- GHSA-pp25-4cg4-qcr9 (critical, published 2026-08-09): Server-Side Template Injection (SSTI) in mode/context prompt rendering → RCE on project activation, bypassing `trusted_project_path_patterns`. Affected: <= 1.6.1. Patched: 1.7.0. <https://github.com/oraios/serena/security/advisories/GHSA-pp25-4cg4-qcr9>
- GHSA-37h2-6p4f-mp3q / CVE-2026-49471 (high, published 2026-07-01): Unauthenticated Flask dashboard on fixed port enables DNS rebinding → memory poisoning → RCE. Affected: < v1.5.2. Patched: v1.5.2+. <https://github.com/oraios/serena/security/advisories/GHSA-37h2-6p4f-mp3q>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `serena`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
