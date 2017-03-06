emotions=["anger", "anticipation", "disgust", "fear", "joy", "sadness", "trust", "surprise"]
wordEmotions = {}
with open("NRC-Emotion-Lexicon-Wordlevel-v0.92.txt") as f:
    prevWord = "NULL"
    for line in f:
       #(key, val) = line.split()
       #d[int(key)] = val
       curWord = line[0]
       emotion = line[1]
       print(curWord)

       #if current word different from the previous one,
       #let's create a new entry in our map
       if(curWord != prevWord):
           wordEmotions[curWord] = [0,0,0,0,0,0,0,0]
       print(emotion)
       if emotion in emotions:
           print emotions.index(emotion)
       print line
       prevWord = curWord