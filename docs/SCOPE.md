# Frozen scope (Day 1)

## Claim
Find the first bad handoff in a multi-agent run, prove it with counterfactual replay,
and generate a regression test.

## In scope
- 4 demo agents: Researcher, Planner, Coder, Verifier
- Decorator-based SDK + trace schema (agent, handoff, tool call, model call)
- Requirement checklist extraction + handoff integrity checks
- First-bad-handoff detection
- Counterfactual replay (repair one handoff, rerun downstream)
- Regression test generation (asserts requirements survive every handoff)
- Developer report + manager report
- Masking of keys and emails only
- 3D handoff graph in dashboard (2D fallback)
- Benchmark: ~40 injected-fault runs, baselines: blame-last-agent, LLM-reads-full-log

## Out of scope
- Browser agent, failure clustering at scale, full privacy suite, multi-tenant auth,
  framework adapters beyond one optional (LangGraph or CrewAI)

## Demo scenarios
1. Temperature CLI (C, F, K): Planner drops Kelvin.
2. Research says 100/min, Planner writes 1000/min (mutated fact).

## Fault types for benchmark
dropped requirement, mutated fact, wrong verification target, stale memory
(hold one type out of rule design as a held-out test).

## Cut order if behind
1. 3D graph -> 2D graph
2. Manager report
3. Second demo scenario
Never cut: replay proof, benchmark table, demo video.
