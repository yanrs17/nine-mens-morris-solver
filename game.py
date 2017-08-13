from state import State
from strategy_random import StrategyRandom
from strategy_minimax import StrategyMinimax
from strategy_heuristic import StrategyHeuristic
from autogame import AutoGame
import random

class Game:
    """
    Game class, use State class from state.py to simulate a game.
    """
    def __init__(self, state, strategy, grid = [], user_pieces_prop = -1, computer_pieces_prop = -1):
        """
        player:
            "c": computer
            "u": user
        
        state:
            import from state.py,

        """

        self.strategy = strategy() # init strategy
        player = ''
        while player not in ['c', 'u']:
            player = input('Who plays first?\nc: computer plays first\nu: user plays first\n')
        
        self.user_pieces_num = 9
        self.computer_pieces_num = 9

        ### Different initial state setting:
        # start from Phase 1 with grid empty.
        # start from Phase 2 with full grid. 1: user; 2: computer
        
        if not grid: # init from Phase 1
            user_pieces_num = 9
            computer_pieces_num = 9
            is_new = True
        else:
            if user_pieces_prop == 0 and computer_pieces_prop == 0:
                user_pieces_num = 0
                computer_pieces_num = 0
            else:
                flattened = [item for sublist in grid for item in sublist]
                user_pieces_num = 9 - sum(list(map(lambda piece: 1 if piece == 1 else 0, flattened)))
                computer_pieces_num = 9 - sum(list(map(lambda piece: 1 if piece == 2 else 0, flattened)))
            is_new = False

        self.state = state(player, is_new = is_new, grid = grid, user_pieces_num = user_pieces_num, computer_pieces_num = computer_pieces_num) # init Phase 2.

    def play(self):
        print("Game init...")
        print(self.state)
        while not self.state.over:
            if self.state.current_player == 'u': 
                # print("user's turn", self.state.pieces_left_onboard(self.state.current_player_key), self.state.current_player)
                # user's turn.
                if self.state.piece_not_used > 0:
                    # in Phase 1, place pieces.
                    target, new_move = self.state.get_move(phase = 1)
                    while not self.state.is_valid_move(new_move, phase = 1):
                        print("Illegal move: ({}, {}), please give a valid cordinates.".format(new_move[0], new_move[1]))
                        print(self.state.instructions())
                        print(self.state)
                        target, new_move = self.state.get_move(phase = 1)
                    print("You choose a valid position ({}, {}) to add a new piece.".format(new_move[1], new_move[0]))
                elif self.state.piece_not_used == 0 and self.state.pieces_left_onboard(self.state.current_player_key) > 3:
                    # in Phase 2, move pieces.
                    # print("in user phase 2 moving...")
                    target, new_move = self.state.get_move(phase = 2)
                    while not self.state.is_valid_move(new_move, phase = 2, target = target):
                        print("Illegal move or invalid target piece, please give a valid cordinates.")
                        print(self.state.instructions())
                        print(self.state)
                        target, new_move = self.state.get_move(phase = 2)
                    print("You pick piece at ({}, {}) to move to ({}, {})".format(target[1], target[0], new_move[1], new_move[0]))
                elif self.state.piece_not_used == 0 and self.state.pieces_left_onboard(self.state.current_player_key) == 3:
                    # in Phase 3, fly pieces.
                    target, new_move = self.state.get_move(phase = 3)
                    while not self.state.is_valid_move(new_move, phase = 3, target = target):
                        print("Illegal move or invalid target piece, please give a valid cordinates.")
                        print(self.state.instructions())
                        print(self.state)
                        target, new_move = self.state.get_move(phase = 3)
                    print("You pick piece at ({}, {}) to fly to ({}, {})".format(target[1], target[0], new_move[1], new_move[0]))
                else:
                    # user pieces is equal to 2. computer wins.
                    print("Computer wins.")
                    return 
                # start to apply the target and new_move into new state.
                self.state = self.state.apply_target_and_move(target, new_move)

            else:
                # computer's turn.
                # assume now computer simply random pick a empty position and put pieces or move or fly.
                # target, new_move = self.strategy.suggest_move(self.state)
                if not self.state.get_successors():
                    # if return no choice for computer, then user wins!
                    print("You beat computer!")
                    return 
                new_grid = self.strategy.suggest_move(self.state)
                self.state.computer_piece_not_used = max(self.state.computer_piece_not_used - 1, 0)
                print("user remained...", self.state.user_piece_not_used, "; computer remained...", self.state.computer_piece_not_used)
                self.state = State(self.state.opponent, is_new = False, grid = new_grid, user_pieces_num = self.state.user_piece_not_used, computer_pieces_num = self.state.computer_piece_not_used)
            
            # # start to apply the target and new_move into new state.
            print("New game state: \n")
            print(self.state)

        # if game is over.
        if self.state.winner == 'u':
            print("You beat computer!")
        elif self.state.winner == 'c':
            print("Computer wins!")
        else:
            print("Tie...")

if __name__ == '__main__':
    g = {'r': StrategyRandom, 'm': StrategyMinimax, 'h': StrategyHeuristic}

    while True:
        players = input("1 for player vs. AI, 2 for AI vs. AI: ")
        if players in ['1', '2']:
            break
        else:
            print("Invalid option, please try again.")
    
    if players == '1':
        while True:
            game_to_play = input("r to play random, m to play minimax, h to play heuristic\n")
            if game_to_play.lower() in g:
                break
            else:
                print("Invalid option, please try again.")
        Game(State, g[game_to_play], grid = []).play()
    elif players == '2':
        # from strategy_random import StrategyRandom
        # from strategy_minimax import StrategyMinimax
        # from strategy_heuristic import StrategyHeuristic

        # g = {'r': StrategyRandom, 'm': StrategyMinimax, 'h': StrategyHeuristic}
        res_lst = []
        while True:
            try:
                rounds = int(input("Input number of rounds: "))
                if rounds > 0:
                    break
                else:
                    print("Invalid option, please try again.")
            except ValueError:
                print("Invalid option, please try again.")
        # rounds = 50
        # rounds = 10

        # if strategy1 is None or strategy2 is None:

        while True:
            print("player 1:")
            game1 = input("r to play random, m to play minimax, h to play heuristic\n")
            if game1.lower() in g:
                break
            else:
                print("Invalid option, please try again.")
        strategy1 =  g[game1]

        while True:
            print("player 2:")
            game2 = input("r to play random, m to play minimax, h to play heuristic\n")
            if game2.lower() in g:
                break
            else:
                print("Invalid option, please try again.")
        strategy2 =  g[game2]
        for i in range(rounds):
            print("=== New Game ===")
            result = AutoGame(State, strategy1, strategy2).play()
            # result = AutoGame(State, StrategyMinimax, StrategyRandom).play()
            # 0: strategy 1 wins; 1: strategy 2 wins.
            res_lst.append(result)
            print("================")
        res_lst = filter(lambda x: x != None, res_lst)
        print("Player 1 wins # {}/{} matches.".format(sum(res_lst), rounds))
    else:
        raise Exception('Not 1 or 2')
