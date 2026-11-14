# Grafana MCP server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `mcp-grafana` |
| Repository | <https://github.com/grafana/mcp-grafana> |
| Package | `binary:GitHub releases; oci:grafana/mcp-grafana` |
| Publisher | grafana (GitHub organisation account) |
| Licence detected by GitHub | Apache-2.0 |
| Upstream status | `active` |
| Latest release | v2.3.0 (2026-11-10) |
| Commit read | `4f09d9f45d35` on `main` (2026-11-13) |
| GitHub stars | 3668 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C3, C4, C6, C8, C10; partly meets C5, C7; does not meet C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The source repository is public and release v2.3.0 is published from it. The release assets include a Sigstore bundle for the checksums file (`mcp-grafana_2.3.0_checksums.txt.sigstore.json`) and SBOM files.

Source: <https://github.com/grafana/mcp-grafana/releases/tag/v2.3.0> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository, and it describes how to report a vulnerability.

Source: <https://github.com/grafana/mcp-grafana/security/policy> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release v2.3.0 is dated 2026-11-10; the newest commit on `main` is dated 2026-11-13; GitHub reports the last push on 2026-11-13.

Source: <https://api.github.com/repos/grafana/mcp-grafana>, <https://github.com/grafana/mcp-grafana/releases/tag/v2.3.0>, <https://github.com/grafana/mcp-grafana/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/grafana/mcp-grafana/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Write tools are on unless `--disable-write` is set; several tool categories are off by default. Quoted: “The `--disable-write` flag provides a way to run the MCP server in read-only mode, preventing any write operations to your Grafana instance.”.

Source: <https://github.com/grafana/mcp-grafana/blob/4f09d9f45d352c8e92870bdfe75bf76af416e35f/README.md?plain=1#L584> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The service-account token is supplied through an environment variable. Quoted: “"GRAFANA_SERVICE_ACCOUNT_TOKEN": "<your service account token>"”.

Source: <https://github.com/grafana/mcp-grafana/blob/4f09d9f45d352c8e92870bdfe75bf76af416e35f/README.md?plain=1#L25> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: partly meets

Anonymous usage statistics are documented as on by default, with documented ways to turn them off. Quoted: “**Reporting is enabled by default**. To opt out, set `--usage-stats=disabled`, `GRAFANA_USAGE_STATS=disabled`, or `DO_NOT_TRACK=1`.”.

Source: <https://github.com/grafana/mcp-grafana/blob/4f09d9f45d352c8e92870bdfe75bf76af416e35f/README.md?plain=1#L1302> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`go.sum`) and an update configuration (`renovate.json`) are committed.

Source: <https://github.com/grafana/mcp-grafana/blob/4f09d9f45d352c8e92870bdfe75bf76af416e35f/go.sum>, <https://github.com/grafana/mcp-grafana/blob/4f09d9f45d352c8e92870bdfe75bf76af416e35f/renovate.json> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/grafana/mcp-grafana/blob/4f09d9f45d352c8e92870bdfe75bf76af416e35f/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: go-sdk v1.8.0 in go.mod. Lower-bound version v1.8.0 of github.com/modelcontextprotocol/go-sdk was published on 2026-09-04, within the 12 months before 2026-11-14.

Source: <https://github.com/grafana/mcp-grafana/blob/4f09d9f45d352c8e92870bdfe75bf76af416e35f/go.mod?plain=1#L24>, <https://proxy.golang.org/github.com/modelcontextprotocol/go-sdk/@v/v1.8.0.info> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `mcp-grafana`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
