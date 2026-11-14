# Plainproof: MCP server review dataset

A dated, sourced review of 37 widely used Model Context Protocol (MCP) servers, written for people who have to decide which servers their organisation allows.

For each server the dataset records ten findings, each measured against a published criterion and each linked to the page it was read from: the project's own repository, documentation, releases, security policy, advisories or package-registry record. Nothing else is used.

**Version 0.2. All entries verified 2026-11-14.**

## What is in it

| Path | What it is |
| --- | --- |
| [`METHODOLOGY.md`](METHODOLOGY.md) | The ten criteria, what counts as a source, how a result is worded and how results are grouped. Read this first. |
| `servers/<slug>.json` | One entry per server: the ten findings with sources and verification dates, the project's published advisories, upstream status. This is the source of each entry. |
| `servers/<slug>.md` | The same entry as a readable page, generated from the JSON. |
| `allowlist.json` | Every entry in one file, with the criteria and the grouping rule. |
| `allowlist.csv` | One row per server, one column per criterion, for spreadsheets and policy tooling. |
| [`CONTESTING.md`](CONTESTING.md) | How to dispute or update a finding. |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed between versions, entry by entry. |
| `build_export.py` | Validates the entries, regenerates the pages and the two exports. Standard-library Python. |

## What a finding looks like

> **C3. Maintenance status: does not meet.** The repository is archived (read-only) on GitHub. The npm record marks the package deprecated. […] Source: <link>, verified 2026-11-14.

Each entry then carries one sentence that sums up its ten results, for example:

> As of 2026-11-14: meets C1, C2, C3, C4, C6, C7, C8, C10; partly meets C5; does not meet C9.

For filtering, entries are placed in one of three groups, computed from the ten results by a fixed rule ([METHODOLOGY.md, section 5](METHODOLOGY.md#5-how-an-outcome-is-worded-and-grouped)):

| Group | Meaning | Entries |
| --- | --- | ---: |
| `criteria-met` | No criterion unmet, no open published advisory, at most four criteria partly met. | 14 |
| `criteria-partly-met` | Everything between the other two groups. | 17 |
| `criteria-not-met` | Provenance, maintenance or advisory criterion unmet, or three or more criteria unmet. | 6 |

A group is a summary of findings on a date. It is not a rating of a project and not a recommendation to use or avoid it.

## How it is made

1. The set of servers was fixed in August 2026 from public popularity lists (METHODOLOGY.md, section 3).
2. On the verification date, each project's repository metadata, release list, registry record, security policy, published advisories and README are fetched and read. Repository files are read at a specific commit, and that commit is recorded.
3. Each of the ten criteria is answered from those pages only. Where a finding depends on wording, the wording is quoted. Where a finding is that something is absent, the files and search terms are listed.
4. Entries are compiled with AI assistance. Quotations are checked mechanically against the fetched text before an entry is written, and `build_export.py` refuses to build if a finding lacks a source or a verification date, or if a group does not follow from the rule.

## What it is not

- **Not a scanner.** No code was executed, no dependency or vulnerability scan was run, no network traffic was observed.
- **Not an audit of source code.** Several criteria describe what the documentation says, not what the software does.
- **Not a certification and not a guarantee.** Meeting every criterion does not make a server safe; missing one does not make it unsafe. The criteria are a short, fixed checklist, not a complete security assessment.
- **Not current after its date.** It is a snapshot. Releases, patches, renames and archiving happen every week. Check the `verified` date, and check the project yourself before you rely on a finding.
- **Not a statement about people.** Findings describe public pages. They say nothing about the intent, competence or reliability of anyone who maintains a project.
- **Not complete.** A server that is not listed has not been reviewed. That is all its absence means.

## Using the exports

- **As input to your own allowlist review.** Start from the findings and their sources instead of from a blank page. Re-check C3 (maintenance) and C4 (advisories) on the day you decide; they change fastest.
- **As a filter.** `allowlist.csv` has one column per criterion (`meets`, `partly meets`, `does not meet`) and an `outcome` column with the group. Filter on the criteria your organisation cares about rather than on the group alone.
- **In policy tooling.** `allowlist.json` carries the same data with sources. The `outcome` field is one of `criteria-met`, `criteria-partly-met`, `criteria-not-met`. How those map onto an allow or deny list is your decision; the dataset does not make it for you.
- **Pin what you approve.** Findings refer to the latest release on the verification date (`latest_release`). Commands such as `npx -y <package>` or `uvx <package>` install whatever is newest.

To rebuild after editing an entry:

```
python build_export.py --check   # validate only
python build_export.py           # regenerate servers/*.md, allowlist.json, allowlist.csv
```

## Disputing or updating a finding

If you maintain a listed project, or you have simply spotted an error or a change, open an issue: <https://github.com/plainproof/mcp-server-findings/issues/new>. [CONTESTING.md](CONTESTING.md) says what to include and what happens next. Corrections are made in the open and recorded in the changelog. There is no fee, no listing charge and no paid way to change a result.

## Licence

- **Data and text** (everything except `build_export.py`): [Creative Commons Attribution-ShareAlike 4.0 International](LICENSE) (CC BY-SA 4.0). Attribute as "Plainproof MCP server review dataset, <version>, <verified date>" with a link to this repository.
- **Code** (`build_export.py`): [MIT](LICENSE-CODE).
- Short quotations from third-party documentation are reproduced for the purpose of identifying what a finding refers to; they remain the property of their authors and are not covered by the licence above. Project and product names are the trademarks of their owners and are used only to identify the software reviewed.

## Disclaimer

The dataset is provided as is, without warranty of any kind. It records what public pages said on a stated date and is not security advice. Verify against current sources before acting on it.
