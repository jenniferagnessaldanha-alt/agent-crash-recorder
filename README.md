# Agent Crash Recorder

License: MIT

A black box, replay debugger and regression-test generator for multi-agent AI workflows.
It finds the **first bad handoff** (not the last agent), proves it with counterfactual
replay, and turns the incident into a test.

Built for the Nebius x NVIDIA Global AI Hackathon (track: Coding and Agentic Engineering).

## Status
Day 1: scope frozen, repo scaffolded, model connectivity script ready.

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # add your NEBIUS_API_KEY
python scripts/check_models.py
```

## Where Nemotron and Nebius are used
(Fill in as built: Token Factory for requirement extraction, handoff checks,
root-cause analysis; Serverless Jobs for replay sweeps and benchmark.)

## Layout
- `sdk/` decorator-based tracing SDK
- `backend/` FastAPI, trace store, checks, replay, test generation
- `demo_agents/` Researcher, Planner, Coder, Verifier
- `dashboard/` React + Three.js UI
- `scripts/` utilities
- `docs/` scope, schema, benchmark
