"""Nine Men's Morris routines.
    A) Class State
    A specializion of the StateSpace Class that is tailored to the game of Nine Men's Morris.
    B) class Direction
    An encoding of the directions of movement that are possible for players in Nine Men's Morris.
"""

from copy import deepcopy
# Copy a new board from the old board
#   without aliasing to the old board

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
        opponent_key = 2 if player_key == 1 else 1
        number_of_player_pieces = flat_list.count(player_key)

        # get_neighbors and check if can move.
        all_blocked = True
        all_cords = self.get_coords(player_key)
        for cord in all_cords:
            its_neighbors = self.get_neighbors(cord)
            for neighbor in its_neighbors:
                if not self.grid[neighbor[0]][neighbor[1]] == opponent_key: # if any of neighbors is not opponent.
                    all_blocked = False
                    break
            if all_blocked == False:
                break
        
        if number_of_player_pieces == 2 or all_blocked:
            return True # the player indicated lose
        else:
            return False
    
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
        
        Pseudo-code:
        if not isAllUsed():
            place()
        else:
            if num_pieces > 3:
                move()
            elif num_pieces == 3:
                fly()
            elif num_pieces == 2:
                lose()
                # Means opponent wins
            else:
                raise error('Something is wrong')

        if isMill():
            # Mill: 3 together
            remove()
        """

        successors = []

        if piece_not_used > 0:
            # Place
            for x in range(7):
                for y in range(7):
                    if self.grid[x][y] == 0: # Unoccupied
                        successors.append(('P', x, y))
                        
        elif piece_not_used == 0:
            num_pieces = self.pieces_left_onboard(self.grid, self.current_player)
            if num_pieces > 3:
                # Move
                coords = self.get_coords(self.grid, self.current_player)
                for coord in coords:
                    neighbors = self.get_neighbor(coord)
                    for neighbor in neighbors:
                        x = neighbor[0]
                        y = neighbor[1]
                        if self.board[x][y] == 0:
                            successors.append(('M', x, y))
                            # 'M' means to move a piece on the board
                            # i.e. Place + Remove
            elif num_pieces == 3:
                # Fly
                for x in range(7):
                    for y in range(7):
                        if self.grid[x][y] == 0: # Unoccupied
                            successors.append(('F', x, y))
                            # 'F' means to fly a piece on the board
                            # Similar to 'M' but when removing a piece,
                            # we can remove any piece on the board
                            # instead of in 'M' we have to remove its
                            # neighbor (origin piece has also to be its neighbor)
            elif num_pieces == 2:
                # Lose
                # TODO CHECK_LOSE_STATE()
            else:
                # Exception
                raise
        else:
            # Exception
            raise

        # TODO CALL ISMILL()

        # flag = 'P' # 'P' means to place a piece on the board

        return instruction_to_grid(successors)

    def instruction_to_grid(self, successors)
        """
        Convert instruction and coordinates to actual board
        """


        next_boards = []
        for s in successors:
            instruction = s[0] # P or M or F
            x = s[1]
            y = s[2]
            next_board = deepcopy(self.grid)
            # Place a piece
            next_board[x][y] = self.current_player
            
            if instruction == 'P':
                if (isMill(next_board, self.current_player)):

                next_boards.append(next_board)
            if instruction == 'M':
                # next_board


            



        # self.instruction_to_grid()
        
        # new_grid = self.apply_move(...)
        # if isMill(self.grid, self.current_player):
        #     flag = 'm' # Small m means Mill
    
    
    def get_coords(self, player):
        """
        Get the coordinates for all the pieces of "player" on the board
        """
        # Source:
        # https://stackoverflow.com/questions/27175400/how-to-find-the-index-of-a-value-in-2d-array-in-python
        return [(ix,iy) for ix, row in enumerate(self.grid) for iy, i in enumerate(row) if i == player]

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

    def isMill(b, player):
        """
        B is the 7*7 board
        player means the letter representation of the player
        e.g. w (for white) or b (for black)

        >>> b = [['u' for i in range(7)] for j in range(7)]
        >>> isMill(b, 'b')
        False
        >>> b[0][0] = 'b'
        >>> b[3][0] = 'b'
        >>> b[6][0] = 'b'
        >>> isMill(b, 'b')
        True
        >>> isMill(b, 'w')
        False
        >>> b[0][3] = 'b'
        >>> b[0][6] = 'b'
        >>> b[3][0] = 'w'
        >>> isMill(b, 'b')
        True
        >>> b[0][6] = 'b'
        >>> isMill(b, 'w')
        False
        """
        all_mill_possibilities = [ # 16 possibilities
            # Outer 3
            [b[0][0], b[3][0], b[6][0]], # every 3 pieces form an "m"
            [b[0][0], b[0][3], b[0][6]],
            [b[0][6], b[3][6], b[6][6]],
            [b[6][0], b[6][3], b[6][6]],
            # Middle 3
            [b[1][1], b[3][1], b[5][1]],
            [b[1][1], b[1][3], b[1][5]],
            [b[1][5], b[3][5], b[5][5]],
            [b[5][1], b[5][3], b[5][5]],
            # Inner 3
            [b[2][2], b[3][2], b[4][2]],
            [b[2][2], b[2][3], b[2][4]],
            [b[2][4], b[3][4], b[4][4]],
            [b[4][2], b[4][3], b[4][4]],
            # Cross 3
            [b[0][3], b[1][3], b[2][3]],
            [b[3][0], b[3][1], b[3][2]],
            [b[3][4], b[3][5], b[3][6]],
            [b[4][3], b[5][3], b[6][3]]
            ]

        # "lambda p: p == player" means each piece (e.g. b[0][0]) 
        #       returns true if it is occupied by the argument "player"
        # "all(list(map(lambda p: p == player, m)))" means each mill condition "m"
        #       returns true iff ALL of them (e.g. [b[0][0], b[3][0], b[6][0]]) are true
        # "lambda m: all(list(map(lambda p: p == player, m)" means whether
        #       each m forms a mill
        # "True in ..." means the board forms a mill as long as one of them is a mill
        return True in list(map(lambda m: all(list(map(lambda p: p == player, m))), all_mill_possibilities))
        
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
print(new_state.get_coords(1))