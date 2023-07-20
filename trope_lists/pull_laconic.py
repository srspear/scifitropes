import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

# Read the existing CSV
df = pd.read_csv('identicalclone_tropesdb.csv')

# Initialize a list to hold laconic texts
laconic = []

# Instantiate RobotFileParser and set the url to robots.txt of the domain
rp = RobotFileParser()
rp.set_url('https://tvtropes.org/robots.txt')
rp.read()

# Define headers to present as a web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

for url in df['laconic_url']:
    # Check if we are allowed to scrape the page
    if rp.can_fetch('*', url):
        # Send a GET request
        response = requests.get(url, headers=headers)

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the specific text and append to laconic
        main_article = soup.find('div', {'id': 'main-article', 'class': 'article-content retro-folders'})
        if main_article:
            p_text = main_article.find('p').text.split('<hr')[0]
            laconic.append(p_text)
        else:
            laconic.append(None)
        
        # Sleep to delay for next request
        time.sleep(1)
    else:
        print(f'Not allowed to scrape {url}')
        laconic.append(None)

# Add the laconic to the dataframe
df['laconic'] = laconic

# Save the updated dataframe back to CSV
df.to_csv('identicalclone_tropesdb_laconic.csv', index=False)

