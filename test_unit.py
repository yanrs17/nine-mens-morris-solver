from game import Game
from state import State
from strategy_random import StrategyRandom

def test1():
    """
    Init from Phase 1.
    """
    Game(State, StrategyRandom, grid = []).play()

def test2():
    """
    Init from Phase 2, convenient for testing.
    > computer cannot move, thus user wins.
    """
    grid = [
        [2,  -1, -1,  2, -1, -1,  2],
        [-1,  2, -1,  2, -1,  2, -1],
        [-1, -1,  2,  2,  2, -1, -1],
        [1,   1,  1, -1,  1,  1,  1],
        [-1, -1,  1,  1,  1, -1, -1],
        [-1,  0, -1,  0, -1,  0, -1],
        [0,  -1, -1,  0, -1, -1,  0]
    ]
    Game(State, StrategyRandom, grid = grid).play()

def test3():
    """
    Init from Phase 2, convenient for testing.
    """
    grid = [
        [2,  -1, -1,  0, -1, -1,  2],
        [-1,  2, -1,  2, -1,  2, -1],
        [-1, -1,  2,  2,  2, -1, -1],
        [1,   1,  1, -1,  1,  1,  0],
        [-1, -1,  1,  1,  1, -1, -1],
        [-1,  0, -1,  0, -1,  0, -1],
        [0,  -1, -1,  2, -1, -1,  1]
    ]
    Game(State, StrategyRandom, grid = grid).play()

test3()









