"""Nine Men's Morris routines.
    A) Class State
    A specializion of the StateSpace Class that is tailored to the game of Nine Men's Morris.
    B) class Direction
    An encoding of the directions of movement that are possible for players in Nine Men's Morris.
"""

from search import *

class State(StateSpace):

    def __init__(self, action, gval, parent, grid, player):
        """
        Create a Nine Men's Morris state

        @param width:   The width of the grid, in this case it is 7
        @param height:  The height of the grid, in this case it is 7
        @param grid:    The board of players with size width * height
        @param player:  The current player, 1 is white, 2 is black
        """
        StateSpace.__init__(self, action, gval, parent)
        self.width = 7
        self.height = 7
        self.grid = grid
        self.player = player

        # Cell Types
        # -1 means x (The cell is impossible to be reached by any player)
        #  0 means empty (The cell is Unoccupied but is reachable by any player)
        #  1 means w (The cell is currently occupied by the White player)
        #  2 means b (The cell is currently occupied by the Black player)
        self.cell_types = {-1: 'x', 0: ' ', 1: 'w', 2: 'b'}

    def successors(self):
        """
        Generate all the actions that can be performed from this state,
        and the states those actions will create.
        """
        successors = []
        for w in range(self.width):
            for h in range(self.height):
                if self.grid[self.width][self.height] == self.cell_types[0]:
                    successors.append((self.width, self.height))
        return successors

    # def hashable_state(self):
    #     """
    #     Return a data item that can be used as a dictionary key to UNIQUELY represent a state.
    #     """
    #     return hash((self.robot, frozenset(self.snowballs.items())))


    def state_string(self):
        """
        Return a string representation of a state that can be printed to stdout.
        """
        return self.grid


    def print_state(self):
        """
        Print the string representation of the state. ASCII art FTW!
        """        
        print("ACTION was " + self.action)      
        print(self.state_string())