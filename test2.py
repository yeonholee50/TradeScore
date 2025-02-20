import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://finviz.com/insidertrading.ashx?view=managers&page=200"  # Change if needed

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Fetch page content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Open CSV file for writing
with open("fund_managers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(soup)