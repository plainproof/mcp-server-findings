# Qdrant MCP server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-server-qdrant` |
| Repository | <https://github.com/qdrant/mcp-server-qdrant> |
| Package | `pypi:mcp-server-qdrant` |
| Publisher | qdrant (GitHub organisation account) |
| Licence detected by GitHub | Apache-2.0 |
| Upstream status | `active` |
| Latest release | 0.8.1 (2025-12-10) |
| Commit read | `9cfd5f1584e4` on `master` (2026-11-10) |
| GitHub stars | 1570 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C4, C6, C7, C8; partly meets C1, C2, C3, C5, C10; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: partly meets

The PyPI record for mcp-server-qdrant 0.8.1 lists no project or repository URL; the repository's `pyproject.toml` declares the package name `mcp-server-qdrant`. PyPI holds no provenance attestation for the release (the integrity record returned HTTP 404).

Source: <https://pypi.org/pypi/mcp-server-qdrant/json>, <https://github.com/qdrant/mcp-server-qdrant/blob/9cfd5f1584e4de45517c335c2bb69f7a53e44055/pyproject.toml>, <https://pypi.org/integrity/mcp-server-qdrant/0.8.1/mcp_server_qdrant-0.8.1-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: partly meets

GitHub's security-policy page for the repository says "No security policy detected"; the same page offers private vulnerability reporting ("Report a vulnerability").

Source: <https://github.com/qdrant/mcp-server-qdrant/security/policy> (verified 2026-11-14)

### C3. Maintenance status: partly meets

The repository is not archived. The latest release is 339 days old (more than 180); repository activity falls within the last 180 days. Latest release 0.8.1 is dated 2025-12-10; the newest commit on `master` is dated 2026-11-10; GitHub reports the last push on 2026-11-10.

Source: <https://api.github.com/repos/qdrant/mcp-server-qdrant>, <https://pypi.org/pypi/mcp-server-qdrant/json>, <https://github.com/qdrant/mcp-server-qdrant/commits/master> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/qdrant/mcp-server-qdrant/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

The store tool is available unless read-only mode is set. Quoted: “`QDRANT_READ_ONLY` | Enable read-only mode (disables `qdrant-store` tool) | `false` |”.

Source: <https://github.com/qdrant/mcp-server-qdrant/blob/9cfd5f1584e4de45517c335c2bb69f7a53e44055/README.md?plain=1#L55> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The API key is supplied through an environment variable. Quoted: “`QDRANT_API_KEY` | API key for the Qdrant server”.

Source: <https://github.com/qdrant/mcp-server-qdrant/blob/9cfd5f1584e4de45517c335c2bb69f7a53e44055/README.md?plain=1#L47> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/qdrant/mcp-server-qdrant/blob/9cfd5f1584e4de45517c335c2bb69f7a53e44055/README.md> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`uv.lock`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/qdrant/mcp-server-qdrant/blob/9cfd5f1584e4de45517c335c2bb69f7a53e44055/uv.lock>, <https://github.com/qdrant/mcp-server-qdrant/blob/9cfd5f1584e4de45517c335c2bb69f7a53e44055/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/qdrant/mcp-server-qdrant/blob/9cfd5f1584e4de45517c335c2bb69f7a53e44055/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: partly meets

Declared MCP library: fastmcp==2.7.0. Lower-bound version 2.7.0 of fastmcp (PyPI) was published on 2025-06-05, between 12 and 24 months before 2026-11-14.

Source: <https://pypi.org/pypi/mcp-server-qdrant/json>, <https://pypi.org/pypi/fastmcp/json> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-server-qdrant`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
