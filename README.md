# 📜 Project-WebScraper-Quotes

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Issues](https://img.shields.io/github/issues/udaykotian/Project-WebScraper-Quotes)

A lightweight Python web scraper that extracts quotes, authors, and tags from the static website [quotes.toscrape.com](http://quotes.toscrape.com/) using `requests` and `BeautifulSoup`. The scraped data is saved in a structured CSV file (`quotes.csv`) for easy analysis.

## 🌟 Features
- Extracts quotes, authors, and associated tags from a static website.
- Saves data in a CSV format for portability and analysis.
- Lightweight, efficient, and beginner-friendly implementation.

## 🛠️ Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.13** (or compatible version)
- **pip** (Python package manager)

## 🚀 Installation
Follow these steps to set up and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/udaykotian/Project-WebScraper-Quotes.git
   cd Project-WebScraper-Quotes

Set up a virtual environment (recommended):
bash

python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

Install dependencies:
bash

pip install -r requirements.txt

 Usage
Run the scraper to extract quotes and save them to quotes.csv:
bash

python3 quotes_scraper.py

The script will:
Fetch quotes from quotes.toscrape.com.

Save the data to quotes.csv in the project directory.

Example Output (quotes.csv)
quote

author

tags

"The world as we have created it..."

Albert Einstein

change,deep-thoughts

"It is our choices, Harry, that..."

J.K. Rowling

abilities,choices

 Project Structure

Project-WebScraper-Quotes/
├── quotes_scraper.py    # Main script for scraping quotes
├── quotes.csv           # Output file with scraped data
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
└── LICENSE              # MIT License file

 License
This project is licensed under the MIT License (LICENSE) - see the file for details.


