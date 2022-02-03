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
    ''''''
    printBanner('Wordle Solver')
    print('When a word is guessed, the guess is evaluated and each letter of the guess is shaded in either yellow, green, or grey.')
    print('These colors indicate to what degree each letter appears in the solution word.')
    print('\nIn this solver, the following encoding is used: \ngreen is 2, yellow is 1, and grey is 0')

    return


def loadWordList():
    '''Load a list of words over which solving occurs.'''

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
    '''Grabs the user's guess and score of guess.'''

    guess = str(input('Word guessed (or \'q\' to quit): ')).lower()

    if guess == 'q':
        printBanner('Exiting Wordle Solver.  Byeee.')
        exit()

    score = input('Score of the guess: ')

    score = [int(a) for a in list(score)]

    return guess, score


def refineWordList(wordList, guess, score):
    '''Remove entries of a word list which do not mach guess/score.'''

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
    print('\nEnter letters (or \'c\' to continue to next guess):')
    while True:
        letters = input('> ')
        if letters == 'c':
            break
        else:
            newList = wordsContainLetters(loadWordList(), letters)
            print(f'{len(newList)} words contain these letters: \n', newList)

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


if __name__ == '__main__':

    # Some sample function calls to test functionality

    #print(scoreGuess('lymph', 'crimp'))

    #guess, score = queryUser()

    #c = refineWordList(loadWordList(), 'beast', [0,2,2,2,2])
    #print(c)

    #print(wordsContainLetters(loadWordList(), 'bhm'))

    #nextGuessHelper()

    print(letterCount(['cat', 'cot']))

    print('Finished')