import requests
from bs4 import BeautifulSoup

url = "https://angel.co/europe"

r = requests.get(url)
htmlContent = r.content
# print(htmlConten)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://angel.co" +link.get('href')
        all_links.add((link))
        print(linkText)