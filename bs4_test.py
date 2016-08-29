#! /usr/bin/python3

from bs4 import BeautifulSoup
import urllib

urlString = "https://en.wikipedia.org/w/index.php?title=Cannabis_(drug)"
wikipediaPageHtml = urllib.urlopen(urlString).read()

soup = BeautifulSoup(wikipediaPageHtml)

print soup.get_text()
