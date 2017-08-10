from game import Game
from state import State
from strategy_random import StrategyRandom

def test1():
    """
    Init from Phase 1.
    """
    print("### You are testint Phase 1 ###")
    Game(State, StrategyRandom, grid = []).play()

def test2():
    """
    Init from Phase 2, convenient for testing.
    > computer cannot move, thus user wins.
    """
    print("### You are testint Phase 2 ###")
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
    print("### You are testint Phase 2 ###")
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

def test4():
    """
    Init from Phase 3, convenient for testing.
    """
    print("### You are testint Phase 3 ###")
    grid = [
        [0,  -1, -1,  0, -1, -1,  0],
        [-1,  0, -1,  0, -1,  0, -1],
        [-1, -1,  0,  2,  2, -1, -1],
        [1,   1,  0, -1,  0,  0,  0],
        [-1, -1,  0,  0,  0, -1, -1],
        [-1,  0, -1,  0, -1,  0, -1],
        [0,  -1, -1,  2, -1, -1,  1]
    ]
    Game(State, StrategyRandom, grid = grid, user_pieces_prop = 0, computer_pieces_prop = 0).play()

def test5():
    """
    Init from Phase 3, testing for mills.
    """
    print("### You are testint Phase 3, especially for mills. ###")
    grid = [
        [1,  -1, -1,  1, -1, -1,  1],
        [-1,  0, -1,  0, -1,  0, -1],
        [-1, -1,  0,  2,  0, -1, -1],
        [1,   2,  2, -1,  2,  0,  0],
        [-1, -1,  0,  1,  0, -1, -1],
        [-1,  0, -1,  1, -1,  0, -1],
        [1,  -1, -1,  1, -1, -1,  1]
    ]
    Game(State, StrategyRandom, grid = grid, user_pieces_prop = 0, computer_pieces_prop = 0).play()

def test6():
    """
    Init from Phase 2, testing for computer forming mills.
    """
    print("### You are testint Phase 2, especially for computer forming mills. ###")
    grid = [
        [1,  -1, -1,  1, -1, -1,  1],
        [-1,  1, -1,  0, -1,  0, -1],
        [-1, -1,  0,  2,  0, -1, -1],
        [1,   2,  2, -1,  2,  2,  2],
        [-1, -1,  1,  1,  0, -1, -1],
        [-1,  1, -1,  2, -1,  1, -1],
        [2,  -1, -1,  0, -1, -1,  2]
    ]
    Game(State, StrategyRandom, grid = grid, user_pieces_prop = 0, computer_pieces_prop = 0).play()

test6()









