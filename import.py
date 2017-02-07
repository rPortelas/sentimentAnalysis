import csv

raw = []
sentiment = []
paragraphs = []
newparagraphs = []

filename = "handLabelledData.csv"
 
f = open(filename, "rt", encoding= "utf-8")

reader = csv.reader(f)
raw = list(reader) 

#print(raw)	
print("File Added")

for row in raw:
	sentiment.append(row[1])
	paragraphs.append(row[0])

for i in paragraphs:
	newparagraphs.append(i.replace("\n", ""))

print(newparagraphs)
#print("Over")
#print(sentiment)