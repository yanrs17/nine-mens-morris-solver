"""Nine Men's Morris routines.
    A) Class State
    A specializion of the StateSpace Class that is tailored to the game of Nine Men's Morris.
    B) class Direction
    An encoding of the directions of movement that are possible for players in Nine Men's Morris.
"""

class State:

    def __init__(self, player='u', is_new = False, grid=[], piece_not_used=9):
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
                [0,  -1, -1,  0, -1, -1,  0],
                [-1,  0, -1,  0, -1,  0, -1],
                [-1, -1,  0,  0,  0, -1, -1],
                [0,   0,  0, -1,  0,  0,  0],
                [-1, -1,  0,  0,  0, -1, -1],
                [-1,  0, -1,  0, -1,  0, -1],
                [0,  -1, -1,  0, -1, -1,  0]
            ]
            self.piece_not_used = 9
        else:
            self.grid = grid
            self.piece_not_used = piece_not_used - 1

        self.winner = None

        if self.check_lose_state(self.grid, self.opponent): # check if current user wins.
            self.winner = self.current_player
            self.over = True


    def check_lose_state(self, grid, player):
        """
        Winning condition: 
            opponent equals to 2 pieces on board, or
            opponent cannot move
        
        player: will be either 'c' or 'u'
        
        user: 1,
        computer: 2
        """
        flat_list = [piece for row in grid for piece in row]
        player_key = 1 if player == 'u' else 2
        number_of_player_pieces = flat_list.count(player_key)

        # get_neighbors and check if can move.
        return True
    
    def get_neighbors(self, piece_cord):
        """
        Given a piece cordinates (x, y), output a dictionary of its neighbor cordinate tuples.

        Note that x is upper horizontal axis, and y is left vertical axis, say, (0, 0) is upper left corner.
        """
        x = piece_cord[0]
        y = piece_cord[1]
        
        neighbors = []
        if x == 0 or x == 6:
            if y == 0 or y == 6:
                neighbors.append((3, y))
                neighbors.append((x, 3))
            elif y == 3:
                neighbors.append((x, 0))
                neighbors.append((x, 6))
                if x == 1: # (1, 3)
                    neighbors.append((1, 3))
                elif x == 6: # (5, 3)
                    neighbors.append((5, 3))
        elif x == 1 or x == 5:
            if y == 1 or y == 5:
                neighbors.append((3, y))
                neighbors.append((x, 3))
            elif y == 3:
                neighbors.append((x, 1))
                neighbors.append((x, 5))
                neighbors.append((x - 1, 3))
                neighbors.append((x + 1, 3))
        elif x == 2 or x == 4:
            if y == 2 or y == 4:
                neighbors.append((3, y))
                neighbors.append((x, 3))
            elif y == 3:
                neighbors.append((x, 2))
                neighbors.append((x, 4))
                if x == 2: # (2, 3)
                    neighbors.append((1, 3))
                elif x == 4: # (4, 3)
                    neighbors.append((5, 3))
        else: # x = 3
            if y == 0 or y == 6:
                neighbors.append((0, y))
                neighbors.append((6, y))
                if y == 0:
                    neighbors.append((3, 1))
                elif y == 6: 
                    neighbors.append((3, 5))
            elif y == 1 or y == 5:
                neighbors.append((1, y))
                neighbors.append((5, y))
                neighbors.append((3, y - 1))
                neighbors.append((3, y + 1))
            elif y == 2 or y == 4:
                neighbors.append((2, y))
                neighbors.append((4, y))
                if y == 2: # (3, 2)
                    neighbors.append((3, 1))
                elif y == 4: # (3, 5)
                    neighbors.append((3, 5))
        print(neighbors)




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
        
    
    def start(self):
        print("game start...")
        self.print_state()
        while True:
            # assume it's user turn first.
            print("user's turn...")
            user_move = self.new_move()


new_state = State()
new_state.get_neighbors((1, 3))
new_state.get_neighbors((2, 2))
new_state.get_neighbors((2, 3))