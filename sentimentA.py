from __future__ import division
import sys
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from time import sleep
import vlc
import csv
alchemy_language = AlchemyLanguageV1(api_key='2028a073cb9e01642fc80f06c315946833cdb0a2')


raw = []
paragraphs = []
sentiments = []
guesses = []
alchemyOutputs = []

#load alchemyOutputs
with open('alchemyRecords.txt', 'r') as f:
   alchemyOutputs = json.load(f)



filename = "handLabelledData.csv"
 
f = open(filename, 'rb') 
reader = csv.reader(f)
raw = list(reader) 
print("File Added")

#load tagged samples
for row in raw:
	sentiments.append(unicode(row[1], "utf-8"))
	paragraphs.append(unicode(row[0], "utf-8"))

#set accuracy checking variables
nbSuccess = 0
accuracy = 0

#sentiment analisys on samples
i = 0
for paragraph in paragraphs:
	#Right now only looking at 50 first paragraphs, TODO finish labelling
	if (i >= 50):
		break
	#print "SAMPLE # "
	#print i
	#print paragraph

	 #print(json.dumps(alchemy_language.emotion(text=paragraph), indent=2))
	#sentimentDict = alchemy_language.emotion(text=paragraph).get("docEmotions")
	#alchemyOutputs.append(alchemy_language.emotion(text=paragraph).get("docEmotions"))
	#print(sentimentDict.get("anger"))
	guess = max(alchemyOutputs[i].iterkeys(), key=(lambda key: alchemyOutputs[i][key]))

	#disgust is ignored
	if (guess == "disgust"):
		alchemyOutputs[i][guess] = 0.0
		guess = max(alchemyOutputs[i].iterkeys(), key=(lambda key: alchemyOutputs[i][key]))

	#if the greatest detected emotion is < 0.5 sample is seen as neutral
	if (alchemyOutputs[i][guess] < 0.5):
		guesses.append("Neutral")
	elif (guess == "joy"):
		guesses.append("Happiness")
	elif (guess == "fear"):
		guesses.append("Fear")
	elif (guess == "sadness"):
		guesses.append("Sadness")
	elif (guess == "anger"):
		guesses.append("Anger")
	else:
		print "WTF"
		print guess
	print i
	print(guesses[i])
	print(sentiments[i])
	print guesses[i] == sentiments[i]
	i = i +1

for j in range(0,i):	
	#print "guess: " + guesses[j]
	#print "true: "  + sentiments[j]
	if guesses[j] == sentiments[j]:
		nbSuccess = nbSuccess + 1
print "accuracy: "
print ((nbSuccess/i)*100)

#writing alchemy output in file
#with open('alchemyRecords.txt', 'w') as f:
#    json.dump(alchemyOutputs, f)

#print(json.dumps(alchemy_language.emotion(text=neutralScene), indent=2))
#print(json.dumps(alchemy_language.emotion(text=fearScene), indent=2))
'''
p = vlc.MediaPlayer("01. Thundertruck.mp3")
p.play()
for i in neutralScene:
	sleep(0.01)
	sys.stdout.write(i)
	sys.stdout.flush()
p.pause()
p = vlc.MediaPlayer("05 Alors On Danse (Radio Edit).mp3")
p.play()
for i in fearScene:
	sleep(0.01)
	sys.stdout.write(i)
	sys.stdout.flush()
'''
