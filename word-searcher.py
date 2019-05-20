import os #OS module enables underlying OS capabilities
import heapq #Heapq module enables heap data structure to find n largest values in a dataset

directory = '/Users/emilbrannstrom/Documents/dev/word-searcher/textfiles'

#create dictionary with textfiles as key and their associated keyword count as value
fileDict = {} 

matchingWords = []

numberOfMatches = len(matchingWords)

#list all files in directory
allFiles = os.listdir('textfiles/')

print('Text files found in directory: ' + str(allFiles))

#prompt for keywords and split them
keywords = raw_input('Enter words to search for: ').split()
if len(keywords) == 0:
    print('No keyword given')
print('Your keywords: ' + str(keywords))



#iterate through all textfiles in directory
for file in allFiles:
    path = (directory + '/' + file)
    if file.endswith('.txt'):
        with open (path, 'rt') as openFile: #rt = Read Text and close file  
            for line in openFile:
                for word in line.split():
                    if word in keywords:
                        matchingWords.append(word)
                        fileDict[file] = len(matchingWords)
            print('Matches found in ' + file + ' :' + str(matchingWords))

print fileDict
topTen = heapq.nlargest(10, fileDict, len(matchingWords()))
print("Top 10 files matching your keywords:") 
print topTen
"""
numberOfKeywords = len(keywords)

matchPercentage = numberOfMatches/float(numberOfKeywords)

print('Number of matches: ' + str(numberOfMatches))
if len(matchingWords) < 1:
    print('Matches found: none')
else: 
    print('Matches found: ' + str(matchingWords))
print('Percentage of your words that were found: ' + str(matchPercentage*100))"""
