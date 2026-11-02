"""AI health assistant. The API key stays on the server, never in the browser."""
from __future__ import annotations

import os

SYSTEM_PROMPT = (
    "You are the assistant on Sakhi, a women's health, skin and hair information website "
    "for readers in India. Answer questions on periods, PCOD/PCOS, late or irregular cycles, "
    "gynecological health, weight management, diet, yoga, skin care, hair care and hair fall. "
    "Use simple, warm, plain language and short paragraphs, under 180 words. Suggest Indian "
    "food options where relevant. Never diagnose or prescribe medicines or doses. Always "
    "mention when to see a doctor if symptoms could be serious (very heavy bleeding, severe "
    "pain, no period for 3+ months, fever with pelvic pain, possible pregnancy). For "
    "emergencies, tell the person to seek urgent medical care. Do not ask for or store "
    "personal details; if the person shares any, gently tell them it is not needed. "
    "Politely decline topics unrelated to health and wellness."
)

MAX_MESSAGES = 10
MAX_CHARS = 500


def clean_messages(raw) -> list[dict]:
    """Validate and trim the chat history sent by the browser."""
    if not isinstance(raw, list):
        raise ValueError("messages must be a list")
    msgs = []
    for m in raw[-MAX_MESSAGES:]:
        if not isinstance(m, dict) or m.get("role") not in ("user", "assistant"):
            raise ValueError("invalid message")
        content = m.get("content")
        if not isinstance(content, str) or not content.strip():
            raise ValueError("invalid message")
        msgs.append({"role": m["role"], "content": content.strip()[:MAX_CHARS]})
    while msgs and msgs[0]["role"] != "user":
        msgs.pop(0)
    if not msgs or msgs[-1]["role"] != "user":
        raise ValueError("the last message must come from the user")
    return msgs


def reply(messages: list[dict]) -> str:
    import anthropic  # imported here so the rest of the app works without it

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    response = client.messages.create(
        model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-5"),
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=messages,
    )
    return "".join(b.text for b in response.content if b.type == "text").strip()
