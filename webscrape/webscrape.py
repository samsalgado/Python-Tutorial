from bs4 import BeautifulSoup
import requests
html_text = requests.get("https://bitcoin.org/en/")
print(html_text)
