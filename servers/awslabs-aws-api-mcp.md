# AWS API MCP Server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `awslabs-aws-api-mcp` |
| Repository | <https://github.com/awslabs/mcp> (`src/aws-api-mcp-server`) |
| Package | `pypi:awslabs.aws-api-mcp-server` |
| Publisher | awslabs (GitHub organisation account) |
| Licence detected by GitHub | Apache-2.0 |
| Upstream status | `superseded-upstream` - The README says the server is superseded by another AWS MCP server and that a deprecation notice is shown at start-up; releases continued (1.6.0 on 2026-10-27). Quoted: “This MCP server is superseded by the official [AWS MCP server]”. |
| Latest release | 1.6.0 (2026-10-27) |
| Commit read | `5d58a6adaf89` on `main` (2026-11-13) |
| GitHub stars | 9919 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-met` |

## Outcome

As of 2026-11-14: meets C1, C2, C4, C6, C8, C9, C10; partly meets C3, C5, C7.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The PyPI record for awslabs.aws-api-mcp-server 1.6.0 links the repository, and PyPI holds a provenance attestation for the release naming `awslabs/mcp` (workflow `release.yml`) as publisher.

Source: <https://pypi.org/pypi/awslabs.aws-api-mcp-server/json>, <https://pypi.org/integrity/awslabs.aws-api-mcp-server/1.6.0/awslabs_aws_api_mcp_server-1.6.0-py3-none-any.whl/provenance> (verified 2026-11-14)

### C2. Published security policy: meets

GitHub shows a security policy for the repository, and it describes how to report a vulnerability.

Source: <https://github.com/awslabs/mcp/security/policy> (verified 2026-11-14)

### C3. Maintenance status: partly meets

The repository is not archived and releases continue, but the README says the server is superseded by a successor and describes a deprecation notice shown at start-up. Quoted: “This MCP server is superseded by the official [AWS MCP server]”; “suppresses the deprecation notice that is otherwise shown at server startup”. Latest release 1.6.0 is dated 2026-10-27; the newest commit on `main` is dated 2026-11-13; GitHub reports the last push on 2026-11-13.

Source: <https://github.com/awslabs/mcp/blob/5d58a6adaf89a056d0c14e732593dceb12e633df/src/aws-api-mcp-server/README.md?plain=1#L4>, <https://github.com/awslabs/mcp/blob/5d58a6adaf89a056d0c14e732593dceb12e633df/src/aws-api-mcp-server/README.md?plain=1#L225>, <https://api.github.com/repos/awslabs/mcp>, <https://pypi.org/pypi/awslabs.aws-api-mcp-server/json> (verified 2026-11-14)

### C4. Published advisories: meets

4 advisories are published in the repository's advisory list for awslabs.aws-api-mcp-server; each names a patched version at or below the latest release (1.6.0). Most recent: GHSA-4wq9-grf3-qg2p (high, published 2026-11-10, patched in 1.5.1).

Source: <https://github.com/awslabs/mcp/security/advisories>, <https://github.com/awslabs/mcp/security/advisories/GHSA-4wq9-grf3-qg2p> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Mutating AWS operations are available by default; the README documents a read-only switch that is off by default. Quoted: “`READ_OPERATIONS_ONLY` | ❌ No | `"false"` | When set to "true", restricts execution to read-only operations only.”.

Source: <https://github.com/awslabs/mcp/blob/5d58a6adaf89a056d0c14e732593dceb12e633df/src/aws-api-mcp-server/README.md?plain=1#L213> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

Credentials come from the AWS credential chain, a named profile or environment variables. Quoted: “Use environment variables to configure AWS credentials”.

Source: <https://github.com/awslabs/mcp/blob/5d58a6adaf89a056d0c14e732593dceb12e633df/src/aws-api-mcp-server/README.md?plain=1#L215> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: partly meets

Additional telemetry to AWS is documented as on by default, with an environment variable to turn it off. Quoted: “`AWS_API_MCP_TELEMETRY` | ❌ No | `"true"` | Allow sending additional telemetry data to AWS related to the server configuration.”.

Source: <https://github.com/awslabs/mcp/blob/5d58a6adaf89a056d0c14e732593dceb12e633df/src/aws-api-mcp-server/README.md?plain=1#L216> (verified 2026-11-14)

### C8. Dependency management files: meets

A lockfile (`src/aws-api-mcp-server/uv.lock`) and an update configuration (`.github/dependabot.yml`) are committed.

Source: <https://github.com/awslabs/mcp/blob/5d58a6adaf89a056d0c14e732593dceb12e633df/src/aws-api-mcp-server/uv.lock>, <https://github.com/awslabs/mcp/blob/5d58a6adaf89a056d0c14e732593dceb12e633df/.github/dependabot.yml> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: meets

The README has a section on prompt injection and untrusted data with recommendations. Quoted: “**Do not connect this MCP server to data sources with untrusted data**”.

Source: <https://github.com/awslabs/mcp/blob/5d58a6adaf89a056d0c14e732593dceb12e633df/src/aws-api-mcp-server/README.md?plain=1#L312> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: fastmcp<4.0,>=3.4.3 (also mcp<2.0,>=1.23.0). Lower-bound version 3.4.3 of fastmcp (PyPI) was published on 2026-07-05, within the 12 months before 2026-11-14.

Source: <https://pypi.org/pypi/awslabs.aws-api-mcp-server/json>, <https://pypi.org/pypi/fastmcp/json> (verified 2026-11-14)

## Advisories published by the project

- GHSA-4wq9-grf3-qg2p / CVE-2026-125271 (high, published 2026-11-10): AWS API MCP Server Security Policy Bypass via Incorrect Operation Name Normalization. Affected: >= 0.2.13 AND < 1.5.1. Patched: 1.5.1. <https://github.com/awslabs/mcp/security/advisories/GHSA-4wq9-grf3-qg2p>
- GHSA-4prq-p2x5-w9fh / CVE-2026-115413 (high, published 2026-10-27): AWS API MCP Server OAuth Token Audience Validation Bypass. Affected: >=1.3.0 AND <1.6.0. Patched: 1.6.0. <https://github.com/awslabs/mcp/security/advisories/GHSA-4prq-p2x5-w9fh>
- GHSA-29w2-fq35-v728 / CVE-2026-16584 (high, published 2026-07-23): AWS API MCP Server Security Policy Bypass via Startup Initialization Failure. Affected: >= 0.2.13 AND < 1.3.47. Patched: 1.3.47. <https://github.com/awslabs/mcp/security/advisories/GHSA-29w2-fq35-v728>
- GHSA-2cpp-j2fc-qhp7 / CVE-2026-4270 (medium, published 2026-03-16): AWS API MCP File Access Restriction Bypass. Affected: >= 0.2.14, < 1.3.9. Patched: 1.3.9. <https://github.com/awslabs/mcp/security/advisories/GHSA-2cpp-j2fc-qhp7>

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `awslabs-aws-api-mcp`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
