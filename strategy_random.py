from strategy import Strategy
import random

class StrategyRandom(Strategy):

    def suggest_move(self, state):
        # return random.choice(state.possible_next_moves())

        state.computer_piece_not_used = max(state.computer_piece_not_used - 1, 0)
        print("each remained...", state.user_piece_not_used, state.computer_piece_not_used)

        if state.piece_not_used > 0:
            # random pick the first empty position.
            return (-1, -1), state.get_coords(0)[0]
        elif state.piece_not_used == 0 and state.pieces_left_onboard(state.current_player) > 3:
            # in Phase 2, random pick a piece that can move to its neighbor.
            for target in state.get_coords(2):
                neighbors = state.get_neighbors(target)
                print("in computer suggestion...", target, neighbors)
                for n in neighbors:
                    if n in state.get_coords(0):
                        return target, n 
            print("computer cannot figure out where to pick pieces and move...")
        elif state.piece_not_used == 0 and state.pieces_left_onboard(state.current_player) == 3:
            # in Phase 3, random pick a piece that can fly.
            target = state.get_coords(2)[0]
            new_move = state.get_coords(0)[0]
            return target, new_move