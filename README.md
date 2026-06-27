# ∞ InfinitEd: Infinity Designs Edutainment

> **Stop Memorizing. Start Experiencing.**  
> A next-generation AI-powered edutainment platform that instantly transforms dense study materials into banger rap songs, breathtaking anime animation shorts, and immersive fiction novels.

![InfinitEd Concept](images/anime_biology.png)

---

## 🎯 Platform Overview & Monetization

**InfinitEd** bridges the massive gap between traditional academic materials and modern student attention spans. By acting as an AI orchestrator, the platform extracts key definitions from textbooks, lecture notes, or slides and synthesizes them into highly engaging edutainment media.

### 💰 Subscription Tiers

* **Free Teaser Tier ($0/month):**
  * **Engine:** Song & Rap Studio only.
  * **Music Genres:** All music genres included (*90s Boom Bap, Synthwave Pop, Lo-Fi Chill, Cyberpunk EDM, Acoustic Rock*).
  * **Input Limit:** 100-character input teaser limit.
  * **Quota:** Limited to 3–5 uses per month.
  * **Speed:** Standard generation queue.

* **Premium Scholar Tier ($9.99/month):**
  * **Engines:** Full access to **EVERYTHING** (Song/Rap Studio + Anime & Animation Lab + Immersive Novel Builder).
  * **Input Limit:** Unlimited characters (upload entire textbook chapters or long PDFs).
  * **Speed:** Priority server generation queue.
  * **Downloads:** High-resolution MP3, MP4, and EPUB exports.

---

## 🚀 How to Run the Localhost Server (For Client Preview)

This repository comes with a built-in zero-configuration Python web server to allow you and your clients to preview the complete interactive front-end simulation on your local machine.

### Prerequisites
Make sure you have **Python 3** installed on your computer. (Python comes pre-installed on Mac/Linux, and can be easily installed on Windows).

### Step-by-Step Instructions

1. **Open your terminal** (Terminal on Mac/Linux, or Command Prompt / PowerShell on Windows).
2. **Navigate to the project folder:**
   ```bash
   cd path/to/infinited-edutainment
   ```
3. **Run the local server script:**
   ```bash
   python3 server.py
   ```
   *(Note: On Windows, you may need to use `python server.py`)*

4. **View in Browser:**
   The script will automatically attempt to open your default web browser. If it doesn't, simply open your browser and go to:
   ```
   http://localhost:8000
   ```
   *Your client can now test the live interactive UI, character limit enforcement, music playback, and Premium tier toggle!*

---

## 🌐 How to Upload to GitHub & Deploy Live for Free

Want to send your client a live public web link (e.g., `https://yourusername.github.io/infinited-edutainment`) instead of making them run it locally? You can host it completely for **free** using **GitHub Pages**.

### Step 1: Push to Your GitHub Account

1. Go to [GitHub.com](https://github.com) and log in.
2. Click the **"+"** icon in the top right and select **New repository**.
3. Name your repository `infinited-edutainment` (keep it Public if you want to use free GitHub Pages) and click **Create repository**.
4. Open your terminal in this project folder and run the following commands to link and push your files:

```bash
# Initialize git repository (if not already done)
git init

# Add all files to staging
git add .

# Commit your files
git commit -m "Initial commit: InfinitEd premium edutainment platform"

# Link to your new GitHub repository (Replace USERNAME with your actual GitHub username)
git remote add origin https://github.com/USERNAME/infinited-edutainment.git

# Rename branch to main
git branch -M main

# Push files to GitHub
git push -u origin main
```

### Step 2: Enable Free Live Hosting (GitHub Pages)

Once your files are on GitHub, you can turn them into a live, shareable website in just 3 clicks:

1. On your GitHub repository page, click the **Settings** tab near the top right.
2. On the left sidebar, scroll down and click on **Pages**.
3. Under **Build and deployment**, look for **Branch**. Click the dropdown (which currently says *None*), select **`main`**, leave the folder as `/ (root)`, and click **Save**.
4. **Done!** Wait about 1–2 minutes, and GitHub will provide you with a live, secure URL at the top of the Pages settings screen:
   ```
   https://yourusername.github.io/infinited-edutainment/
   ```
   *You can instantly text or email this live link to your client for a spectacular preview!*

---

## 📂 Repository Structure

```
.
├── index.html            # Main application UI with standalone embedded CSS/JS & base64 assets
├── index_template.html   # Clean development template code (before base64 injection)
├── server.py             # Dedicated localhost Python web server script
├── README.md             # Platform overview & client preview instructions
├── .gitignore            # Git exclusion rules for clean version control
├── audio/
│   └── mitosis_rap.mp3   # Generated AI educational rap demo audio track
└── images/
    └── anime_biology.png # Generated AI 8K anime concept illustration
```

---

## 📄 License & Credits
Designed and built for **Infinity Designs Edutainment**. All rights reserved.
