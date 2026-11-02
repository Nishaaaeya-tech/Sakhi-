from datetime import date

import pytest

from app import create_app
from sakhi import bmi, chat, cycle


def test_cycle_prediction():
    r = cycle.predict(date(2026, 1, 1), 28, 5, today=date(2026, 1, 3))
    assert r["next_period"] == "2026-01-29"
    assert r["ovulation"] == "2026-01-15"
    assert r["fertile_window"] == ["2026-01-11", "2026-01-16"]
    assert r["cycle_day"] == 3 and r["phase"] == "period"


def test_late_period_is_flagged():
    r = cycle.predict(date(2026, 1, 1), 28, 5, today=date(2026, 2, 10))
    assert r["days_late"] == 12 and r["phase"] == "late" and r["notes"]


def test_invalid_cycle_length():
    with pytest.raises(ValueError):
        cycle.predict(date(2026, 1, 1), 5, 5)


def test_bmi_categories():
    assert bmi.calculate(160, 58)["category"] == "healthy range"
    assert bmi.calculate(160, 75)["category"] == "overweight range"
    with pytest.raises(ValueError):
        bmi.calculate(50, 60)


def test_clean_messages():
    msgs = chat.clean_messages([{"role": "assistant", "content": "hi"}, {"role": "user", "content": " Hello "}])
    assert msgs == [{"role": "user", "content": "Hello"}]
    with pytest.raises(ValueError):
        chat.clean_messages([{"role": "user", "content": "a"}, {"role": "assistant", "content": "b"}])


@pytest.fixture
def client():
    return create_app().test_client()


def test_home_and_health(client):
    assert client.get("/").status_code == 200
    assert client.get("/healthz").json == {"status": "ok"}


def test_api_endpoints(client):
    r = client.post("/api/cycle", json={"last_period": "2026-01-01"})
    assert r.status_code == 200 and "next_period" in r.json
    assert client.post("/api/cycle", json={"last_period": "bad"}).status_code == 400
    assert client.post("/api/bmi", json={"height_cm": 160, "weight_kg": 58}).json["bmi"] == 22.7


def test_chat_without_key_and_with_mock(client, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    assert client.post("/api/chat", json={"messages": []}).status_code == 503
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test")
    monkeypatch.setattr(chat, "reply", lambda m: "Drink water and rest.")
    r = client.post("/api/chat", json={"messages": [{"role": "user", "content": "Cramps?"}]})
    assert r.json == {"reply": "Drink water and rest."}
    assert client.post("/api/chat", json={"messages": "x"}).status_code == 400
