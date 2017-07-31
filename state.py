from search import *

class State(StateSpace):

    def __init__(self, action, gval, parent, grid):
        """
        Create a Nine Men's Morris state

        @param width:   The width of the grid, in this case it is 7
        @param height:  The height of the grid, in this case it is 7
        @param grid:    The board of players with size width * height
        """
        StateSpace.__init__(self, action, gval, parent)
        self.width = 7
        self.height = 7
        self.grid = grid

        # Cell Types
        # -1 means i (The cell is Impossible to be reached by any player)
        #  0 means u (The cell is Unoccupied but is reachable by any player)
        #  1 means w (The cell is currently occupied by the White player)
        #  2 means b (The cell is currently occupied by the Black player)
        self.cell_types = {-1: 'i', 0: 'u', 1: 'w', 2: 'b'}

        def successors(self):
            """
            Generate all the actions that can be performed from this state,
            and the states those actions will create.
            """
            successors = []
            for w in range(self.width):
                for h in range(self.height):
                    if self.grid[width][height] == self.cell_types[0]:
                        successors.append((self.width, self.height))
