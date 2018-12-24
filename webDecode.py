import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
title = soup.find_all(class_="story-heading") # if you look through the html you find all title have the class story-heading
# title is now a list of the story-heading class

for headings in title:
	if headings.a:
		print(headings.a.text.replace("\n", " ").strip())
	else:
		print(headings.contents[0].strip())

