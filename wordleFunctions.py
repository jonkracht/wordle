def printBanner(text):
    ''''''

    bannerMarker = '*'
    bannerWidth = 80
    gap = 3

    leftFill = int((bannerWidth - len(text) - 2 * gap)/2)
    rightFill = bannerWidth - leftFill - len(text) - 2*gap

    print('\n')
    print(bannerWidth * bannerMarker)
    print(leftFill * bannerMarker + gap * ' ' + text + gap * ' ' + rightFill * bannerMarker)
    print(bannerWidth * bannerMarker)

    return()


def loadWordList():
    '''Load a list of words'''

    with open('wordleWordList.txt', 'r') as open_file:
        wordList = open_file.read().split()

    return wordList


def scoreGuess(guess, answer):
    '''Return a Wordle score for an input guessed word and answer.
    Encoding is exact match is '2', inexact match is '1' and miss is '0'.'''

    guessList, answerList = list(guess), list (answer)
    remainingAnswerLetters = list(answer)

    score = len(guessList) * [0]

    # Check for exact matches
    for i in range(len(guessList)):
        if guess[i] == answer[i]:
            score[i] = 2
            remainingAnswerLetters.remove(guess[i])

    # Check for inexact matches
    for i in range(len(guessList)):
        if score[i] != 2 and guessList[i] in remainingAnswerLetters:
            score[i] = 1
            remainingAnswerLetters.remove(guessList[i])

    return score


def queryUser():

    guess = str(input('Wordle guess: ')).lower()
    score = input('Score: ')

    score = [int(a) for a in list(score)]

    return guess, score


def refineWordList(wordList, guess, score):
    '''Remove entries in a word list which do not mach guess/score.'''

    newWordList = [w for w in wordList if scoreGuess(guess, w) == score]

    return newWordList


def wordsContainLetters(wordList, letters):
    '''Returns words who contain desired letters.'''

    newList = []

    letters = list(letters)

    for word in wordList:
        hasAllLetters = True
        for l in letters:
            if l not in word:
                hasAllLetters = False

        if hasAllLetters:
            newList.append(word)

    return newList


def nextGuessHelper():
    '''Provide candidate next guesses based on letters input by user.'''

    printBanner('Helper for next guess')

    while True:
        letters = input('\nEnter letters (or \'c\' to continue): ')
        if letters == 'c':
            break
        else:
            newList = wordsContainLetters(loadWordList(), letters)
            print(f'{len(newList)} words contain these letters: ', newList)

    return


if __name__ == '__main__':

    #print(scoreGuess('lymph', 'crimp'))

    #guess, score = queryUser()

    #c = refineWordList(loadWordList(), 'beast', [0,2,2,2,2])
    #print(c)

    #print(wordsContainLetters(loadWordList(), 'bhm'))

    nextGuessHelper()

    print('Finished')