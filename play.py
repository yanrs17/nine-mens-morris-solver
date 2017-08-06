from state import * 

def play():
    firstMove = 0
    difficulty = 0
    while not firstMove:
        userChoice = input("Who takes the first move? 1: your move first; 2: computer move first: ")
        if userChoice == '1':
            firstMove = 1
            while not difficulty:
                userDifficulty = str(input('Please select difficulty of the game? e: easy; m: medium; h: hard '))
                difficulty = userDifficulty
                game = Game(firstMove=firstMove, difficulty=difficulty)
        elif userChoice == '2':
            firstMove = 2
            while not difficulty:
                userDifficulty = str(input('Please select difficulty of the game? e: easy; m: medium; h: hard '))
                difficulty = userDifficulty
                game = Game(firstMove=firstMove, difficulty=difficulty)
    game.start()

play()