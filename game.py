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
                



