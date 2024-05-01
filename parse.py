from time import sleep
from tqdm import tqdm

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from urllib.parse import urljoin


class DouVacancyScraper:
    def __init__(self) -> None:
        self.url = "https://jobs.dou.ua/vacancies/?category=Python"
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.modify_options())

    def modify_options(self) -> Options:
        self.options.add_argument("--headless=new")
        return self.options

    def has_more(self) -> bool:
        pagination = self.driver.find_element(By.CLASS_NAME, "more-btn")
        if "display: none;" in pagination.get_attribute("outerHTML"):
            return False

        return True

    def extract_all_vacancies(self) -> None:
        while self.has_more():
            try:
                more = self.driver.find_element(
                    By.CSS_SELECTOR, "#vacancyListId > div > a"
                )
                more.click()
            except ElementNotInteractableException:
                sleep(0.15)

    def parse_single_vacancy(self, vacancy: WebElement) -> dict:
        return dict(
            title=vacancy.find_element(By.CLASS_NAME, "vt").text
        )

    def scrape_all_vacancies(self) -> list:
        self.driver.get(self.url)
        self.extract_all_vacancies()

        vacancies = self.driver.find_elements(By.CLASS_NAME, "l-vacancy")

        return [
            self.parse_single_vacancy(vacancy)
            for vacancy in vacancies
        ]

scraper = DouVacancyScraper()
vacancies = scraper.scrape_all_vacancies()
