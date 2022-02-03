import wordleFunctions as wf

def main():

    wf.displayIntroduction()

    wordList, allWords = wf.loadWordList(), wf.loadWordList()

    guessDict = {}

    placedLetters, unplacedLetters = 5 * ['-'], []

    while True:
        wf.printBanner('Guess ' + str(len(guessDict) + 1))
        guess, score = wf.queryUser()

        guessDict[guess] = score

        wordList = wf.refineWordList(wordList, guess, score)
        placedLetters, unplacedLetters = wf.updateKnownLetters(guess, score, placedLetters, unplacedLetters)

        wf.printBanner(f'After guess of \'{guess}\':')

        if len(wordList) == 0:
            # Handle case of all words eliminated
            print('No words match all input information.  Probably data entry error.  Please try again.')
            exit()
        elif len(wordList) == 1:
            print(f'Solution to the Wordle is: \'{wordList[0].upper()}\'!')
            exit()
        else:
            print(f'Placed letters in solution: {placedLetters}\n{unplacedLetters} remain to be placed')
            print(f'\n{len(wordList)} words remain as potential solutions:')
            print(wordList)

            letterCount = wf.letterCount(wordList)
            print(f'\nLetter counts of these words:\n{letterCount}')
            print(f'Top five letters neither placed nor unplaced:  {list(letterCount.keys())[0:5]}')

            wf.nextGuessHelper()

    return


if __name__ == '__main__':
    main()