import re

#open the input file
with open("declaration.txt", 'r') as inFile:
    lines = inFile.readlines()

#find all words in text file
words = re.findall('\w+', open('declaration.txt').read().lower())

#assign words to hashtable, where we assign 'word : count' as 'ket : value'
wordList = {}
for word in words:
    if word not in wordList:
        wordList[word] = 0
    wordList[word] += 1

#write output file 'key : value' alphabetical order
with open("myOutput.txt", 'w') as outFile:
    for key in sorted(wordList.keys()):
        outFile.write(key + ' ' + str(wordList[key]) + '\n')