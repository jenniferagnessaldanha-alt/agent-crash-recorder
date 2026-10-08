"""Day 1 check: connect to Nebius Token Factory, list models, test a call.

Usage: python scripts/check_models.py [model_id]
"""
import os
import sys
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.environ.get("NEBIUS_API_KEY")
if not key:
    sys.exit("Set NEBIUS_API_KEY in .env first.")

client = OpenAI(
    base_url=os.environ.get("NEBIUS_BASE_URL", "https://api.tokenfactory.nebius.com/v1/"),
    api_key=key,
)

models = [m.id for m in client.models.list().data]
print(f"{len(models)} models available.\n")
nemo = [m for m in models if "nemotron" in m.lower()]
print("Nemotron models:")
for m in nemo or ["(none found - check the console / hackathon credits)"]:
    print("  ", m)

target = sys.argv[1] if len(sys.argv) > 1 else (nemo[0] if nemo else None)
if not target:
    sys.exit("\nNo model to test. Pass one as an argument.")

print(f"\nTesting {target} ...")
t0 = time.time()
r = client.chat.completions.create(
    model=target,
    messages=[{"role": "user", "content": "Reply with exactly: ready"}],
    max_tokens=500,
)
print("Reply:", (r.choices[0].message.content or "").strip())
print(f"Latency: {time.time() - t0:.2f}s")
if r.usage:
    print(f"Tokens: {r.usage.prompt_tokens} in / {r.usage.completion_tokens} out")
