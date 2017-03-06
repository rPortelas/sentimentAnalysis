#increment the true positive of the given sentiment
def incTruePos(sentiment):
	print(sentiment)
	if(sentiment == "Anger"):
		print("+1 anger")
		truePos[0] += 1
	elif(sentiment == "Fear"):
		print("+1 fear")
		truePos[1] += 1
	elif(sentiment == "Happiness"):
		print("+1 happiness")
		truePos[2] += 1
	elif(sentiment == "Sadness"):
		print("+1 sadness")
		truePos[3] += 1
	elif(sentiment == "Neutral"):
		print("+1 neutral")
		truePos[4] += 1
		print("done")
		print(truePos[0])
		print(truePos[1])
		print(truePos[2])
		print(truePos[3])
		print(truePos[4])
	else:
		print "WTF incTruePos"
		print sentiment
#set arrays to compute ROC curve
#{Anger, Fear, Happiness, Sadness, Neutral}
truePos = [0,0,0,0,0]
incTruePos("Fear")
incTruePos("Anger")
incTruePos("Anger")

for k in range(0,4):
	print truePos[k]
	#print falseNeg[k]
truePos[3] += 1 
print truePos[3]
	#sensitivity = (truePos[k] * 100) / (truePos[k] + falseNeg[k])
print(sensitivity)

