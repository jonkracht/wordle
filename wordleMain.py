import wordleFunctions as wf

def main():

    wf.printBanner('Wordle Solver')

    wordList, allWords = wf.loadWordList(), wf.loadWordList()

    guessDict = {}

    while True:
        wf.printBanner('Guess ' + str(len(guessDict) + 1))
        guess, score = wf.queryUser()

        guessDict[guess] = score

        wordList = wf.refineWordList(wordList, guess, score)

        print(f'\nAfter guess of \'{guess}\', {len(wordList)} words remain as potential solutions:')
        print(wordList)

        wf.nextGuessHelper()

    return


if __name__ == '__main__':
    main()