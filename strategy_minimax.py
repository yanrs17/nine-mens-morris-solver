from strategy import strategy
from state import *

class StrategyMinimax(Strategy):
    def __init__(self):
        Strategy.__init__(self)

    def suggest_move(self, state):
        '''
        Recommend a next move using the current strategy
        '''

        mill = []

        opponent_pieces = state.pieces_left_onboard(state.current_player)

        for nxt in state.get_successors():
            # If there is a state that leads to win, return it.
            if nxt.winner == state.opponent: 
                # TODO OR JUST state.current_player?
                return nxt

            # If there is a state that leads to mill, return it.
            
            # We calculate the number of pieces of opponent
            # if the piece is reduced (by one),
            # it means the opponent has been milled
            # pieceMilled means the difference of pieces of opponent
            # if pieceMilled is 0: not milled
            # if 1: milled
            # else: exception
            pieceMilled = opponent_pieces - nxt.pieces_left_onboard(nxt.opponent)
            if pieceMilled == 1:
                # A piece of opponent has been removed
                mill.append(nxt)
            elif pieceMilled == 0:
                # Do nothing
                pass
            else:
                # Exception
                raise

        # If there is no state that leads to win
        # Check if there is any state that leads to mill
        if mill:
            # Return the first state that leads to mill
            # It does not have to be [0], just an option
            return mill[0]

        # If there is no state that leads to win
        # AND there is no state that leads to mill
        # Just return the first state
        # It does not have to be [0], just an option
        return state.get_successors()[0]