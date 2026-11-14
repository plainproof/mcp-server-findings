# Redis MCP Server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-redis` |
| Repository | <https://github.com/redis/mcp-redis> |
| Package | `pypi:redis-mcp-server; oci:mcp/redis` |
| Publisher | redis (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 0.5.1 (2026-08-05) |
| Commit read | `d66c5ea0172e` on `main` (2026-11-11) |
| GitHub stars | 642 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C1, C3, C4, C7, C8, C10; partly meets C5, C6; does not meet C2, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The PyPI record for redis-mcp-server 0.5.1 links the repository, and PyPI holds a provenance attestation for the release naming `redis/mcp-redis` (workflow `release.yml`) as publisher.

Source: <https://pypi.org/pypi/redis-mcp-server/json>, <https://pypi.org/integrity/redis-mcp-server/0.5.1/redis_mcp_server-0.5.1-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: does not meet

GitHub's security-policy page for the repository says "No security policy detected" and offers no private vulnerability reporting; the README names no channel for security reports (searched for: security@, vulnerability, responsible disclosure, report security).

Source: <https://github.com/redis/mcp-redis/security/policy>, <https://github.com/redis/mcp-redis/blob/d66c5ea0172e0991a98c0f13c0f880246c93b2a5/README.md> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 0.5.1 is dated 2026-08-05; the newest commit on `main` is dated 2026-11-11; GitHub reports the last push on 2026-11-11.

Source: <https://api.github.com/repos/redis/mcp-redis>, <https://pypi.org/pypi/redis-mcp-server/json>, <https://github.com/redis/mcp-redis/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/redis/mcp-redis/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

No server-side read-only switch is described; the README documents restricting access through a Redis ACL user. Searched `README.md` for: --read-only, READ_ONLY, read-only mode. Quoted: “You can configure Redis ACL to restrict the access to the Redis database. For example, to create a read-only user:”.

Source: <https://github.com/redis/mcp-redis/blob/d66c5ea0172e0991a98c0f13c0f880246c93b2a5/README.md?plain=1#L293>, <https://github.com/redis/mcp-redis/blob/d66c5ea0172e0991a98c0f13c0f880246c93b2a5/README.md> (verified 2026-11-14)

### C6. Credential handling in the documented setup: partly meets

Both command-line arguments and environment variables are documented; the connection address format shown can carry a password. Quoted: “The Redis MCP Server can be configured in two ways: via command line arguments or via environment variables.”; “redis://user:secret@localhost:6379/0?foo=bar&qux=baz”.

Source: <https://github.com/redis/mcp-redis/blob/d66c5ea0172e0991a98c0f13c0f880246c93b2a5/README.md?plain=1#L288> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: meets

The README contains no reference to telemetry or usage collection, and the documented function contacts only the service the user configures. Searched `README.md` for: telemetry, usage statistics, usage stats, we collect, data collection, opt-out, posthog.

Source: <https://github.com/redis/mcp-redis/blob/d66c5ea0172e0991a98c0f13c0f880246c93b2a5/README.md> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`uv.lock`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/redis/mcp-redis/blob/d66c5ea0172e0991a98c0f13c0f880246c93b2a5/uv.lock>, <https://github.com/redis/mcp-redis/blob/d66c5ea0172e0991a98c0f13c0f880246c93b2a5/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/redis/mcp-redis/blob/d66c5ea0172e0991a98c0f13c0f880246c93b2a5/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: mcp[cli]<2,>=1.26.0. Lower-bound version 1.26.0 of mcp (PyPI) was published on 2026-01-24, within the 12 months before 2026-11-14.

Source: <https://pypi.org/pypi/redis-mcp-server/json>, <https://pypi.org/pypi/mcp/json> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-redis`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
