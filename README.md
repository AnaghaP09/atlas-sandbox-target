# ATLAS sandbox target

This repository is the demonstration target for [ATLAS](https://github.com/AnaghaP09/atlas). It
plays the part of a customer's code base: ATLAS proposes small, bounded fixes here so that its
execution path can be shown end to end without touching any real project.

## How changes arrive

1. ATLAS investigates a failure and recommends delegating a bounded fix to a coding agent.
2. An engineering manager approves preparing the task.
3. The coding agent writes the change inside a container with no network access and no secrets.
   The change is built and tested there.
4. The engineering manager approves the exact diff.
5. ATLAS opens a **draft** pull request here. CI runs the tests in the same isolation, and a
   person judges whether the fix is correct.

Nothing is merged automatically. Every pull request stays a draft until a person decides.

## Contents

The Go package and its tests will be added here. They are written for the demo and are not taken
from any other project.

## About this project

This repository is part of the ATLAS team capstone project by Swetha, Bhuneshwari and Anagha.
