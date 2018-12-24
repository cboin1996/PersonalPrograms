#Written by Cboin.
#you may import and use in pieces of code.
import requests

from bs4 import BeautifulSoup

def htmlTextGrab():
	url = input("Enter a url: ")
	r = requests.get(url)
	r_html = r.text
	niceContent = []
	soup = BeautifulSoup(r_html, "html.parser")
	filetoWrite = input("Enter a name to save the file contents to: ")
	with open(filetoWrite, 'w') as var: #w is write only, r is readonly, r+ is both :p
		var.write(soup.text)
	print("Contents written to: ", filetoWrite)

if __name__=="__main__":
	htmlTextGrab()
	
	

	