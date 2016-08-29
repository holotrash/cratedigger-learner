#! /usr/bin/python3

from Tkinter import *
import ttk
import urllib
import json
from bs4 import BeautifulSoup
from cdl_functions import *

def getRecordFromWorld():
	print "got a record"

def getRecords():
	aCollectorName = collectorsComboBox.get()
	
	if(aCollectorName == ""):
		print "please select a collector"
	else:
		recordsListBox.delete(0, END)
		
		print "getting records from " + aCollectorName
		#TODO populate the list box if the user has selected a collector.
		urlString = "http://cratedigger.holotrash.com/api/crecordlist.php?c_name=" + aCollectorName
		print "url=" + urlString
		recordListJson = urllib.urlopen(urlString).read()
		recordList = json.loads(recordListJson)
		
		count = 1
		for r in recordList["records"]:
			aRecordStr = r['artist'] + " - " + r['title'] + " (" + r['label'] + "," + r['year'] + ")"
			print aRecordStr
			recordsListBox.insert(count, aRecordStr)
			count = count + 1
		return recordList["records"]
	
	
def learn():
	aCollectorName = collectorsComboBox.get()
	if(aCollectorName == ""):
		print "please select a collector"
	else:
		previousKnownRecords = getRecords()
		numRecordsToLearn = int(learnSpinbox.get())
		numRecordsLearned = 0
		print "learning " + str(numRecordsToLearn) + " records."
		
		webSearchTerms = []
		discogsSearchTerms = []
		for record in previousKnownRecords:
			webSearchTerms.append(record['artist'])
			discogsSearchTerms.append(record['artist'])
			print "added " + record['artist'] + " to search term list."
			
		while(numRecordsLearned < numRecordsToLearn):
			while(len(discogsSearchTerms) < 50):
				aSearchTerm = webSearchTerms.pop()
				
				print getWikipediaText(aSearchTerm)
				
				
	
	
	

controlPanel = Tk()

collectorNameListJson = urllib.urlopen("http://cratedigger.holotrash.com/api/cnamelist.php").read()
collectorNameList = json.loads(collectorNameListJson)
collectorsComboBox = ttk.Combobox(controlPanel);
collectorsComboBox.pack()

collectorNameArray = []

for p in collectorNameList["collectors"]:
	print p['name']
	collectorNameArray.append(p['name'])

collectorsComboBox['values'] = tuple(collectorNameArray)


recordsListBox = Listbox(controlPanel, width=100);
recordsListBox.pack()

getRecordsButton = Button(controlPanel, text="list records", command=getRecords)
getRecordsButton.pack()

labelInst = Label(controlPanel, text="Number of records to learn:")
labelInst.pack()

learnSpinbox = Spinbox(controlPanel, from_=0, to=500)
learnSpinbox.pack()

learnButton = Button(controlPanel, text="start learning", command=learn)
learnButton.pack()

statusLabel = Label(controlPanel, text="Crate Digger Learner v0.5")
statusLabel.pack() 


controlPanel.mainloop()
