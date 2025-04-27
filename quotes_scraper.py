import requests
from bs4 import BeautifulSoup
import csv

# URL of the static website to scrape
URL = "http://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(URL)
response.raise_for_status()  # Raise an exception for bad status codes

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote containers
quotes = soup.find_all("div", class_="quote")

# Prepare data for CSV
quote_data = []
for quote in quotes:
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
    quote_data.append({"quote": text, "author": author, "tags": tags})

# Write to CSV file
with open("quotes.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["quote", "author", "tags"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(quote_data)

print(f"Scraped {len(quote_data)} quotes and saved to quotes.csv")