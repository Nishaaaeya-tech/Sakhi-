"""BMI using the Asian-Indian cut-offs. A screening number, not a diagnosis."""
from __future__ import annotations


def calculate(height_cm: float, weight_kg: float) -> dict:
    if not 100 <= height_cm <= 220:
        raise ValueError("height_cm must be between 100 and 220")
    if not 25 <= weight_kg <= 250:
        raise ValueError("weight_kg must be between 25 and 250")

    h = height_cm / 100
    bmi = weight_kg / (h * h)
    if bmi < 18.5:
        category = "underweight range"
    elif bmi < 23:
        category = "healthy range"
    elif bmi < 25:
        category = "overweight risk range"
    else:
        category = "overweight range"

    return {
        "bmi": round(bmi, 1),
        "category": category,
        "healthy_weight_kg": [round(18.5 * h * h), round(22.9 * h * h)],
    }
