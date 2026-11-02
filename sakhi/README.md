<div align="center">

# 🌸 Sakhi

### Women's health, skin and hair guide, built with Python and Flask

Track your cycle, understand PCOD/PCOS, eat well, move gently and care for your skin and hair. It includes an AI health assistant that needs no personal details.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-c8456b?style=for-the-badge)

</div>

---

## ✨ Features

- 🩸 **Cycle tracker:** next period, fertile window, ovulation, a live phase ring, and late-cycle alerts
- 🩺 **Health guides:** PCOD/PCOS, late periods, painful or heavy periods, thyroid
- ⚖️ **BMI check** with Asian-Indian ranges
- 🥗 **Diet charts and 2-minute recipes** (Indian vegetarian and non-vegetarian)
- 🧘 **Yoga poses** for cramps and PCOD
- ✨ **Skin and hair care:** concerns, tips, routines and hair fall recipes
- 🤖 **AI assistant** (Claude API) with the key kept safely on the server
- 🌙 Responsive, light and dark mode, accessible

## 🧱 Tech stack

| Layer | Tools |
|---|---|
| Backend | Python, Flask |
| AI | Anthropic API (`anthropic` SDK) |
| Frontend | HTML, CSS, vanilla JavaScript |
| Tests | pytest |
| Deploy | gunicorn (Render, Railway, PythonAnywhere) |

## 📁 Project structure

```
sakhi/
├── app.py                 # Flask app and API routes
├── sakhi/
│   ├── cycle.py           # Cycle prediction logic
│   ├── bmi.py             # BMI calculator
│   └── chat.py            # AI assistant (prompt, validation, API call)
├── templates/index.html   # Page
├── static/css/style.css
├── static/js/app.js
├── tests/test_sakhi.py
├── requirements.txt
├── .env.example
└── Procfile
```

## 🚀 Getting started

```bash
git clone https://github.com/YOUR-USERNAME/sakhi.git
cd sakhi

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # then add your ANTHROPIC_API_KEY
python app.py
```

Open **http://localhost:5000**. Without an API key, everything works except the AI chat, which shows a "not set up" message.

Get an API key from the [Anthropic Console](https://console.anthropic.com/). **Never commit your `.env` file.**

## 🔌 API

| Method | Route | Body | Returns |
|---|---|---|---|
| `GET` | `/healthz` | | `{"status": "ok"}` |
| `POST` | `/api/cycle` | `{"last_period": "2026-01-01", "cycle_length": 28, "period_length": 5}` | Next period, ovulation, fertile window, phase, notes |
| `POST` | `/api/bmi` | `{"height_cm": 160, "weight_kg": 58}` | BMI, category, healthy weight range |
| `POST` | `/api/chat` | `{"messages": [{"role": "user", "content": "..."}]}` | `{"reply": "..."}` |

The chat endpoint validates input, caps message length, and limits each visitor to 20 questions per hour.

## 🧪 Run the tests

```bash
pip install -r requirements-dev.txt
pytest
```

## ☁️ Deploy

GitHub Pages cannot run Python, so use a Python host such as [Render](https://render.com), [Railway](https://railway.app) or [PythonAnywhere](https://www.pythonanywhere.com).

On Render: create a **Web Service** from your repo, set the build command to `pip install -r requirements.txt`, the start command to `gunicorn app:app`, and add `ANTHROPIC_API_KEY` as an environment variable.

## 🛣️ Roadmap

- [ ] Hindi and other Indian languages
- [ ] Yoga demo videos
- [ ] Optional login with saved cycle history (SQLite)
- [ ] PWA with period reminders
- [ ] Doctor-reviewed content badge

## 🤝 Contributing

Contributions are welcome, especially from doctors, dermatologists and dietitians who can review content. Fork the repo, create a branch, run `pytest`, and open a pull request.

## ⚕️ Medical disclaimer

Sakhi shares **general health, skin and hair information only**. It is not a diagnosis or a substitute for a qualified doctor. Cycle predictions are estimates and are not birth control. See a doctor for severe pain, very heavy bleeding, fever with pelvic pain, no period for 3 months or more, or any worrying symptom. In an emergency, call your local emergency number.

## 🔒 Privacy

No account is needed. Tracker dates stay in your browser's local storage. The AI assistant asks for no personal details, and chats are not saved by this app.

## 📄 License

MIT. See [LICENSE](LICENSE). Replace `YOUR NAME` in that file with your name.

---

<div align="center">Made with 💗 for women's health and wellness</div>
