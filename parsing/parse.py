import os

from time import sleep
from tqdm import tqdm
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from storage import Vacancy


load_dotenv()

TECHNOLOGIES = os.getenv("TECHNOLOGIES")


class DouVacancyScraper:
    def __init__(self) -> None:
        self.driver = self.get_driver()
        self.detail_driver = self.get_driver()

    def modify_options(self) -> Options:
        options = Options()
        options.add_argument("--headless=new")
        return options

    def get_driver(self):
        return webdriver.Chrome(options=self.modify_options())

    def has_more(self) -> bool:
        try:
            pagination = self.driver.find_element(By.CLASS_NAME, "more-btn")
        except NoSuchElementException:
            return False

        if "display: none;" in pagination.get_attribute("outerHTML"):
            return False

        return pagination.is_displayed()

    def extract_all_vacancies(self) -> None:
        while self.has_more():
            try:
                more = self.driver.find_element(
                    By.CSS_SELECTOR, "#vacancyListId > div > a"
                )
                more.click()
            except ElementNotInteractableException:
                sleep(0.15)

    def open_detail_page(self, vacancy: WebElement) -> str:
        detail_url = vacancy.find_element(
            By.CLASS_NAME, "vt"
        ).get_attribute("href")

        self.detail_driver.get(detail_url)
        return detail_url

    def scrape_single_vacancy(self, vacancy: WebElement) -> Vacancy:
        detail_url = self.open_detail_page(vacancy)

        title = WebDriverWait(self.detail_driver, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "g-h2"))
        ).text

        description = self.detail_driver.find_element(
            By.CSS_SELECTOR, "div.text.b-typo.vacancy-section"
        ).text

        stack = [
            tech for tech in TECHNOLOGIES.split(",")
            if tech.lower() in description.lower()
        ]

        try:
            location = self.detail_driver.find_element(
                By.CLASS_NAME, "bi-geo-alt-fill"
            ).text
        except NoSuchElementException:
            location = None

        return Vacancy(
            title=title,
            location=location,
            stack=stack if stack else None,
            url=detail_url
        )

    def scrape_all_vacancies(self, url: str) -> list[Vacancy]:
        self.driver.get(url)
        self.extract_all_vacancies()

        vacancies = self.driver.find_elements(By.CLASS_NAME, "l-vacancy")

        return [
            self.scrape_single_vacancy(vacancy)
            for vacancy in tqdm(vacancies, desc="Total progress", position=0)
        ]
