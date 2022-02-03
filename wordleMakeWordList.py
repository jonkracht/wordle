# From an input dictionary, create a word list whose entries have the desired number of letters

nLetters = 5

# Obtained from: https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt
dictionaryFile = 'english-dictionary.txt'

wordListSaveName = 'wordleWordList.txt'

with open(dictionaryFile, 'r') as open_file:
    dictionary = open_file.read().split()

wordList = [word for word in dictionary if len(list(word)) == nLetters]

with open(wordListSaveName, 'w') as open_file:
    [open_file.write(w.lower() + '\n') for w in wordList]