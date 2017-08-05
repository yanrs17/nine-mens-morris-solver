"""Nine Men's Morris routines.
    A) Class State
    A specializion of the StateSpace Class that is tailored to the game of Nine Men's Morris.
    B) class Direction
    An encoding of the directions of movement that are possible for players in Nine Men's Morris.
"""

class State:

    def __init__(self, firstmove, difficulty, isNew=False):
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
        #  0 means _ (The cell is unoccupied but reachable by any player)
        #  1 means w (The cell is currently occupied by the White player)
        #  2 means b (The cell is currently occupied by the Black player)
        self.cell_types = {-1: 'x', 0: '_', 1: 'w', 2: 'b'}


    def successors(self):
        """
        Generate all the actions that can be performed from this state,
        and the states those actions will create.
        
        Pseudo-code:
        if not isAllUsed():
            place()
        else:
            if pieceLeft > 3:
                move()
            elif pieceLeft == 3:
                fly()
            elif pieceLeft == 2:
                lose()
                # Means opponent wins
            else:
                raise error('Something is wrong')

        if isMill():
            # Mill: 3 together
            remove()
        """

        

        if piece_not_used > 0:
            # Place
            successors = []
            for w in range(self.width):
                for h in range(self.height):
                    if self.grid[self.width][self.height] == self.cell_types[0]:
                        successors.append((self.width, self.height, 'P')) # 'P' means to place a piece on the board
        elif piece_not_used == 0:
            left = self.pieces_left_onboard(self.grid, self.player)
            if 
        else:
            raise
        return successors

    def pieces_left_onboard(self, board, player):
    """

    >>> b = [['u' for i in range(7)] for j in range(7)]
    >>> pieces_left_onboard(self, b, 'u')
    49
    >>> pieces_left_onboard(self, b, 'b')
    0
    >>> pieces_left_onboard(self, b, 'w')
    0
    >>> b[0][0] = 'b'
    >>> pieces_left_onboard(self, b, 'u')
    48
    >>> pieces_left_onboard(self, b, 'b')
    1
    >>> pieces_left_onboard(self, b, 'w')
    0
    """
    # Flatten the board from 2D to 1D
    flattened = [item for sublist in board for item in sublist]
    return sum(list(map(lambda piece: 1 if piece == player else 0, flattened)))

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
