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
            print('No words match all criteria.  Likely data entry error.  Please try again.')
            exit()
        elif len(wordList) == 1:
            print(f'\nSolution is:  \'{wordList[0].upper()}\'')
            exit()
        else:
            print(f"\n{'Placed letters:':<25}{placedLetters}")
            print(f"{'Unplaced letters:':<25}{unplacedLetters}")

            print(f'\n{len(wordList)} words remain as potential solutions:\n')
            wf.printWordList(wordList)

            letterCount = wf.letterCount(wordList)
            print(f'\nLetter counts of these words:\n{letterCount}')

            temp = []
            for key, val in letterCount.items():
                if key not in unplacedLetters and key not in placedLetters:
                    temp.append(key)
                    if len(temp) > 4:
                        break

            print(f'\nTop five letters neither placed nor unplaced:')
            wf.printWordList(temp)



            wf.nextGuessHelper()

    return


if __name__ == '__main__':
    main()