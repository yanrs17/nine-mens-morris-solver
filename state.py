"""Nine Men's Morris routines.
    A) Class State
    A specializion of the StateSpace Class that is tailored to the game of Nine Men's Morris.
    B) class Direction
    An encoding of the directions of movement that are possible for players in Nine Men's Morris.
"""

class State:

    def __init__(self, player, is_new = False, grid, piece_not_used):
        """
        Create a Nine Men's Morris state

        player: current user, user or computer.
        is_new: if we need to init the board.
        grid: board.
        piece_not_used: the number of pieces not being placed on grid.
        Cell Types:
            -1 means x (The cell is impossible to be reached by any player)
            0 means empty (The cell is Unoccupied but is reachable by any player)
            1 means u (The cell is currently occupied by the White player)
            2 means c (The cell is currently occupied by the Black player)
        """
        self.grid = []
        self.width = 7
        self.height = 7
        self.cell_types = {-1: 'x', 0: '_', 1: 'w', 2: 'b'}

        if player == 'c':
            self.current_player = 'c'
            self.opponent = 'u'
        else: 
            self.current_player = 'u'
            self.opponent = 'c'

        if is_new:
            self.grid = [
                [0, -1, -1, 0, -1, -1, 0],
                [-1, 0, -1, 0, -1, 0, -1],
                [-1, -1, 0, 0, 0, -1, -1],
                [0, 0, 0, -1, 0, 0, 0],
                [-1, -1, 0, 0, 0, -1, -1],
                [-1, 0, -1, 0, -1, 0, -1],
                [0, -1, -1, 0, -1, -1, 0]
            ]
            self.piece_not_used = 9
        else:
            self.grid = grid
            self.piece_not_used = piece_not_used - 1

        self.winner = None

        if check_win_state(self.grid, self.current_player): # check if current user wins.
            self.winner = self.current_player
            self.over = True
        elif check_win_state(self.grid, self.opponent): # check if opponent wins.
            self.winner = self.opponent
            self.over = True

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
