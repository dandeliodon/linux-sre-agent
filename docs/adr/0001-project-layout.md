# 0001. Project layout and module boundaries

- Status: Accepted
- Date: 2026-10-30

## Context
These choices made for better centralize package maintenance and security reasons of LLM which can read untrusted logs and propose mutating commands

## Decision
1. src layout instead of flat for test to import installed packages 
2. one sre_agent package with submodule for each component, shared config.py and events.py
3. LLM side is read only, and only after classifier gets approval executor is allowed to write 

## Consequences
1. test imports installed packages so mistakes will show locally rather than in production
2. shared packages to reduce code duplication and centralize maintenance 
3. force to test that LLM won't run mutating command to the server
