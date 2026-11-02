<div align="center">
# 🌸 Sakhi
 
### Your friend for periods, PCOD, diet, yoga, skin and hair
 
A free, mobile-friendly women's health and wellness website.
Track your cycle, learn about PCOD/PCOS, eat well, move gently and care for your skin and hair, all in plain, kind language.
 
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![No Dependencies](https://img.shields.io/badge/dependencies-none-5d8a73?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-c8456b?style=for-the-badge)
 
**[Live demo](#-live-demo)** · **[Features](#-features)** · **[Run it](#-run-it-locally)** · **[Deploy](#-deploy-for-free)** · **[Roadmap](#-roadmap)**
 
</div>
---
 
## 💗 Why Sakhi?
 
*Sakhi* means "a close female friend" in Hindi. Many women have questions about periods, PCOD, weight, skin and hair but feel shy or can't find simple, trustworthy answers. Sakhi puts it all in one calm place, with no sign-up and no judgement.
 
## ✨ Features
 
| Section | What you get |
|---|---|
| 🩸 **Cycle tracker** | Enter your last period date to see a live cycle-phase ring, your next period, fertile window and estimated ovulation. Flags late or unusual cycles. |
| 🩺 **Health guides** | Plain-language guides on PCOD/PCOS, late or missed periods, painful or heavy periods, and thyroid, each with a "see a doctor if" box. |
| ⚖️ **BMI check** | BMI calculator using Asian-Indian ranges, a healthy weight range and simple weight habits. |
| 🥗 **Diet charts** | Indian vegetarian PCOD plan, a plan with egg or fish, and a "eat by cycle phase" guide. |
| 🍌 **2-minute recipes** | Quick healthy snacks and breakfasts such as sprouts chaat, makhana and smoothies. |
| 🧘 **Yoga** | Six poses for cramps and PCOD with benefits, steps and demo video links. |
| ✨ **Skin and hair** | Common skin and hair concerns, skin care tips, a haircare routine and hair fall care recipes. |
| 🤖 **AI health assistant** | Ask any question without sharing personal details. No name or email needed, and chats are not saved. |
 
### Built with care
 
- 📱 Mobile-first and responsive
- 🌙 Automatic light and dark mode
- ♿ Large tap targets, keyboard focus styles and reduced-motion support
- 🔒 Privacy-friendly: tracker dates are saved only in your own browser
- ⚡ A single `index.html` file, with no frameworks or build step
## 📸 Screenshots
 
> Add your screenshots to a `screenshots/` folder and update the paths below.
 
| Home | Cycle tracker | Skin and hair |
|:---:|:---:|:---:|
| ![Home](screenshots/home.png) | ![Tracker](screenshots/tracker.png) | ![Skin and hair](screenshots/skin-hair.png) |
 
## 🌐 Live demo
 
After you deploy (see below), add your link here:
 
```
https://YOUR-USERNAME.github.io/sakhi/
```
 
## 🚀 Run it locally
 
No installation needed.
 
```bash
# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/sakhi.git
 
# 2. Open the folder
cd sakhi
 
# 3. Open index.html in your browser
```
 
You can also double-click `index.html`, or use any simple server:
 
```bash
python -m http.server 8000
# then visit http://localhost:8000
```
 
## ☁️ Deploy for free
 
### GitHub Pages
 
1. Push this project to a GitHub repository.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select the `main` branch and the `/ (root)` folder, then click **Save**.
5. After a minute, your site is live at `https://YOUR-USERNAME.github.io/REPO-NAME/`.
### Netlify or Cloudflare Pages
 
Drag the project folder onto [Netlify Drop](https://app.netlify.com/drop), or connect the repository to Cloudflare Pages. No build settings are needed.
 
## 📁 Project structure
 
```
sakhi/
├── index.html      # The whole website (HTML, CSS and JavaScript)
├── README.md       # This file
└── screenshots/    # Optional images for this README
```
 
## 🤖 About the AI assistant
 
The chat assistant in the "Ask" section was built to run inside Claude, using Claude's built-in `sample` capability. This means:
 
- ✅ It works when the page is opened through its Claude artifact link.
- ⚠️ **It will not work** when the site is hosted on GitHub Pages or another host. There, it shows a friendly "not available" message, and all other sections work normally.
**To enable the chat on your own host**, add a small backend (for example a serverless function) that calls an AI API with your own secret key, and update the `ask()` function in `index.html` to call that endpoint. Never put an API key directly in the front-end code.
 
## 🛣️ Roadmap
 
- [ ] Hindi and other Indian language versions
- [ ] Short yoga demo videos (15 to 30 seconds)
- [ ] Backend for the AI assistant so it works on any host
- [ ] Installable app (PWA) with period reminders
- [ ] Blog and SEO articles
- [ ] Optional login to save cycle history
- [ ] Doctor-reviewed content badge
## 🤝 Contributing
 
Contributions are welcome, especially from doctors, dietitians, dermatologists and yoga teachers who can review content.
 
1. Fork the repository
2. Create a branch: `git checkout -b feature/your-idea`
3. Commit your changes: `git commit -m "Add your idea"`
4. Push the branch: `git push origin feature/your-idea`
5. Open a pull request
## ⚕️ Medical disclaimer
 
Sakhi shares **general health, skin and hair information only**. It is not a diagnosis and is not a substitute for advice from a qualified doctor. Cycle predictions are estimates and are not a form of birth control. If you have severe pain, very heavy bleeding, fever with pelvic pain, no period for 3 months or more, or any symptom that worries you, please see a doctor. In an emergency, call your local emergency number or go to the nearest hospital.
 
Content should be reviewed by a qualified gynecologist, dermatologist and dietitian before public use.
 
## 🔒 Privacy
 
- No account or personal details are needed.
- Cycle tracker dates are stored only in your browser's local storage and are never sent to a server.
- The AI assistant asks for no personal information. Please don't share any.
## 📄 License
 
Released under the [MIT License](LICENSE). Add a `LICENSE` file to your repository (GitHub can create one for you from **Add file → Create new file → LICENSE**).
 
---
 
<div align="center">
Made with 💗 for women's health and wellness
 
⭐ If this project helps you, please give it a star!
 
</div>
 
