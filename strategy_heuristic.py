from strategy import Strategy
from state import *
import random

class StrategyHeuristic(Strategy):
    def __init__(self):
        Strategy.__init__(self)
        self.name = "Heurtistic"

    def suggest_move(self, state):
        '''
        Recommend a next move using the current strategy
        '''

        mill = []

        opponent_pieces = state.pieces_left_onboard(state.current_player_key)

        for nxt in state.get_successors():
            
            # If there is a state that leads to win, return it.
            new_state = State(state.current_player, is_new = False, grid = nxt, user_pieces_num = 0, computer_pieces_num = 0) # init Phase 2.
            if new_state.winner == state.opponent: 
                # TODO OR JUST state.current_player?
                return nxt
            

            # If opponent is going to form a mill, stop them!
            # nxt is next grid; self.grid is original grid. 
            #   if in the next grid, find the one being placed, 
            #       compare every piece coordinates, if is 1 in nxt grid while 2 in self.grid, then is the latest one.
            #   if is user's piece, will it form the mill? if it is then return it. 



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
            return mill[0]

        # If there is no state that leads to win
        # AND there is no state that leads to mill
        # Choose a random one
        # print("choice length...", len(state.get_successors()))
        return random.choice(state.get_successors())