from state import * 

def main():
    firstMove = 0
    difficulty = 0
    while not firstMove:
        userChoice = input('Who takes the first move? 1: your move first; 2: computer move first: ')
        if userChoice == '1':
            firstMove = 1
            while not difficulty:
                userDifficulty = input('Please select difficulty of the game? e: easy; m: medium; h: hard ')
                if userDifficulty == 'e':
                    difficulty = 1
                elif userDifficulty == 'm':
                    difficulty = 2
                elif userDifficulty == 'h':
                    difficulty = 3
                else:
                    continue
                game = Game(firstmove=firstMove, difficulty=difficulty)
        elif userChoice == '2':
            firstMove = 2
            while not difficulty:
                userDifficulty = input('Please select difficulty of the game? e: easy; m: medium; h: hard ')
                if userDifficulty == 'e':
                    difficulty = 1
                elif userDifficulty == 'm':
                    difficulty = 2
                elif userDifficulty == 'h':
                    difficulty = 3
                else:
                    continue
                game = Game(firstmove=firstMove, difficulty=difficulty)
    game.start()

main()