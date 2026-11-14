# Firecrawl MCP Server

> Findings as of 2026-11-14, read from the project's own public material and measured against the criteria in [METHODOLOGY.md](../METHODOLOGY.md). This is a point-in-time reading, not a scan, a certification or a guarantee, and it says nothing about the people who maintain the project. To dispute or update a finding, see [CONTESTING.md](../CONTESTING.md).

| Field | Value |
| --- | --- |
| Slug | `firecrawl-mcp-server` |
| Repository | <https://github.com/firecrawl/firecrawl-mcp-server> |
| Package | `npm:firecrawl-mcp; remote:https://mcp.firecrawl.dev/v2/mcp` |
| Publisher | firecrawl (GitHub organisation account) |
| Licence detected by GitHub | MIT |
| Upstream status | `active` |
| Latest release | 3.40.0 (2026-11-12) |
| Commit read | `a3d0fbe920d8` on `main` (2026-11-13) |
| GitHub stars | 7817 |
| Verified | 2026-11-14 |
| Outcome group | `criteria-partly-met` |

## Outcome

As of 2026-11-14: meets C1, C3, C4, C6, C10; partly meets C5, C7, C8; does not meet C2, C9.

The group above is computed from these ten results by the rule in [METHODOLOGY.md, section 5](../METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped).

## Findings

### C1. Source and release provenance: meets

The npm record for firecrawl-mcp@3.40.0 names the repository `git+https://github.com/firecrawl/firecrawl-mcp-server.git` and carries a provenance attestation (`dist.attestations`).

Source: <https://registry.npmjs.org/firecrawl-mcp/latest> (verified 2026-11-14)

### C2. Published security policy: does not meet

GitHub's security-policy page for the repository says "No security policy detected" and offers no private vulnerability reporting; the README names no channel for security reports (searched for: security@, vulnerability, responsible disclosure, report security).

Source: <https://github.com/firecrawl/firecrawl-mcp-server/security/policy>, <https://github.com/firecrawl/firecrawl-mcp-server/blob/a3d0fbe920d800c257f118a487b87773ff5c1320/README.md> (verified 2026-11-14)

### C3. Maintenance status: meets

The repository is not archived and the package is not marked deprecated. Latest release 3.40.0 is dated 2026-11-12; the newest commit on `main` is dated 2026-11-13; GitHub reports the last push on 2026-11-14.

Source: <https://api.github.com/repos/firecrawl/firecrawl-mcp-server>, <https://registry.npmjs.org/firecrawl-mcp/latest>, <https://github.com/firecrawl/firecrawl-mcp-server/commits/main> (verified 2026-11-14)

### C4. Published advisories: meets

No advisory is published in the repository's advisory list.

Source: <https://github.com/firecrawl/firecrawl-mcp-server/security/advisories> (verified 2026-11-14)

### C5. Documented scope controls: partly meets

Scraping, crawling and browser interaction are available by default; the README documents a `CLOUD_SERVICE` mode with stricter defaults. Quoted: “`CLOUD_SERVICE=true` serves the tools over streamable HTTP on `PORT` (default `3000`, bound to `0.0.0.0`) with stricter defaults”.

Source: <https://github.com/firecrawl/firecrawl-mcp-server/blob/a3d0fbe920d800c257f118a487b87773ff5c1320/README.md?plain=1#L320> (verified 2026-11-14)

### C6. Credential handling in the documented setup: meets

The API key is supplied through an environment variable, or OAuth on the hosted endpoint. Quoted: “env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp”.

Source: <https://github.com/firecrawl/firecrawl-mcp-server/blob/a3d0fbe920d800c257f118a487b87773ff5c1320/README.md?plain=1#L96> (verified 2026-11-14)

### C7. Telemetry and outbound data, as documented: partly meets

The documented function is retrieving arbitrary web addresses through the Firecrawl API; the README also documents feedback tools that are registered unless opted out. Quoted: “Scrape any URL into clean Markdown”; “**Opt out:** set `FIRECRAWL_NO_SEARCH_FEEDBACK=1`”.

Source: <https://github.com/firecrawl/firecrawl-mcp-server/blob/a3d0fbe920d800c257f118a487b87773ff5c1320/README.md?plain=1#L19> (verified 2026-11-14)

### C8. Dependency management files: partly meets

A lockfile (`pnpm-lock.yaml`) is committed. No Dependabot or Renovate configuration file exists at the paths listed in the methodology.

Source: <https://github.com/firecrawl/firecrawl-mcp-server/blob/a3d0fbe920d800c257f118a487b87773ff5c1320/pnpm-lock.yaml>, <https://github.com/firecrawl/firecrawl-mcp-server/tree/a3d0fbe920d800c257f118a487b87773ff5c1320> (verified 2026-11-14)

### C9. Documentation of untrusted-content risk: does not meet

No statement about prompt injection or untrusted content was found in the files searched. Searched `README.md` for: prompt-injection, untrusted, malicious, attacker, adversarial.

Source: <https://github.com/firecrawl/firecrawl-mcp-server/blob/a3d0fbe920d800c257f118a487b87773ff5c1320/README.md> (verified 2026-11-14)

### C10. Currency of the declared MCP library: meets

Declared MCP library: @modelcontextprotocol/server 2.3.1. Lower-bound version 2.3.1 of @modelcontextprotocol/server (npm) was published on 2026-10-05, within the 12 months before 2026-11-14.

Source: <https://registry.npmjs.org/firecrawl-mcp/latest>, <https://registry.npmjs.org/@modelcontextprotocol/server> (verified 2026-11-14)

## Advisories published by the project

None in the repository's advisory list for this server on 2026-11-14.

## Dispute or update this entry

Open an issue at <https://github.com/plainproof/mcp-server-findings/issues/new> with the slug `firecrawl-mcp-server`, the criterion, and a link to the project's own material that shows the finding is wrong or out of date. The process and the response commitment are in [CONTESTING.md](../CONTESTING.md).
