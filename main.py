from parse import DouVacancyScraper
from storage import csv_writer


PYTHON_URL = "https://jobs.dou.ua/vacancies/?category=Python"
EXP_RANGES = {
    "0-1": ("python_0-1", "&exp=0-1",),
    "1-3": ("python_1-3", "&exp=1-3",),
    "3-5": ("python_3-5", "&exp=3-5",),
    "5+": ("python_5+", "&exp=5plus",)
}


def scrape_general_vacancy_data(url: str) -> None:
    scraper = DouVacancyScraper()
    vacancies = scraper.scrape_all_vacancies(url)
    csv_writer("python", vacancies)


def scrape_vacancy_data_by_experience(range: str) -> None:
    scraper = DouVacancyScraper()

    filename, url = EXP_RANGES.get(range)

    if filename and url:
        vacancies = scraper.scrape_all_vacancies(PYTHON_URL + url)
        csv_writer(filename, vacancies)
    else:
        raise ValueError("Invalid range")


if __name__ == "__main__":
    scrape_general_vacancy_data(PYTHON_URL)

    for range in EXP_RANGES:
        scrape_vacancy_data_by_experience(range)
