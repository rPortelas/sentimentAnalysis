import csv

raw = []
sentiment = []
paragraphs = []
newparagraph = []

filename = "handLabelledData.csv"
 
f = open(filename, 'rb') 
reader = csv.reader(f)
raw = list(reader) 

#print(raw)	
print("File Added")

for row in raw:
	sentiment.append(row[1])
	paragraphs.append(row[0])

for i in paragraphs:
	newparagraph.append(unicode(i, "utf-8"))

print(newparagraph)
#print("Over")
#print(sentiment)