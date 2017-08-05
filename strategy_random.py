from strategy import Strategy
import random

class StrategyRandom(Strategy):

    def suggest_move(self, state):
        return random.choice(state.possible_next_moves())
