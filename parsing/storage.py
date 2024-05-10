import csv
from dataclasses import dataclass, fields, astuple


@dataclass
class Vacancy:
    title: str
    location: str
    stack: list[str]
    url: str


VACANCY_FIELDS = [field.name for field in fields(Vacancy)]


def csv_writer(filename: str, vacancies: list[Vacancy]) -> None:
    with open(f"{filename}.csv", "w+") as file:
        writer = csv.writer(file)
        writer.writerow(VACANCY_FIELDS)
        writer.writerows([astuple(vacancy) for vacancy in vacancies])
