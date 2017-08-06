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
            if self.state.current_player == 'u': # user's turn
                if self.state.piece_not_used > 0:
                    # in Phase 1, place pieces.
                    new_move = self.state.get_move(phase = 1)
                    while self.state.is_valid_move(new_move, phase = 1):
                        print("Illegal move: ({}, {}), please give a valid cordinates.".format(new_move[0], new_move[1]))
                        print(self.instruction())
                        print(self.state)
                        new_move = self.state.get_move(phase = 1)
                    print("You choose a valid position ({}, {})".format(new_move[0], new_move[1]))
                elif self.state.piece_not_used == 0 and self.state.pieces_left_onboard(self.state.grid, self.state.current_player) > 3:
                    # in Phase 2, move pieces.
                    target, new_move = self.state.get_move(phase = 2)
                    while self.state.is_valid_move(new_move, phase = 2, target = target):
                        print("Illegal move or invalid target piece, please give a valid cordinates.")
                        print(self.instruction())
                        print(self.state)
                        target, new_move = self.state.get_move(phase = 2)

                    


