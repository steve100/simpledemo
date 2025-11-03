#!/usr/bin/env python3
"""
Send a prompt to LM Studio (OpenAI-compatible local API)
with automatic server reachability check and error handling.
"""

import os
import sys
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Default to localhost if not defined
LMSTUDIO_API_BASE = os.getenv("LMSTUDIO_API_BASE", "http://localhost:1234/v1")
LMSTUDIO_API_KEY = os.getenv("LMSTUDIO_API_KEY", "not-needed")
MODEL_NAME = os.getenv("LMSTUDIO_MODEL", "granite-4.0-micro")

#actually it currently does not need a MODEL_NAME nor KEY.  Uses the loaded model
LMSTUDIO_API_KEY = ""
MODEL_NAME = ""

# --- Check if LM Studio server is reachable ---
try:
    health_url = LMSTUDIO_API_BASE.rstrip("/v1") + "/"
    r = requests.get(health_url, timeout=2)
    if r.status_code != 200:
        print(f"⚠️  Warning: LM Studio responded with status {r.status_code}")
except requests.RequestException as e:
    print(f"❌ Could not connect to LM Studio at {LMSTUDIO_API_BASE}")
    print(f"Error details: {e}")
    sys.exit(1)

# --- Initialize client ---
client = OpenAI(
    base_url=LMSTUDIO_API_BASE,
    api_key=LMSTUDIO_API_KEY
)

# --- Send a simple chat request ---
try:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a haiku about autumn."}
        ],
    )
    print("\n✅ LM Studio reply:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"❌ Error communicating with LM Studio: {e}")
    sys.exit(1)
