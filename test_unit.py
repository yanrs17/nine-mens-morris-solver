from game import Game
from autogame import AutoGame
from state import State
from strategy_random import StrategyRandom
from strategy_minimax import StrategyMinimax

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

def test7():
    """
    Init from Phase 2, testing for computer strategy.
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
    Game(State, StrategyMinimax, grid = grid, user_pieces_prop = 0, computer_pieces_prop = 0).play()

def test8():
    """
    Init from Phase 1, testing for computer strategy.
    """
    print("### You are testint Phase 1, especially for computer forming mills. ###")
    Game(State, StrategyMinimax, grid = [], user_pieces_prop = -1, computer_pieces_prop = -1).play()

def test9():
    """
    Init from Phase 3, testing for computer strategy.
    """
    print("### You are testint Phase 3, especially for computer forming mills. ###")
    grid = [
        [1,  -1, -1,  0, -1, -1,  0],
        [-1,  0, -1,  0, -1,  0, -1],
        [-1, -1,  0,  2,  0, -1, -1],
        [1,   0,  0, -1,  2,  0,  0],
        [-1, -1,  0,  0,  2, -1, -1],
        [-1,  0, -1,  0, -1,  0, -1],
        [1,  -1, -1,  0, -1, -1,  0]
    ]
    Game(State, StrategyMinimax, grid = grid, user_pieces_prop = 0, computer_pieces_prop = 0).play()

def test10():
    """
    Let two strategy compete with each other.
    """
    print("### Machine V.S Machine ###")
    res_lst = []
    for i in range(30):
        result = AutoGame(State, StrategyMinimax, StrategyRandom).play()
        # 0: strategy 1 wins; 1: strategy 2 wins.
        res_lst.append(result)
    print("Strategy {} wins # {} matches.".format("Minimax", sum(res_lst)))
    


test10()









