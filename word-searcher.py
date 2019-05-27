import os #Enable underlying OS capabilities

#Path to directory to scan for files
directory = '/Users/emilbrannstrom/Documents/dev/word-searcher/textfiles'

#Create list of all files in directory
allFiles = os.listdir('textfiles/')

#Prompt for keywords
keywords = input('Enter words to search for: ').lower().split()

nrOfKeywords = len(keywords)

keywordsInText = []

#Create empty dictionary for pairing textfiles with number of keyword matches
results = {} 

#Iterate through all textfiles in directory and search for keyword matches
for file in allFiles:
    path = (directory + '/' + file)
    if file.endswith('.txt'):
        with open(path, 'rt') as openFile: #Open and automatically close file
            text = openFile.read().lower().split() #Read text and split into single words
            uniqueWords = list(dict.fromkeys(text)) #Remove duplicate words
            for word in keywords: #For each keyword, do the following:
                if word in uniqueWords: #Check if keyword matches any word in text
                    keywordsInText.append(word)
                    results[file] = len(keywordsInText) #Add number of matches to corresponding file in dictionary
            keywordsInText = [] #Flush keywords

for key, value in results.items():
    results[key] = float(value)/float(nrOfKeywords) * 100

#Transform results into a sorted list, and then back into a dictionary
sortedResults = dict(sorted(results.items(), key=lambda x: x[1], reverse=True)) 

#Show matched files and corresponding match ratio
counter = 0
for key, value in sortedResults.items():
    counter += 1
    print(int(value),'% match in ',key)
    if counter > 9:
        break

"""
TODO: 
- Show hits with 0 % in output.
"""

