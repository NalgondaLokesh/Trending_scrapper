import requests
from bs4 import BeautifulSoup
import csv

# GitHub Trending URL
url = "https://github.com/trending"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find repository list items
repo_list = soup.find_all("article", class_="Box-row")[:5]  # Top 5

# Prepare data for CSV
repos = []
for repo in repo_list:
    # Get repository name and link
    anchor = repo.h2.a
    repo_name = anchor.get_text(strip=True).replace("\n", "").replace(" ", "")
    repo_link = "https://github.com" + anchor['href']
    repos.append([repo_name, repo_link])

# Save to CSV
with open("trending_repos.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Repository Name", "Link"])
    writer.writerows(repos)

print("Top 5 trending repositories saved to 'trending_repos.csv'")
