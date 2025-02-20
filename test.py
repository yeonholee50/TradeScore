import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://www.marketbeat.com/ratings/by-issuer/evercore-isi-stock-recommendations/"  # Change if needed

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Fetch page content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Open CSV file for writing
with open("analyst_ratings.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Ticker", "Company Name", "Brokerage", "Action", "Current Price", "Price Target", "Rating"])

    # Find all table rows
    for row in soup.find_all("tr"):
        columns = row.find_all("td")
        if len(columns) < 7:
            continue  # Skip invalid rows
        
        # Extract values
        ticker_name = columns[0].get("data-clean", "").split("|")
        ticker, company = ticker_name if len(ticker_name) == 2 else ("", "")

        action = columns[1].get("data-sort-value", "").strip()
        brokerage = columns[2].get("data-sort-value", "").strip()
        current_price = columns[4].get("data-clean", "").split("|")[0].strip()
        price_target = columns[5].text.strip()
        rating = columns[6].text.strip()

        # Write to CSV
        writer.writerow([ticker, company, brokerage, action, current_price, price_target, rating])

print("Data successfully extracted and saved to analyst_ratings.csv")
