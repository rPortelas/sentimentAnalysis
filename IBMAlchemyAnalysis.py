from __future__ import division
import sys
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from time import sleep
import csv

#return emotion guesses for paragraphs
def alchemyAnalysis(paragraphs):
	alchemy_language = AlchemyLanguageV1(api_key='7ee2d55604ee59df13c9a315603405291131cf6e')
	guesses = []
	alchemyOutputs = []

	#load alchemyOutputs
	with open('alchemyRecords.txt', 'r') as f:
	   alchemyOutputs = json.load(f)

	#sentiment analisys on samples
	i = 0
	for paragraph in paragraphs:
		#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		#WARNING Right now only looking at 50 first paragraphs, TODO finish labelling !!!!!!!!!!!!!!!!!!!!!!!!!!
		if (i >= 50):
			break

		##print(json.dumps(alchemy_language.emotion(text=paragraph), indent=2))
		##sentimentDict = alchemy_language.emotion(text=paragraph).get("docEmotions")
		##alchemyOutputs.append(alchemy_language.emotion(text=paragraph).get("docEmotions"))
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
		i = i +1
	#writing alchemy output in file
	#with open('alchemyRecords.txt', 'w') as f:
	#    json.dump(alchemyOutputs, f)
	return guesses
