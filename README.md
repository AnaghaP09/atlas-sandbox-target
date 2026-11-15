# ATLAS sandbox target

This repository is the demo target for [ATLAS](https://github.com/AnaghaP09/atlas). It stands in
for an organisation's own code. ATLAS proposes small fixes here. This lets the demo show the
whole code-change process without touching a real project.

## Status

This repository holds a small Go package, `netaddr`, with a known bug: it joins IPv6 addresses
and ports in the wrong form. The package is sample code written for the demo. It does not come
from any other project.

The behaviour test for the bug fails on purpose, so the automated test run shows red until a fix
lands. ATLAS does not open pull requests here yet. That step is not connected.

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
