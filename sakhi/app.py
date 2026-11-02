"""Sakhi: Flask app. Run with `python app.py`."""
from __future__ import annotations

import os
import time
from collections import defaultdict, deque
from datetime import date

from flask import Flask, jsonify, render_template, request

from sakhi import bmi, chat, cycle

try:  # optional: load variables from a local .env file
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

RATE_LIMIT = 20          # chat requests ...
RATE_WINDOW = 3600       # ... per hour, per visitor


def create_app() -> Flask:
    app = Flask(__name__)
    hits: dict[str, deque] = defaultdict(deque)

    def too_many() -> bool:
        now, q = time.time(), hits[request.remote_addr or "unknown"]
        while q and now - q[0] > RATE_WINDOW:
            q.popleft()
        if len(q) >= RATE_LIMIT:
            return True
        q.append(now)
        return False

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/healthz")
    def healthz():
        return {"status": "ok"}

    @app.post("/api/cycle")
    def api_cycle():
        data = request.get_json(silent=True) or {}
        try:
            result = cycle.predict(
                date.fromisoformat(data.get("last_period", "")),
                int(data.get("cycle_length", 28)),
                int(data.get("period_length", 5)),
            )
        except (ValueError, TypeError) as e:
            return jsonify(error=str(e)), 400
        return jsonify(result)

    @app.post("/api/bmi")
    def api_bmi():
        data = request.get_json(silent=True) or {}
        try:
            result = bmi.calculate(float(data.get("height_cm")), float(data.get("weight_kg")))
        except (ValueError, TypeError) as e:
            return jsonify(error=str(e)), 400
        return jsonify(result)

    @app.post("/api/chat")
    def api_chat():
        if not os.getenv("ANTHROPIC_API_KEY"):
            return jsonify(error="The assistant is not set up yet. Add ANTHROPIC_API_KEY on the server."), 503
        data = request.get_json(silent=True) or {}
        try:
            messages = chat.clean_messages(data.get("messages"))
        except ValueError as e:
            return jsonify(error=str(e)), 400
        if too_many():
            return jsonify(error="Too many questions. Please try again in a while."), 429
        try:
            return jsonify(reply=chat.reply(messages))
        except Exception:
            app.logger.exception("chat failed")
            return jsonify(error="Sorry, the assistant could not answer right now."), 502

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1", port=int(os.getenv("PORT", 5000)))
