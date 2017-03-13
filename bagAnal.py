

emotions=["anger", "anticipation", "disgust", "fear", "joy", "sadness", "trust", "surprise"]
wordEmotions = {}

def load_emolex(fileName):
	#open EmoLex file and load it in wordEmotions dictionary
	with open(fileName) as f:
	    prevWord = "NULL"
	    for line in f:
	       elements = line.split()
	       curWord = elements[0]
	       emotion = elements[1]
	       emotionValue = elements[2]
	       print emotionValue

	       #if current word different from the previous one,
	       #let's create a new entry in our map
	       if(curWord != prevWord):
	           wordEmotions[curWord] = [0,0,0,0,0,0,0,0]

	       if (emotionValue == "1") and (emotion in emotions):
	       		#get index that we need to increment
	       		index = emotions.index(emotion)

	       		#get old array and update it
	       		newValues = wordEmotions[curWord]
	       		newValues[index] += 1
	       		wordEmotions[curWord] = newValues      
	       prevWord = curWord

	#print dictionary
	for a in wordEmotions:
		print(a)
		print(wordEmotions[a])



#load emoLex from file
load_emolex("NRC-Emotion-Lexicon-Wordlevel-v0.92.txt")





