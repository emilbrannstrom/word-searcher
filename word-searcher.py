#provide underlying operative system functionality
#to enable path to directory
#(prova utan denna och se vad som haender)
#from os import path

#import regular expressions module
import re

#pathToFile = path.relpath('/textfiles/romeo.txt')
#open all files in a directory containing textfiles
#(borjar med en fil)

#//////// add nordic character encoding /////////////
#//////// currently textfiles are in current path
# fix so that they are in a subdirectory /////////////
#import OS module to enable underlying OS capabilities
import os

directory = '/Users/emilbrannstrom/Documents/dev/word-searcher/textfiles'

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
            print('Matches found in ' + file + ' :' + str(matchingWords))
            dictionary = {file : len(matchingWords)}
            print dictionary
                    

numberOfKeywords = len(keywords)

matchPercentage = numberOfMatches/float(numberOfKeywords)

#print('Number of keywords: ' + str(numberOfKeywords))
print('Number of matches: ' + str(numberOfMatches))
if len(matchingWords) < 1:
    print('Matches found: none')
else: 
    print('Matches found: ' + str(matchingWords))
print('Percentage of your words that were found: ' + str(matchPercentage*100))
