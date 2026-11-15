# ATLAS sandbox target

This repository is the demo target for [ATLAS](https://github.com/AnaghaP09/atlas). It stands in
for an organisation's own code. ATLAS proposes small fixes here. This lets the demo show the
whole code-change process without touching a real project.

## Status

This repository is empty apart from this page and the licence. Two things are not here yet:

- **The first content.** A small Go package, its tests and its automated test setup will be
  added. They are sample code written for the demo. They do not come from any other project.
- **Draft pull requests.** ATLAS does not open pull requests here yet. That step is not
  connected.

## How changes arrive

1. ATLAS investigates a failure. It suggests giving a small, well-defined fix to a coding agent.
   A coding agent is a program that writes code changes.
2. An engineering manager approves the preparation of the change.
3. The coding agent writes the change inside a container. A container is an isolated space on
   the computer. This one has no network access and no secrets. ATLAS builds and tests the
   change inside the container.
4. The engineering manager approves the exact change.
5. ATLAS opens a **draft** pull request in this repository. A pull request is a proposed change
   that a person reviews. The automated tests run in the same kind of container. A person
   decides whether the fix is correct.

Steps 1 to 4 work today. Step 5 is the part that is not connected.

Nothing will merge automatically. Each pull request stays a draft until a person decides.

## About this project

This repository is part of ATLAS. ATLAS was built as a capstone project.

## Licence

MIT (see LICENSE).
