# Dou Vacancy Scraper and Analyzer

## Overview
This project is aimed at scraping job vacancies from the DOU (Developers of Ukraine) website and analyzing them using Python. The scraper is built using Selenium, and the analysis is conducted using Pandas, NumPy, and Matplotlib libraries.

## Features
- __Scraping__: Utilizes Selenium to extract job vacancies data from the DOU website.
- __Analysis__: Employs Pandas, NumPy, and Matplotlib for in-depth analysis of the scraped data.
- __Visualization__: Generates visualizations to provide insights into job trends and statistics.

## Stack Used
This project leverages **Jupyter Notebook**, **Matplotlib**, **NumPy**, **Pandas**, **python-dotenv**, **Selenium**, and **tqdm** for various tasks such as data analysis, visualization, web scraping, and progress tracking.

## Installation
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
