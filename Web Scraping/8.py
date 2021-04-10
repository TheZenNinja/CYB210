import bs4
import requests

req = requests.get("http://inventwithpython.com/")
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text, "html.parser")