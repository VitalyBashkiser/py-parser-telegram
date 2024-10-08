# py-parser-telegram

# 📄 Resume Parser & Sorter Bot 🤖
This project is a comprehensive solution designed to streamline the hiring process by parsing and sorting resumes from popular job websites and interfacing with a Telegram bot for user-friendly interactions.

# 🌟 Project Overview
This project is divided into three main parts:

Resume Parsing: Scrapes resumes from work.ua and robota.ua with customizable filters such as job position, years of experience, skills, location, and salary expectations.
Candidate Sorting: Implements a scoring mechanism to rank candidates based on their relevance to the specified job criteria.
Telegram Bot Interface: Provides an intuitive interface via Telegram for HR personnel to interact with the system, fetch resumes, and view the most relevant candidates.
# 🛠️ Features
# 🔍 Advanced Resume Filtering: Filter resumes by job position, experience, skills, location, and more.
# 📊 Intelligent Candidate Scoring: Sort candidates using a custom scoring algorithm that prioritizes relevant experience and skills.
# 🤖 Telegram Bot Integration: User-friendly Telegram bot for easy access to resumes directly within the app.
# 🚀 Getting Started
- Prerequisites
- Python 3.x
- Telegram Bot API Token
- Environment variables setup using .env with decouple
# Installation
Clone the repository:

```bash
git clone https://github.com/VitalyBashkiser/py-parser-telegram.git
cd resume-parser-bot
```
**Install dependencies:**

```bash
pip install -r requirements.txt
```
**Set up environment variables:**

Create a .env file in the project root with the following:

```bash
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```
Running the Bot
To start the bot, simply run:

```bash
python main.py
```
# ⚙️ How It Works
**Resume Parsing:**
Uses web scraping to collect resumes from work.ua and robota.ua.
Filters results based on user-defined criteria.
**Candidate Sorting:**
Sorts parsed resumes using a custom scoring mechanism based on job relevance.
**Telegram Bot Interface:**
Allows users to interact with the system through a Telegram bot.
Users can specify criteria and get links to the relevant resumes.

# 📚 Project Structure
- resume_scraper/: Contains the scrapers for each job website.
- resume_evaluation/: Contains the scoring mechanism to sort candidates.
- bot/: Contains the Telegram bot implementation.
- utils/: Utility functions including environment loading and keyboard creation.

# 📝 Future Improvements
Adding support for more job websites.
Enhancing the scoring mechanism with machine learning techniques.
Improving the Telegram bot with more interactive features like inline keyboards.

# 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
