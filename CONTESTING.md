# Disputing or updating a finding

Every entry in this dataset describes a named project. If you maintain one of them, or you have noticed that a finding is wrong or out of date, this page says how to get it changed.

## Who can ask

Anyone. You do not need to be a maintainer, and maintainers get no different treatment from anyone else. There is no fee and no paid route to a different result.

## How to ask

Open an issue on the dataset repository:

<https://github.com/plainproof/mcp-server-findings/issues/new>

Give the issue a title of the form `finding: <slug> <criterion>`, for example `finding: example-server C5`.

## What to include

1. **The entry and the criterion.** The slug (the file name under `servers/`) and the criterion number, C1 to C10.
2. **What is wrong.** One or two sentences: the finding misreads the source, the source has changed, the wrong source was read, or the criterion was applied incorrectly.
3. **A link to the project's own public material that shows it.** A file in the repository (ideally a permalink to a commit), a release page, the security policy, a published advisory, the registry record, or the project's documentation site. This matters: findings rest only on the project's own public material ([METHODOLOGY.md, section 2](METHODOLOGY.md#2-sources)), so a correction has to rest on it too. If the material does not exist yet, publishing it (for example adding a `SECURITY.md`, or documenting a read-only option) and then linking it is a perfectly good way to change a finding.
4. **The date you checked**, if the point is that something has changed since the entry's `verified` date.

You do not need to argue about the group an entry falls in. Groups are computed from the ten results by a fixed rule; if a result changes, the group follows.

If you think a criterion itself is badly defined, say so in an issue titled `methodology: <criterion>`. That is a different kind of request and is handled as a change to METHODOLOGY.md.

## What happens next

- **Every issue is read, and reviewed within 15 working days of being opened.** The linked material is read on the day of review.
  - If it shows the finding is wrong or out of date, the entry is corrected, its `verified` date is updated, the exports are regenerated, and the change is recorded in [CHANGELOG.md](CHANGELOG.md) with a link to the issue. The issue is closed with a link to the change.
  - If the material does not support a change, the issue is closed with the reason and the source that was read.
- **While an issue is open**, the entry page carries a line saying that the finding is disputed and linking to the issue, so readers can see both positions.
- **Nothing is removed quietly.** Entries are corrected or annotated, not silently deleted. A corrected finding stays visible in the changelog.

This is a commitment to read what you send and to correct what is wrong. If the 15 working days pass without a result, say so in the issue; that is a defect in the process and will be treated as one.

## Errors in general

An error that makes a project look worse than its own material supports is treated as the most urgent kind and is corrected first.

## What cannot be handled here

- **Unpublished vulnerabilities.** Do not describe an undisclosed vulnerability in a public issue on this repository. Report it to the affected project through its own security policy. This dataset only reflects advisories after the project has published them.
- **Requests to be removed because a finding is unwelcome.** An entry that is accurate and sourced stays. An entry that is inaccurate gets fixed.
- **Requests to add a server.** Welcome, but they go on a backlog; open an issue titled `add: <repository>`.
