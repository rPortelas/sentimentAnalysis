from __future__ import division
import sys
import json
from os.path import join, dirname
from time import sleep
import vlc
import csv

from IBMAlchemyAnalysis import alchemyAnalysis

#increment the true positive of the given sentiment
def incTruePos(sentiment, truePos):
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
def incFalsePos(sentiment, falsePos):
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
def incTrueNegAllBut(sentiments, trueNeg):
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
def incFalseNeg(sentiment, falseNeg):
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


def displayPerformanceAnalysis(guesses, targets):
	#set accuracy checking variables
	nbSuccess = 0
	accuracy = 0
	#set arrays to compute sensitivity / specificity
	#{Anger, Fear, Happiness, Sadness, Neutral}
	truePos = [0,0,0,0,0]
	falsePos = [0,0,0,0,0]
	trueNeg = [0,0,0,0,0]
	falseNeg = [0,0,0,0,0]
	sensitivity = [0.,0.,0.,0.,0.]
	specificity = [0.,0.,0.,0.,0.]

	#i refers to the number of guesses
	i = len(guesses)
	for j in range(0,i):	
		if guesses[j] == targets[j]:
			nbSuccess = nbSuccess + 1
			nb = 0
			incTruePos(guesses[j], truePos)
			print(truePos)
			incTrueNegAllBut([guesses[j]], trueNeg)
		else:
			incFalseNeg(targets[j], falseNeg)
			incFalsePos(guesses[j], falsePos)
			incTrueNegAllBut([guesses[j],targets[j]], trueNeg)
		#TODO handle anxiousness
		#if guesses[j] == "Fear" && sentiments[j] == "Anxious"
	print "accuracy: "
	print ((nbSuccess/i)*100)
	for k in range(0,5):
		if(truePos[k] == 0 & falseNeg[k] == 0):
			#No data on this label
			continue
		sensitivity[k] = (truePos[k] * 100) / (truePos[k] + falseNeg[k])
		specificity[k] = (trueNeg[k] * 100) / (trueNeg[k] + falsePos[k])
	print "sensitivity: "
	print(sensitivity)
	print "specificity: "
	print(specificity)

def loadAccuracyDataset(fileName, data, labels):
	raw = []
	f = open(fileName, 'rb') 
	reader = csv.reader(f)
	raw = list(reader) 
	print("Accuracy Dataset Added")

	#load tagged samples
	for row in raw:
		labels.append(unicode(row[1], "utf-8"))
		data.append(unicode(row[0], "utf-8"))



#MAIN PART
paragraphs = []
sentiments = []
loadAccuracyDataset("handLabelledData.csv", paragraphs, sentiments)

#Run IBM Alchemy API Analysis
guesses = alchemyAnalysis(paragraphs)
displayPerformanceAnalysis(guesses, sentiments)



#p = vlc.MediaPlayer("01. Thundertruck.mp3")
#p.play()
#sleep(10)