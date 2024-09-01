import pandas as pd
from decouple import config
from telegram import ReplyKeyboardMarkup, KeyboardButton

from resume_evaluation.evaluator import rate_candidates
from resume_scraper.robota_ua_scraper import RobotaUaScraper
from resume_scraper.work_ua_scraper import WorkUaScraper


def load_token():
    return config("TELEGRAM_BOT_TOKEN")


def create_keyboard(options, one_time_keyboard=True):
    keyboard = [[KeyboardButton(option)] for option in options]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=one_time_keyboard)


def fetch_results(user_data) -> list:
    job_position = user_data.get("position")
    experience = user_data.get("experience")
    location = user_data.get("location")
    salary_expectation = user_data.get("salary")
    technologies = user_data.get("technologies", [])

    scrapers = []
    if user_data["job_site"] in ["work_ua", "both"]:
        scrapers.append(
            WorkUaScraper(
                job_position,
                years_of_experience=experience,
                location=location,
                salary_expectation=salary_expectation,
            )
        )
    if user_data["job_site"] in ["robota_ua", "both"]:
        scrapers.append(
            RobotaUaScraper(
                job_position,
                years_of_experience=experience,
                location=location,
                salary_expectation=salary_expectation,
            )
        )

    for scraper in scrapers:
        scraper.scrape()
        scraper.close()

    rate_candidates("jobs.csv", technologies, "sorted_resumes.csv")

    df = pd.read_csv("sorted_resumes.csv")
    links = df["resume"].head(5).tolist()

    return links
