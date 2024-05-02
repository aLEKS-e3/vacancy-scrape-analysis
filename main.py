from parse import DouVacancyScraper
from storage import csv_writer


def launch_scrape_analysis():
    scraper = DouVacancyScraper()
    vacancies = scraper.scrape_all_vacancies()
    csv_writer("python", vacancies)


if __name__ == "__main__":
    launch_scrape_analysis()
