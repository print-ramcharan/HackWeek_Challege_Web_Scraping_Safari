from bs4 import BeautifulSoup as Soup
import requests as R, csv

# fetching the webpage content using req.
html = R.get("https://github.com/trending").text

# parsing using BeautifulSoup
soup = Soup(html, 'html.parser')

# the hierarchy in which the required data is present.
repos = soup.select("article h2 a")[:5]

# created a csv file.
with open("trending.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    #creating a row.
    writer.writerow(["repository_name", "repository_link"])
    
    #looping through the top 5 and scrapping.
    for repo in repos:
        name = ' '.join(repo.text.split())
        link = "https://github.com" + repo['href']
        # adding into csv
        writer.writerow([name, link])

