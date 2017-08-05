from strategy import Strategy
from tippy_game_state import *

    
class StrategyMinimax(Strategy):
    ''' The strategy of minimax.
    
    '''  
    def __init__(self, interactive):
        ''' (StrategyMinimax, bool) -> NoneType
        
        Initialize StrategyMinimax self.
        '''
        Strategy.__init__(self, interactive)
        
    def suggest_move(self, state):
        ''' (StrategyMinimax, GameState) -> Move
        
        Suggest a next move for state.
        '''
        # In case there is a tie.
        tie = []
        
        # If there is one step that leads to win, return it.        
        for i in state.possible_next_moves():
            new_state = state.apply_move(i)
            if self.win(new_state) == -1.0:
                return i
            elif self.win(new_state) == 0.0:
                tie.append(i)
        
        if tie:
            return tie[0]
        # Else: return the smallest one.
        return state.possible_next_moves()[0]
    
    def win(self, state):
        ''' (StrategyMinimax, GameState) -> float
        
        Return whether the player is WIN(1.0), LOSE(-1.0) or DRAW(0.0)
        'win' is in {WIN, LOSE, DRAW}.
        '''
        
        possibility = [self.win(state.apply_move(i)) 
                       for i in state.possible_next_moves()]        
        if state.over or possibility == []:
            if state.winner(state.next_player):
                return 1.0
            elif state.winner(state.opponent()):
                return -1.0
            else:
                return 0.0
        else:
            possibility.sort()
            if (possibility[0] == possibility[-1]) and possibility[0] == 1.0:
                return -1.0
            elif -1.0 in possibility:
                return 1.0
            else:
                return 0.0