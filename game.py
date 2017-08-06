from state import State

class Game:
    """
    Game class, use State class from state.py to simulate a game.
    """
    def __init__(self, state, strategy):
        """
        player:
            "c": computer
            "u": user
        
        state:
            import from state.py,

        """
        player = ''
        while player not in ['c', 'u']:
            player = input('Who plays first? c: computer plays first; u: user plays first')
        
        self.state = state(player, is_new = True) # init game state.
        self.strategy = strategy() # init strategy

    def play(self):
        print("Game init...")
        print(self.state)
        while not self.state.over:
            if self.state.current_player == 'u': 
                # user's turn.
                if self.state.piece_not_used > 0:
                    # in Phase 1, place pieces.
                    new_move = self.state.get_move(phase = 1)
                    while self.state.is_valid_move(new_move, phase = 1):
                        print("Illegal move: ({}, {}), please give a valid cordinates.".format(new_move[0], new_move[1]))
                        print(self.instruction())
                        print(self.state)
                        target, new_move = self.state.get_move(phase = 1)
                    print("You choose a valid position ({}, {}) to add a new piece.".format(new_move[0], new_move[1]))
                elif self.state.piece_not_used == 0 and self.state.pieces_left_onboard(self.state.grid, self.state.current_player) > 3:
                    # in Phase 2, move pieces.
                    target, new_move = self.state.get_move(phase = 2)
                    while self.state.is_valid_move(new_move, phase = 2, target = target):
                        print("Illegal move or invalid target piece, please give a valid cordinates.")
                        print(self.instruction())
                        print(self.state)
                        target, new_move = self.state.get_move(phase = 2)
                    print("You pick piece at ({}, {}) to move to ({}, {})".format(target[0], target[1], new_move[0], new_move[1]))
                elif self.state.piece_not_used == 0 and self.state.pieces_left_onboard(self.state.grid, self.state.current_player) == 3:
                    # in Phase 3, fly pieces.
                    target, new_move = self.state.get_move(phase = 3)
                    while self.state.is_valid_move(new_move, phase = 3, target = target):
                        print("Illegal move or invalid target piece, please give a valid cordinates.")
                        print(self.instruction())
                        print(self.state)
                        target, new_move = self.state.get_move(phase = 3)
                    print("You pick piece at ({}, {}) to fly to ({}, {})".format(target[0], target[1], new_move[0], new_move[1]))
            else:
                # computer's turn.
                # assume now computer simply random pick a empty position and put pieces or move or fly.
                target, new_move = self.strategy.suggest_move(self.state)
                if target == (-1, -1): 
                    # in Phase 1.
                    print("Computer place a piece at ({}, {})".format(new_move[0], new_move[1]))
                else:
                    # in Phase 2 or 3.
                    print("Computer pick piece at ({}, {}) to move or fly to ({}, {})".format(target[0], target[1], new_move[0], new_move[1]))
            
            # start to apply the target and new_move into new state.
            self.state = self.state.apply_target_and_move(target, new_move)
            print("New game state: ", str(self.state), "\n")

        # if game is over.
        if self.state.winner == 'u':
            print("You beats computer!")
        elif self.state.winner == 'c':
            print("Computer wins!")
        else:
            print("Tie...")

if __name__ == '__main__':
    from state import State
    from strategy_random import StrategyRandom
    Game(State, StrategyRandom).play()
                    


