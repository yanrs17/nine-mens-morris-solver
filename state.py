"""Nine Men's Morris routines.
    A) Class State
    A specializion of the StateSpace Class that is tailored to the game of Nine Men's Morris.
    B) class Direction
    An encoding of the directions of movement that are possible for players in Nine Men's Morris.
"""

class State:

    def __init__(self, firstmove, difficulty):
        """
        Create a Nine Men's Morris state

        firstmove: 1: you move first; 2: computer move first.
        difficulty: 1: easy; 2: medium: 3: hard
        """
        self.width = 7
        self.height = 7
        self.grid = [
            [0, -1, -1, 0, -1, -1, 0],
            [-1, 0, -1, 0, -1, 0, -1],
            [-1, -1, 0, 0, 0, -1, -1],
            [0, 0, 0, -1, 0, 0, 0],
            [-1, -1, 0, 0, 0, -1, -1],
            [-1, 0, -1, 0, -1, 0, -1],
            [0, -1, -1, 0, -1, -1, 0]
        ]
        # self.player = player
        
        self.firstmove = firstmove
        self.difficulty = difficulty

        # Cell Types
        # -1 means x (The cell is impossible to be reached by any player)
        #  0 means empty (The cell is Unoccupied but is reachable by any player)
        #  1 means w (The cell is currently occupied by the White player)
        #  2 means b (The cell is currently occupied by the Black player)
        self.cell_types = {-1: 'x', 0: '_', 1: 'w', 2: 'b'}

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
        for i in range(self.width):
            for j in range(self.height):
                print(self.cell_types[self.grid[i][j]], end=" ")
            print()

    def new_move()
        
    
    def start(self):
        print("game start...")
        self.print_state()
        while True:
            # assume it's user turn first.
            print("user's turn...")
            user_move = self.new_move()
