from strategy import Strategy
import random

class StrategyRandom(Strategy):

    def suggest_move(self, state):
        # return random.choice(state.possible_next_moves())

        if self.state.piece_not_used > 0:
            # random pick the first empty position.
            return (-1, -1), self.state.get_coords(0)[0]
        elif self.state.piece_not_used == 0 and self.state.pieces_left_onboard(self.state.grid, self.state.current_player) > 3:
            # in Phase 2, random pick a piece that can move to its neighbor.
            for target in self.state.get_coords(2):
                neighbors = self.state.get_neighbors(target)
                for n in neighbors:
                    if n in self.state.get_coords(0)
                        return target, n 
            print("computer cannot figure out where to pick pieces and move...")
        elif self.state.piece_not_used == 0 and self.state.pieces_left_onboard(self.state.grid, self.state.current_player) == 3:
            # in Phase 3, random pick a piece that can fly.
            target = self.state.get_coords(2)[0]
            new_move = self.state.get_coords(0)[0]
            return target, new_move