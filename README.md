# Dou Vacancy Scraper and Analyzer

## Overview
This project is aimed at scraping job vacancies from the DOU (Developers of Ukraine) website and analyzing them using Python. The scraper is built using Selenium, and the analysis is conducted using Pandas, NumPy, and Matplotlib libraries.

## Analysis
### General Stack Analysis
I'll begin by scraping all Python-related job listings to gather data on required technologies. Once the data is cleaned and prepared, I'll generate a chart like this:

![Stack Analysis](/analysis/plots/2024-05-10-stack-analysis.jpg)

#### Summary
It's evident that the predominant high-demand tools are associated with web development. Additionally, employers prioritize developers who comprehend SOLID, REST, and OOP principles.

### Location Analysis
Next, let's explore the top cities in demand for developers. Using the same dataset of vacancies and employing similar cleaning and preparation methods, I'll uncover the leading cities sought after by developers.

![Location Analysis](/analysis/plots/2024-05-10-location-analysis.jpg)

#### Summary
While a significant number of companies offer remote work opportunities, it's noteworthy that three Ukrainian cities—Kyiv, Lviv, and Dnipro—are among the most sought after by developers. Additionally, many companies are either headquartered or seeking developers based in various countries, indicating a global scope in the search for talent.

### Junior vs Senior Stack Analysis
This part of the analysis is probably one of the most intriguing and controversial. Using dou.ua's feature to filter vacancies based on years of experience, I can analyze the required skill sets for specific experience ranges and draw conclusions based on the findings.

![Junior Stack Analysis](/analysis/plots/2024-05-10-junior-stack-analysis.jpg)

![Senior Stack Analysis](/analysis/plots/2024-05-10-senior-stack-analysis.jpg)

#### Summary

It's immediately apparent that there's a disparity in the number of Junior vacancies compared to Senior positions. However, beyond this observation, certain trends emerge. For Junior developers, employers prioritize basic skills like Git, Docker, and SQL. In contrast, Senior roles require experience with more advanced technologies, ranging from Kubernetes to TensorFlow.

## Installation
Want to get started launching this project locally? Awesome! Just follow these simple steps below!

1. Clone the repository:
```bash
git clone https://github.com/aLEKS-e3/vacancy-scrape-analysis.git
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the scraper to have all the fresh data stored in the csv:
```bash
python main.py
```
2. Run jupyter notebook to perform basic analysis:
```bash
jupyter notebook vacancy_analysis.ipynb 
```
3. Check the generated visualizations and analysis report in the output directory.
