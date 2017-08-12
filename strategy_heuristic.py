from strategy import Strategy
from state import *
from copy import deepcopy
import random

class StrategyHeuristic(Strategy):
    def __init__(self):
        Strategy.__init__(self)
        self.name = "Heuristic"

    def suggest_move(self, state):
        '''
        Recommend a next move using the current strategy
        '''

        mill = []
        neighbors_prefer_grids = []
        stop_opponent_move = []

        opponent_pieces = state.pieces_left_onboard(state.current_player_key)

        for nxt in state.get_successors():
            
            # If there is a state that leads to win, return it.
            # print("printing out player...", state.current_player, state.opponent)
            new_state = State(state.current_player, is_new = False, grid = nxt, user_pieces_num = 0, computer_pieces_num = 0) # init Phase 2.
            if new_state.winner == state.current_player: 
                # TODO OR JUST state.current_player?
                return nxt
            

            # Note that such heuristic only happens at Phase 1 and 2, not 3!
            # If opponent is going to form a mill, stop them!
            # nxt is next grid; self.grid is original grid. 
            #   if in the next grid, find the one being placed, 
            #       compare every piece coordinates, if is 2 in nxt grid while 0 in self.grid, then is the latest one.
            #   if is user's piece, will it form the mill? if it is then return it. 
            if state.pieces_left_onboard(state.current_player_key) > 3:
                fake_grid = deepcopy(state.grid)
                new_piece = (-1, -1)
                for x,y in [(ix,iy) for ix, row in enumerate(nxt) for iy, i in enumerate(row) if i == state.current_player_key]:
                    # print("new_piece...", x, y, state.grid[x][y])
                    if state.grid[x][y] == 0:
                        new_piece = (x, y)
                fake_grid[new_piece[0]][new_piece[1]] = state.opponent_player_key
                if (sum(state.getMills(fake_grid, state.opponent_player_key)) > 0) and \
                    (not state.getMills(fake_grid, state.opponent_player_key) == state.getMills(state.grid, state.opponent_player_key)) and \
                    (sum(state.getMills(fake_grid, state.opponent_player_key)) >= sum(state.getMills(state.grid, state.opponent_player_key))):
                    # print("user may form a mill...", nxt)
                    # return nxt
                    stop_opponent_move = nxt

            # if the new_piece is in the neighbors of current pieces' neighbors.
            if state.piece_not_used > 0:
                new_piece = (-1, -1)
                neighbors = []
                for x,y in [(ix,iy) for ix, row in enumerate(nxt) for iy, i in enumerate(row) if i == state.current_player_key]:
                    # print("new_piece...", x, y, state.grid[x][y])
                    neighbors.extend(state.get_neighbors((x, y)))
                    if state.grid[x][y] == 0:
                        new_piece = (x, y)
                if new_piece in neighbors:
                    neighbors_prefer_grids.append(nxt)



            # If there is a state that leads to mill, return it.
            
            # We calculate the number of pieces of opponent
            # if the piece is reduced (by one),
            # it means the opponent has been milled
            # pieceMilled means the difference of pieces of opponent
            # if pieceMilled is 0: not milled
            # if 1: milled
            # else: exception
            # print("print opponent_pieces", opponent_pieces, new_state.pieces_left_onboard(new_state.opponent_player_key))
            if (sum(state.getMills(nxt, state.current_player_key)) > 0) and \
                (not state.getMills(nxt, state.current_player_key) == state.getMills(state.grid, state.current_player_key)) and \
                (sum(state.getMills(nxt, state.current_player_key)) >= sum(state.getMills(state.grid, state.current_player_key))):
            # pieceMilled = opponent_pieces - new_state.pieces_left_onboard(new_state.opponent_player_key)
            # if pieceMilled == 1:
                # A piece of opponent has been removed
                
                # if nxt forms a mill.
                mill.append(nxt)
            else:
                # Do nothing
                pass
            # else:
            #     # Exception
            #     raise Exception(pieceMilled)

        # If there is no state that leads to win
        # Check if there is any state that leads to mill
        if mill:
            # Return the first state that leads to mill
            # It does not have to be [0], just an option
            # print("mill length...", len(mill))
            return random.choice(mill)

        if stop_opponent_move:
            return stop_opponent_move


        # not use random to return! find neighbors! if any neibor is empty, use that to form close regional relationship.
        if neighbors_prefer_grids:
            print("close pieces are more preferred...")
            return random.choice(neighbors_prefer_grids)
        else:
            return random.choice(state.get_successors())