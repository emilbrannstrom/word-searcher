import os #Enable underlying OS capabilities

#path to directory to scan for files
directory = '/Users/emilbrannstrom/Documents/dev/word-searcher/textfiles'

#create list of all files in directory
allFiles = os.listdir('textfiles/')

#prompt for keywords
keywords = input('Enter words to search for: ').split()

nrOfKeywords = len(keywords)

count = 0

#create empty dictionary for pairing textfiles with number of keyword matches
results = {} 

#iterate through all textfiles in directory and search for keyword matches
for file in allFiles:
    path = (directory + '/' + file)
    if file.endswith('.txt'):
        with open(path, 'r') as openFile: #open and automatically close file
            text = openFile.read().split() #read text and split into single words
            uniqueWords = list(dict.fromkeys(text))
            for word in keywords: #for each keyword, do the following:
                if word in uniqueWords: #check if keyword matches any word in text
                    count += 1
                    results[file] = count #add number of matches to corresponding file in dictionary
                    
print('number of keywords: \n',nrOfKeywords)

for key, value in results.items():
    results[key] = float(value)/float(nrOfKeywords) * 100

#show top 10 matched files and corresponding match ratio
print('Matches found in: \n',results)

"""
TODO: 
- Improve match ratio for each textfile.
- Limit result to only show top 10.
- Fix upper limit on counter.
- Transform to lowercase.
"""
