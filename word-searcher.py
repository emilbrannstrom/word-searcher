import os #OS module enables underlying OS capabilities
from heapq import nlargest

#path to directory to scan for files
directory = '/Users/emilbrannstrom/Documents/dev/word-searcher/textfiles'

#list all files in directory
allFiles = os.listdir('textfiles/')

#prompt for keywords and split them
keywords = raw_input('Enter words to search for: ').split()

#create empty dictionary for pairing textfiles with associated keyword count
fileDictionary = {} 

#list to store matching words in
matchingWords = [] 

#iterate through all textfiles in directory and search for keyword matches
for file in allFiles:
    path = (directory + '/' + file)
    if file.endswith('.txt'):
        with open (path, 'rt') as openFile: #rt = Read Text and close file  
            for line in openFile:
                for word in line.split():
                    if word in keywords: #add any matching words to list
                        matchingWords.append(word)
                        fileDictionary[file] = len(matchingWords) #add number of matches to corresponding file in dictionary

#remove duplicates from dictionary
matchingWords = list(dict.fromkeys(matchingWords))

#get matching words ratio
matchRatio = float(len(matchingWords))/len(keywords)*100

print "Matches found: ", len(matchingWords)
print "Match percentage: ", matchRatio, "%"

"""TODO: Fix match ratio for each textfile in the top 10 list."""

print'Matches found in: ', file

#list top 10 files where keywords match
top10 = nlargest(10, fileDictionary, key=fileDictionary.get)
if len(matchingWords) > 0:
    print("Top 10 files matching your keywords:")
    print top10
