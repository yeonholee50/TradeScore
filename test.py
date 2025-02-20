import requests
from bs4 import BeautifulSoup
import csv

# URL of the MarketBeat analyst ratings page
url = 'https://www.marketbeat.com/ratings/'

# Send a GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Parse the HTML content using BeautifulSoup
csv_filename = 'analyst_ratings.csv'

soup = BeautifulSoup(response.text, 'html.parser')
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(soup)
    
# Find the table containing the analyst ratings
table = soup.find('table', {'class': 'ratings-table'})

# Check if the table was found
if not table:
    print('Error: Ratings table not found on the page.')
    exit()

# Extract table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    cols = row.find_all('td')
    if len(cols) == 0:
        continue  # Skip rows without data
    row_data = [col.text.strip() for col in cols]
    rows.append(row_data)

# Define the CSV filename
csv_filename = 'analyst_ratings.csv'

# Write data to CSV
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)  # Write header
    csvwriter.writerows(rows)    # Write data rows

print(f'Data successfully extracted and saved to {csv_filename}')
