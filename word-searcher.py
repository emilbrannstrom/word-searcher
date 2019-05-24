import os #Enable underlying OS capabilities

#path to directory to scan for files
directory = '/Users/emilbrannstrom/Documents/dev/word-searcher/textfiles'

#create list of all files in directory
allFiles = os.listdir('textfiles/')

#prompt for keywords
keywords = input('Enter words to search for: ').lower().split()

nrOfKeywords = len(keywords)

keywordsInText = []

#create empty dictionary for pairing textfiles with number of keyword matches

results = {} 

#iterate through all textfiles in directory and search for keyword matches
for file in allFiles:
    #fileList = []
    path = (directory + '/' + file)
    if file.endswith('.txt'):
        with open(path, 'rt') as openFile: #open and automatically close file
            text = openFile.read().lower().split() #read text and split into single words
            uniqueWords = list(dict.fromkeys(text))
            for word in keywords: #for each keyword, do the following:
                if word in uniqueWords: #check if keyword matches any word in text
                    keywordsInText.append(word)
                    print(keywordsInText)
                    results[file] = len(keywordsInText) #add number of matches to corresponding file in dictionary
            keywordsInText = []
print('number of keywords: \n',nrOfKeywords) 

for key, value in results.items():
    results[key] = float(value)/float(nrOfKeywords) * 100

#show top 10 matched files and corresponding match ratio
print('Matches found in: \n',results)

"""
TODO: 
- Improve match ratio for each textfile. done
- Limit result to only show top 10.
- Transform to lowercase. done
"""
