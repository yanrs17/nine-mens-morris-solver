from strategy import Strategy
import random

class StrategyRandom(Strategy):

    def suggest_move(self, state):
         return random.choice(state.get_successors())