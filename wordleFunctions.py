def printBanner(text):
    '''Standardized means of printing information to stdout.'''

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


def displayIntroduction():
    '''Prints explanation of Wordle and this solver.'''

    printBanner('Wordle Solver')

    print('\nEncoding scheme:')
    print(f"{'Match type':<25} {'Color':<20}{'Encoding'}")
    print(f"{'----------':<25} {'-----':<20}{'--------'}")
    print(f"{'Exact':<25} {'Green':<20}{'2'}")
    print(f"{'Inexact':<25} {'Yellow':<20}{'1'}")
    print(f"{'No match':<25} {'Gray':<20}{'0'}")

    print('\nExample:  \nIf the letters of a guess are colored (yellow, green, gray, gray, yellow),')
    print('the score to input into the solver should be \'12001\'.')

    return


def loadWordList():
    '''Load a list of words over which solving occurs.'''

    with open('wordleWordList.txt', 'r') as open_file:
        wordList = open_file.read().split()

    return wordList


def scoreGuess(guess, answer):
    '''Return a Wordle score for an input guessed word and answer.
    Encoding: exact match is scored as '2', inexact match is '1', and miss is '0'.'''

    guessList, answerList = list(guess), list(answer)
    remainingAnswerLetters = list(answer)

    score = len(guessList) * [0]

    # Find exact matches
    for i in range(len(guessList)):
        if guess[i] == answer[i]:
            score[i] = 2
            remainingAnswerLetters.remove(guess[i])

    # Find inexact matches
    for i in range(len(guessList)):
        if score[i] != 2 and guessList[i] in remainingAnswerLetters:
            score[i] = 1
            remainingAnswerLetters.remove(guessList[i])

    return score


def queryUser():
    '''Input guessed word and score.  Enforce proper input type.'''

    # Input word guessed
    while True:
        guess = str(input('\nWord guessed (or \'q\' to quit):\n>> ')).lower()

        if guess == 'q':
            printBanner('Exiting Wordle Solver.  Byeee.')
            exit()

        # Verify guess is of the appropriate form (5 letters)
        if len(list(guess)) == 5:
            break

        print('Incorrect number of letters.  Try again.')

    # Input score:  Check input length and either 0, 1, 2
    while True:
        score = input('Score of the guess:\n>> ')

        score = [int(a) for a in list(score)]  # convert string to list

        if len(score) == 5 and False not in [x in [0, 1, 2] for x in score]:
            break

        print('\nNot a possible Wordle score.  Try again.')

    return guess, score


def refineWordList(wordList, guess, score):
    '''Remove entries of a word list which would not produce a deisred score for a guessed word.'''

    return [w for w in wordList if scoreGuess(guess, w) == score]


def wordsContainLetters(wordList, letters):
    '''Returns words in wordList that contain desired letters.'''

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
    '''For a set of letters input by user, provide candidate words for next guess.'''

    printBanner('Next Guess Helper')
    print('\nEnter letters (or \'c\' to continue to next guess):')

    while True:
        letters = input('> ')
        if letters == 'c':
            break
        else:
            newList = wordsContainLetters(loadWordList(), letters)
            print(f'\n{len(newList)} possible words from the letters \'{letters}\': \n')
            printWordList(newList)

    return


def letterCount(wordlist):
    '''Given a list of words, compute letter frequency'''

    from collections import Counter, OrderedDict

    letterCount = Counter(''.join(wordlist))

    return OrderedDict(letterCount.most_common())


def updateKnownLetters(guess, score, placedList, unplacedList):
    '''Monkies'''

    guessList, scoreList = list(guess), list(score)

    remainingLetters = list(guess)

    # Check for exact matches
    for i in range(len(guessList)):
        if scoreList[i] == 2:
            placedList[i] = guessList[i]
            remainingLetters.remove(guessList[i])

    # Check for inexact matches
    for i in range(len(guessList)):
        if scoreList[i] == 1 and guessList[i] in remainingLetters:
            unplacedList.append(guessList[i])
            remainingLetters.remove(guessList[i])

    return placedList, unplacedList


def printWordList(wordList):
    ''''''

    width, gap = 10, 3

    while len(wordList) > 0:
        string = ''

        if len(wordList) >= width:
            temp = wordList[:width]
        else:
            temp = wordList

        for t in temp:
            string += t + gap * ' '

        print(string)

        wordList = wordList[width:]

    return


if __name__ == '__main__':

    # Some sample function calls to test functionality

    #print(scoreGuess('lymph', 'crimp'))

    #guess, score = queryUser()

    #c = refineWordList(loadWordList(), 'beast', [0,2,2,2,2])
    #print(c)

    #print(wordsContainLetters(loadWordList(), 'bhm'))

    #nextGuessHelper()

    #print(letterCount(['cat', 'cot']))

    displayIntroduction()
    print('Finished')