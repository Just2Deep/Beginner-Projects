# Scraping GitHub Profile using Python

import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/just2deep"
req = requests.get(github_profile)

scraper = bs(req.content, "html.parser")
#print(scraper.find('img', {"alt": "Avatar"}))

profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]

print(profile_picture)
