# Worked example: KubeVirt

ATLAS works with any project. You describe each project in a projects file, and nothing in ATLAS
is tied to one project. This page shows ATLAS on one real project, KubeVirt, so you can see what
it reads, what it measures and which parts of the demo are sample data.

## Why KubeVirt

[KubeVirt](https://github.com/kubevirt/kubevirt) is a public open-source project that runs virtual
machines on Kubernetes. It was chosen as the example project because it has a long, public history
of issues, pull requests, releases and CI runs. ATLAS needs that history to rebuild a project as
it stood on a past day and to check its forecasts against what happened next.

KubeVirt is one of two example projects in `deploy/projects.example.toml`. The other, Argo CD, has
live views and reports only. KubeVirt is the project with `evaluation = true`, so the quality checks
run on its data.

## What ATLAS reads from KubeVirt

ATLAS only reads these sources. It never writes to them.

| Source | What ATLAS reads | How | Data label |
|---|---|---|---|
| Issue tracker | Issues, comments, labels, timeline events and edit history of `kubevirt/kubevirt` | GitHub GraphQL and REST, read-only | Real data |
| Git | Commits, pull requests, diffs, release tags and release branches | GitHub REST, read-only | Real data |
| CI | Prow job logs linked from issues | Public storage, read-only | Real data |
| Security scanner | Known vulnerabilities for the Go modules in `go.mod` at a pinned commit | [OSV.dev](https://osv.dev) query API | Real data |
| Architecture graph | Components, owner teams and dependency edges from Go imports and `OWNERS` files | Derived from the repository at a pinned commit | Real data (derived) |

The KubeVirt entry in the example projects file lists the hosts of its CI and links:
`prow.ci.kubevirt.io` (the CI job viewer), `storage.googleapis.com` (where the CI logs are kept)
and `kubevirt.io` (its Go module host), with a few Go and container-image hosts. ATLAS keeps these
host names in text it sends to an AI model and opens links to them. These hosts belong to the
KubeVirt entry only, not to ATLAS.

## The frozen copies

ATLAS works from frozen copies of the project. Each copy shows KubeVirt as it stood at one moment,
and is labelled **Data as of** that date. For example, **Data as of 30 July 2026** is KubeVirt on the
day release v1.9.0 shipped. It holds the issues, code changes and test results that existed on that
day, and nothing that happened later.

The example data has:

- five release closes, v1.5.0 to v1.9.0;
- seven example cases, each a copy of the project at the moment a known past failure was reported;
- test copies of the example cases with the names disguised, which check that ATLAS does not repeat
  an answer from memory.

Committed copies replace person names, handles and emails with stable pseudonyms. Source links and
their origin are kept. Raw fetches stay on the owner's machine and are never committed.

## What the measured numbers mean

ATLAS forecasts which issues the next release will inherit. Forecast accuracy asks one question:
did the forecast name the release blockers in advance?

KubeVirt does not record which issues blocked each release. When the data was checked on
14 November 2026, release-blocker labels existed only for 1.6 (2 issues) and 1.7 (1 issue), none for
1.8 to 1.10, and there were no milestones. So ATLAS uses a stand-in, the *proxy blocker*. An issue
counts as a blocker of a release when one of these is true:

- it is a bug or flaky-test issue whose fix was copied to the release branch between the first beta
  and the release;
- it is a critical-urgent issue that was still open on the day of the release.

One person checks each candidate.

The forecast for a release is made at the close of the release before it, from that close's frozen
copy. An issue reported after that point could not have been named, so it does not count. For the
four scored releases this keeps 36 of 120 candidates. The other 84 are kept in the evaluator files
with the reason they were left out; most were reported after the forecast was made.

- **Recall** is the share of those 36 blockers that the forecast named.
- **Precision** is the share of named issues that turned out to be blockers.

Every forecast accuracy number in ATLAS says, beside the number, that it counts only blockers that
were already open when the forecast was made and that it uses a stand-in. For KubeVirt the reason
for the stand-in comes from the project's `blocker_note` setting. The latest results are on the
**Quality checks** page in ATLAS.

## What was sample data

Some inputs in the demo are made up for the demo and labelled as sample data. ATLAS never counts
sample data as a real result.

| Input | What it holds |
|---|---|
| Kubernetes events | Cluster events for environment-failure cases |
| Telemetry | Error-rate series |
| Capacity | Role ids, skill tags and availability; never names |

Everything else on this page is real public data from KubeVirt.

## Using your own project

To point ATLAS at your own project, replace the example entries in your projects file, or use
**Add project** in ATLAS. Give each project its own `hosts` for its CI and links, and a
`blocker_note` if your project also lacks a record of release blockers.
