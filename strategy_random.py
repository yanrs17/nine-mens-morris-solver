from strategy import Strategy
import random

class StrategyRandom(Strategy):

    def __init__(self):
        Strategy.__init__(self)
        self.name = "Random"

    def suggest_move(self, state):
         return random.choice(state.get_successors())