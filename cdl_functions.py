#! /usr/bin/python3

from bs4 import BeautifulSoup
import urllib
import json

def getWikipediaText(term):
	termSplit = term.split()
	urlString = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch="
	for word in termSplit:
		urlString = urlString + word + "%20"
	urlString = urlString[:-3] + "&utf8=&format=json"

	wikipediaSearchJson = urllib.urlopen(urlString).read()
	wikipediaSearch = json.loads(wikipediaSearchJson)

	print wikipediaSearch
	

	#urlString = "https://en.wikipedia.org/w/index.php?title=Cannabis_(drug)"
	#wikipediaPageHtml = urllib.urlopen(urlString).read()

	#soup = BeautifulSoup(wikipediaPageHtml)

	#return soup.get_text()
