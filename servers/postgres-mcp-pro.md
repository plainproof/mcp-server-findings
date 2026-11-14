# Postgres MCP Pro

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `postgres-mcp-pro` |
| Repository | <https://github.com/crystaldba/postgres-mcp> |
| Package | `pypi:postgres-mcp; oci:crystaldba/postgres-mcp` |
| Publisher | crystaldba (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 0.3.0 (2025-05-16) |
| Commit read | `15c8e3335354` on `main` (2026-08-16) |
| GitHub stars | 3475 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C4, C7; partly meets C1, C3, C5, C6, C8, C9, C10; does not meet C2.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The PyPI record for postgres-mcp 0.3.0 lists no project or repository URL; the repository's `pyproject.toml` declares the package name `postgres-mcp`. PyPI holds no provenance attestation for the release (the integrity record returned HTTP 404).

Source: <https://pypi.org/pypi/postgres-mcp/json>, <https://github.com/crystaldba/postgres-mcp/blob/15c8e33353546148acc2d8bd784551cf3905d1e2/pyproject.toml>, <https://pypi.org/integrity/postgres-mcp/0.3.0/postgres_mcp-0.3.0-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: does not meet

GitHub's security-policy page for the repository says "No security policy detected" and offers no private vulnerability reporting; the README names no channel for security reports (searched for: security@, vulnerability, responsible disclosure, report security).

Source: <https://github.com/crystaldba/postgres-mcp/security/policy>, <https://github.com/crystaldba/postgres-mcp/blob/15c8e33353546148acc2d8bd784551cf3905d1e2/README.md> (verified 2026-11-14)

### C3. Maintenance status: partly meets

The repository is not archived. The latest release is 547 days old (more than 180); repository activity falls within the last 180 days. Latest release 0.3.0 is dated 2025-05-16; the newest commit on `main` is dated 2026-08-16; GitHub reports the last push on 2026-08-17.

Source: <https://api.github.com/repos/crystaldba/postgres-mcp>, <https://pypi.org/pypi/postgres-mcp/json>, <https://github.com/crystaldba/postgres-mcp/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/crystaldba/postgres-mcp/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The README documents a restricted (read-only) access mode; its configuration examples use the unrestricted mode. Quoted: “To use restricted mode, replace `--access-mode=unrestricted` with `--access-mode=restricted` in the configuration examples above.”.

Source: <https://github.com/crystaldba/postgres-mcp/blob/15c8e33353546148acc2d8bd784551cf3905d1e2/README.md?plain=1#L227> (verified 2026-11-14)

### C6. Credential handling in the documented setup: partly meets

The configuration examples pass the connection address through an environment variable; the development instructions pass it as a command-line argument. Quoted: “"DATABASE_URI": "postgresql://username:password@localhost:5432/dbname"”; “uv run postgres-mcp "postgres://user:password@localhost:5432/dbname"”.

Source: <https://github.com/crystaldba/postgres-mcp/blob/15c8e33353546148acc2d8bd784551cf3905d1e2/README.md?plain=1#L144> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/crystaldba/postgres-mcp/blob/15c8e33353546148acc2d8bd784551cf3905d1e2/README.md> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`uv.lock`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/crystaldba/postgres-mcp/blob/15c8e33353546148acc2d8bd784551cf3905d1e2/uv.lock>, <https://github.com/crystaldba/postgres-mcp/tree/15c8e33353546148acc2d8bd784551cf3905d1e2> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: partly meets

The README discusses protecting databases in AI-driven use in general terms; it does not name prompt injection or untrusted content returned by tools. Quoted: “AI amplifies longstanding challenges of protecting databases from a range of threats, ranging from simple mistakes to sophisticated attacks by malicious actors.”.

Source: <https://github.com/crystaldba/postgres-mcp/blob/15c8e33353546148acc2d8bd784551cf3905d1e2/README.md?plain=1#L580> (verified 2026-11-14)

### C10. Currency of the declared MCP library: partly meets

Declared MCP library: mcp[cli]>=1.5.0. Lower-bound version 1.5.0 of mcp (PyPI) was published on 2025-03-21, between 12 and 24 months before 2026-11-14.

Source: <https://pypi.org/pypi/postgres-mcp/json>, <https://pypi.org/pypi/mcp/json> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `postgres-mcp-pro`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
