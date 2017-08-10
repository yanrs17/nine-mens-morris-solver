
from state import State
import random

class AutoGame:
    """
    AutoGame class, use State class and let different strategy compete with each other.
    """
    def __init__(self, state, strategy1, strategy2):
        """
        player:
            "u": strategy1
            "c": strategy2
        
        state:
            import from state.py,

        """
        player = random.choice(['c', 'u']) # random select which to start.
        
        self.user_pieces_num = 9
        self.computer_pieces_num = 9

        self.state = state(player, is_new = True, grid = [], user_pieces_num = 9, computer_pieces_num = 9)
        self.strategy1 = strategy1() # init strategy
        self.strategy2 = strategy2() 

    def play(self):
        print("Game init...")
        print(self.state)
        while not self.state.over:
            if self.state.current_player == 'u': 
                # apply strategy 1.
                print("Strategy {}'s turn".format(self.strategy1.name))
                if not self.state.get_successors():
                    # if return no choice for computer, then user wins!
                    print("Strategy {} wins!".format(self.strategy2.name))
                    return 
                new_grid = self.strategy1.suggest_move(self.state)

                # strategy 1 less piece_not_used.
                self.state.user_piece_not_used = max(self.state.user_piece_not_used - 1, 0)
                print("Strategy {} remained pieces not used...".format(self.strategy1.name), self.state.user_piece_not_used, "; Strategy {} remained pieces not used...".format(self.strategy2.name), self.state.computer_piece_not_used)

                self.state = State(self.state.opponent, is_new = False, grid = new_grid, user_pieces_num = self.state.user_piece_not_used, computer_pieces_num = self.state.computer_piece_not_used)

            else:
                # apply strategy 2.
                print("Strategy {}'s turn".format(self.strategy2.name))
                if not self.state.get_successors():
                    # if return no choice for computer, then user wins!
                    print("Strategy {} wins!".format(self.strategy1.name))
                    return 
                new_grid = self.strategy2.suggest_move(self.state)

                # strategy 2 less piece_not_used.
                self.state.computer_piece_not_used = max(self.state.computer_piece_not_used - 1, 0)
                print("Strategy {} remained...".format(self.strategy1.name), self.state.user_piece_not_used, "; Strategy {} remained...".format(self.strategy2.name), self.state.computer_piece_not_used)

                self.state = State(self.state.opponent, is_new = False, grid = new_grid, user_pieces_num = self.state.user_piece_not_used, computer_pieces_num = self.state.computer_piece_not_used)
            
            # # start to apply the target and new_move into new state.
            print("New game state: \n")
            print(self.state)

        # if game is over.
        if self.state.winner == 'u':
            print("Strategy {} wins!".format(self.strategy1.name))
        elif self.state.winner == 'c':
            print("Strategy {} wins!".format(self.strategy2.name))
        else:
            print("Tie...")