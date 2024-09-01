from abc import ABC, abstractmethod
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from resume_scraper.utils import save_to_file


class ResumeScraper(ABC):
    def __init__(
        self,
        base_url: str,
        job_position: str,
        years_of_experience: int = None,
        skills: List[str] = None,
        location: List[str] = None,
        salary_expectation: int = None,
        criterias: List[str] = None,
    ):
        self.base_url = base_url
        self.job_position = job_position
        self.years_of_experience = years_of_experience
        self.skills = skills
        self.location = location
        self.salary_expectation = salary_expectation
        self.criterias = criterias
        self._driver = None

    def __enter__(self):
        self._driver = self.__setup_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @staticmethod
    def __setup_driver():
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def get_driver(self):
        if not self._driver:
            self._driver = self.__setup_driver()
        return self._driver

    def close(self):
        if self._driver:
            self._driver.quit()
            self._driver = None

    @abstractmethod
    def get_filters(self, driver):
        pass

    @abstractmethod
    def apply_filters(self, driver):
        pass

    @abstractmethod
    def scrape(self):
        pass

    def save_to_file(self, data: List[dict], filename: str):
        save_to_file(data, filename)
