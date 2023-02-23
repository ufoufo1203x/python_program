import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/home?hl=ja&gl=JP&ceid=JP:ja"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Find all the headlines on the page
headlines = soup.find_all("h3")
for headline in headlines:
    print(headline.text)
