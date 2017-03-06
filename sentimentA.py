from __future__ import division
import sys
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from time import sleep
import vlc
import csv

#increment the true positive of the given sentiment
def incTruePos(sentiment):
	if(sentiment == "Anger"):
		truePos[0] += 1
	elif(sentiment == "Fear"):
		truePos[1] += 1
	elif(sentiment == "Happiness"):
		truePos[2] += 1
	elif(sentiment == "Sadness"):
		truePos[3] += 1
	elif(sentiment == "Neutral"):
		truePos[4] += 1
	else:
		print "WTF incTruePos"
		print sentiment

#increment falsePos of the given sentiment
def incFalsePos(sentiment):
	if(sentiment == "Anger"):
		falsePos[0] += 1
	elif(sentiment == "Fear"):
		falsePos[1] += 1
	elif(sentiment == "Happiness"):
		falsePos[2] += 1
	elif(sentiment == "Sadness"):
		falsePos[3] += 1
	elif(sentiment == "Neutral"):
		falsePos[4] += 1
	else:
		print "WTF incFalsePos"

#increment trueNeg of all but the given sentiment(s)
def incTrueNegAllBut(sentiments):
	if(not("Anger" in sentiments)):
		trueNeg[0] += 1
	if(not("Fear" in sentiments)):
		trueNeg[1] += 1
	if(not("Happiness" in sentiments)):
		trueNeg[2] += 1
	if(not("Sadness" in sentiments)):
		trueNeg[3] += 1
	if(not("Neutral" in sentiments)):
		trueNeg[4] += 1

#increment falseNeg of given sentiment
def incFalseNeg(sentiment):
	if(sentiment == "Anger"):
		falseNeg[0] += 1
	elif(sentiment == "Fear"):
		falseNeg[1] += 1
	elif(sentiment == "Happiness"):
		falseNeg[2] += 1
	elif(sentiment == "Sadness"):
		falseNeg[3] += 1
	elif(sentiment == "Neutral"):
		falseNeg[4] += 1
	else:
		print "WTF incFalseNeg"
		print sentiment


alchemy_language = AlchemyLanguageV1(api_key='7ee2d55604ee59df13c9a315603405291131cf6e')
raw = []
paragraphs = []
sentiments = []
guesses = []
alchemyOutputs = []

#load alchemyOutputs
#with open('alchemyRecords.txt', 'r') as f:
#   alchemyOutputs = json.load(f)



filename = "handLabelledData.csv"
 
f = open(filename, 'rb') 
reader = csv.reader(f)
raw = list(reader) 
print("File Added")

#load tagged samples
for row in raw:
	sentiments.append(unicode(row[1], "utf-8"))
	paragraphs.append(unicode(row[0], "utf-8"))


#sentiment analisys on samples
i = 0
for paragraph in paragraphs:
	#Right now only looking at 50 first paragraphs, TODO finish labelling
	if (i >= 50):
		break

	print(json.dumps(alchemy_language.emotion(text=paragraph), indent=2))
	sentimentDict = alchemy_language.emotion(text=paragraph).get("docEmotions")
	alchemyOutputs.append(alchemy_language.emotion(text=paragraph).get("docEmotions"))
	guess = max(alchemyOutputs[i].iterkeys(), key=(lambda key: alchemyOutputs[i][key]))

	#disgust is ignored
	if (guess == "disgust"):
		alchemyOutputs[i][guess] = 0.0
		guess = max(alchemyOutputs[i].iterkeys(), key=(lambda key: alchemyOutputs[i][key]))

	#if the greatest detected emotion is < 0.5 sample is seen as neutral
	if (float(alchemyOutputs[i][guess]) < .55):
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

#set accuracy checking variables
nbSuccess = 0
accuracy = 0
#set arrays to compute ROC curve
#{Anger, Fear, Happiness, Sadness, Neutral}
truePos = [0,0,0,0,0]
falsePos = [0,0,0,0,0]
trueNeg = [0,0,0,0,0]
falseNeg = [0,0,0,0,0]
sensitivity = [0.,0.,0.,0.,0.]
specificity = [0.,0.,0.,0.,0.]
for j in range(0,i):	
	#print "guess: " + guesses[j]
	#print "true: "  + sentiments[j]
	if guesses[j] == sentiments[j]:
		nbSuccess = nbSuccess + 1
		nb = 0
		incTruePos(guesses[j])
		print(truePos)
		incTrueNegAllBut([guesses[j]])
	else:
		incFalseNeg(sentiments[j])
		incFalsePos(guesses[j])
		incTrueNegAllBut([guesses[j],sentiments[j]])

	#TODO handle anxiousness
	#if guesses[j] == "Fear" && sentiments[j] == "Anxious"
print "accuracy: "
print ((nbSuccess/i)*100)
for k in range(0,5):
	print(trueNeg)
	print(falsePos)
	if(truePos[k] == 0 & falseNeg[k] == 0):
		#No data on this label
		continue
	sensitivity[k] = (truePos[k] * 100) / (truePos[k] + falseNeg[k])
	specificity[k] = (trueNeg[k] * 100) / (trueNeg[k] + falsePos[k])
print "sensitivity: "
print(sensitivity)
print "specificity: "
print(specificity)


	

#writing alchemy output in file
#with open('alchemyRecords.txt', 'w') as f:
#    json.dump(alchemyOutputs, f)

#print(json.dumps(alchemy_language.emotion(text=neutralScene), indent=2))
#print(json.dumps(alchemy_language.emotion(text=fearScene), indent=2))

#p = vlc.MediaPlayer("01. Thundertruck.mp3")
#p.play()
#sleep(10)

