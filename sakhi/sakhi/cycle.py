"""Menstrual cycle predictions. These are estimates, not medical advice."""
from __future__ import annotations

from datetime import date, timedelta

MIN_CYCLE, MAX_CYCLE = 15, 60
MAX_PERIOD = 12


def predict(
    last_period: date,
    cycle_length: int = 28,
    period_length: int = 5,
    today: date | None = None,
) -> dict:
    """Return the next period, fertile window, ovulation and current phase."""
    today = today or date.today()
    if not MIN_CYCLE <= cycle_length <= MAX_CYCLE:
        raise ValueError(f"cycle_length must be between {MIN_CYCLE} and {MAX_CYCLE}")
    if not 1 <= period_length <= MAX_PERIOD:
        raise ValueError(f"period_length must be between 1 and {MAX_PERIOD}")

    next_period = last_period + timedelta(days=cycle_length)
    ovulation = last_period + timedelta(days=cycle_length - 14)
    fertile_start = ovulation - timedelta(days=4)
    fertile_end = ovulation + timedelta(days=1)

    day = (today - last_period).days + 1  # day 1 = first day of period
    days_late = (today - next_period).days

    if day < 1:
        phase = "future"
    elif day <= period_length:
        phase = "period"
    elif day < cycle_length - 17:
        phase = "follicular"
    elif day <= cycle_length - 12:
        phase = "fertile window"
    elif day <= cycle_length:
        phase = "luteal"
    else:
        phase = "late"

    notes = []
    if not 21 <= cycle_length <= 35:
        notes.append("Cycle length is outside the usual 21 to 35 days. Consider a check-up.")
    if days_late >= 7:
        notes.append("Your period is a week or more late. If you may be pregnant, take a test, and see a gynecologist if this happens often.")
    elif days_late > 0:
        notes.append("Your period is a little late. Small delays are common with stress or travel.")

    return {
        "cycle_day": day if day >= 1 else None,
        "phase": phase,
        "next_period": next_period.isoformat(),
        "ovulation": ovulation.isoformat(),
        "fertile_window": [fertile_start.isoformat(), fertile_end.isoformat()],
        "days_late": max(days_late, 0),
        "notes": notes,
    }
