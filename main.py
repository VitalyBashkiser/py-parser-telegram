from resume_scraper.work_ua_scraper import WorkUaScraper
from resume_scraper.robota_ua_scraper import RobotaUaScraper

from resume_evaluation.evaluator import rate_candidates


if __name__ == "__main__":
    with RobotaUaScraper(
        job_position="python developer",
        years_of_experience=10,
        location="Київ",
        salary_expectation=[50000],
    ) as robota_ua_scraper:
        robota_ua_scraper.scrape()
        robota_ua_scraper.close()

    with WorkUaScraper(
        job_position="python developer",
        years_of_experience=10,
        location="Kyiv",
    ) as work_ua_scraper:
        work_ua_scraper.scrape()
        work_ua_scraper.close()

    rate_candidates(
        "jobs.csv",
        [
            "Python",
            "Django",
            "GIT",
            "SQL",
            "FastAPI",
        ],
        "sorted_resumes.csv",
    )
