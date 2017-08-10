"""Nine Men's Morris routines.
    A) Class State
    A specializion of the StateSpace Class that is tailored to the game of Nine Men's Morris.
    B) class Direction
    An encoding of the directions of movement that are possible for players in Nine Men's Morris.
"""

from copy import deepcopy
# Copy a new board from the old board
#   without aliasing to the old board

import re

class State:
    def __init__(self, player='u', is_new = False, grid=[], user_pieces_num=10, computer_pieces_num=10):
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
        self.cell_types = {-1: 'x', 0: '_', 1: 'u', 2: 'c'}



        if player == 'c':
            self.current_player = 'c'
            self.current_player_key = 2
            self.opponent_player_key = 1
            self.opponent = 'u'
        else: 
            self.current_player = 'u'
            self.current_player_key = 1
            self.opponent_player_key = 2
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
        else:
            self.grid = grid
        
        if self.current_player_key == 1:
            self.user_piece_not_used = user_pieces_num
            self.computer_piece_not_used = computer_pieces_num
            self.piece_not_used = self.user_piece_not_used
        else:
            self.computer_piece_not_used = computer_pieces_num
            self.user_piece_not_used = user_pieces_num
            self.piece_not_used = self.computer_piece_not_used

        self.winner = None

        if self.check_lose_state(self.grid, self.opponent_player_key): # check if current user wins.
            self.winner = self.current_player
            self.over = True
        else:
            self.over = False


    def check_lose_state(self, grid, player_key):
        """
        Winning condition: 
            opponent equals to 2 pieces on board, or
            opponent cannot move
        
        player: will be either 'c' or 'u'
        
        user: 1,
        computer: 2

        Return:
            True: the player loses
            False: the player does not lose (it does not mean it wins)
        """

        if self.piece_not_used == 0 and self.pieces_left_onboard(player_key) == 2:
            return True
        else:
            # or if opponent cannot move, and it only happen in Phase 2 and 3, not 1.
            if self.piece_not_used == 0:
                opponent_key = 1 if player_key == 2 else 2

                # get_neighbors and check if can move.
                all_blocked = True
                all_cords = self.get_coords(player_key)
                for cord in all_cords:
                    its_neighbors = self.get_neighbors(cord)
                    for neighbor in its_neighbors:
                        if not self.grid[neighbor[0]][neighbor[1]] == opponent_key: # if any of neighbors is not opponent.
                            all_blocked = False
                            break
                    if not all_blocked:
                        break
                return all_blocked
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
        # print(neighbors)
        return neighbors

    def get_neighbors_to_hash(self, piece_cord):
        lst = self.get_neighbors(piece_cord)
        res = {}
        for tup in lst:
            res[tup] = self.grid[tup[0]][tup[1]]
        return res

    def get_successors(self):
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

        return get_next_states()
        """

        successors = []

        if self.piece_not_used > 0: 
            # Place
            for x in range(7):
                for y in range(7):
                    if self.grid[x][y] == 0: # Unoccupied
                        successors.append(('P', x, y))
                        
        elif self.piece_not_used == 0:
            num_pieces = self.pieces_left_onboard(self.current_player_key)
            if num_pieces > 3:
                # Move
                coords = self.get_coords(self.current_player_key)
                for coord in coords:
                    neighbors = self.get_neighbors_to_hash(coord)
                    for neighbor in neighbors:
                        x = neighbor[0]
                        y = neighbor[1]
                        if self.grid[x][y] == 0:
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
                            # neighbor (origin piece has also to be in its neighbors)
            elif num_pieces == 2:
                # Lose
                # It is checked in the next state
                # TODO: EFFICIENCY?
                pass
                
            else:
                # Exception
                raise
        else:
            # Exception
            raise

        return self.get_next_states(successors)

    def get_next_states(self, instructions):
        """
        Convert instruction and coordinates to actual state
        """
        next_boards = []
        oppox_pieces_left = self.get_coords(self.opponent_player_key)

        for instruction, x, y in instructions:
            # instruction can be either P or M or F
            
            next_board = deepcopy(self.grid)

            # Place a piece
            next_board[x][y] = self.current_player_key

            # Get coords of pieces to be moved
            # according to the instruction
            if (instruction == 'P'): # Place
                # We do not remove pieces in "Place"
                # Just a placeholder for for-loop
                pieces = ['new','move']
            elif (instruction == 'M'): # Move
                # Only neighbor pieces placed by the same player
                # can achieve the new state, thus remove it
                neighbors = self.get_neighbors_to_hash((x,y))
                pieces = list(filter(lambda key: neighbors[key] == self.current_player_key, neighbors))
            elif (instruction == 'F'): # Fly
                # Any pieces placed by the same player can be removed
                pieces = self.get_coords(self.current_player_key)
            else:
                # Error
                raise

            for x,y in pieces:

                new_board = deepcopy(next_board)

                # Move/Fly a piece means the same as
                # place a piece in a new coord ("Place")
                # and then remove the piece in the old coord ("Remove")
                # The "Place" has been finished above
                # the following just remove the old piece
                if instruction in ['M', 'F']:
                    new_board[x][y] = 0

                if (self.isMill(new_board, self.current_player_key)):
                    # Mill: Remove a piece from opponents
                    # with each piece removed as a new board
                    for x,y in oppo_pieces_left:
                        next_mill_board = deepcopy(new_board)
                        # Remove the original piece
                        next_mill_board[x][y] = 0
                        next_boards.append(next_mill_board)
                        
                else:
                    # Just append it
                    next_boards.append(new_board)
        return next_boards
    
    def get_coords(self, player):
        """
        Get the coordinates for all the pieces of "player" on the board
        """
        # Source:
        # https://stackoverflow.com/questions/27175400/how-to-find-the-index-of-a-value-in-2d-array-in-python
        return [(ix,iy) for ix, row in enumerate(self.grid) for iy, i in enumerate(row) if i == player]

    def pieces_left_onboard(self, player):
        """
        Get number of pieces left on the board for @player
        >>> pieces_left_onboard(self, 1) # meaning user pieces.
        2
        """
        # Flatten the board from 2D to 1D
        flattened = [item for sublist in self.grid for item in sublist]
        return sum(list(map(lambda piece: 1 if piece == player else 0, flattened)))

    def isMill(self, grid, player):
        """
        B is the 7*7 board
        player means the letter representation of the player
        e.g. w (for white) or b (for black)

        >>> isMill(b, 1) # 1 for user; 2 for computer.
        False
        """
        b = grid
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

    def getMills(self, grid, player):
        """
        B is the 7*7 board
        player means the letter representation of the player
        e.g. w (for white) or b (for black)

        >>> millCount(b, 1) # 1 for user; 2 for computer.
        2 # forms 2 mills for user pieces.
        """
        b = grid
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
        return list(map(lambda m: all(list(map(lambda p: p == player, m))), all_mill_possibilities))
        
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

    def instructions(self):
        """
        Given game phases, return different game instructions.
        """
        if self.piece_not_used > 0:
            return "Pieces not used up yet, give a position to put the piece on."
        elif self.piece_not_used == 0 and self.pieces_left_onboard(self.current_player_key) > 2:
            return "Only allow moving the pieces."

    def __str__(self):
        """
        Print the string representation of the state.
        """
        result = ''
        for i in range(7):
            for j in range(7):
                result += self.cell_types[self.grid[i][j]] + ' '
            result += '\n'
        return result

    def printGrid(self, grid):
        """
        Print the string representation of the state.
        """
        result = ''
        for i in range(7):
            for j in range(7):
                result += self.cell_types[grid[i][j]] + ' '
            result += '\n'
        return result
        
    def get_move(self, phase):

        if phase == 1:
            while True:
                new_move = input("Please type the cordinates of your position, e.g. 0,2, meaning (0, 2) of the grid, note that grid's start point sits at upper left corner.\n")
                if re.match(r"\d,\s*\d", new_move):
                    break
                else:
                    print("Incorrect input, please try again.")
            x = int(new_move.split(",")[0])
            y = int(new_move.split(",")[1])

            self.user_piece_not_used = max(self.user_piece_not_used - 1, 0)
            print("user remained...", self.user_piece_not_used, "; computer remained...", self.computer_piece_not_used)

            return (-1, -1), (y, x) # use (-1, -1) represent placing a new piece.
        elif phase == 2 or phase == 3:
            while True:
                target_piece = input("Select the piece by inputing its cordinates.")
                if re.match(r"\d,\s*\d", target_piece):
                    break
                else:
                    print("Incorrect input, please try again.")
            target_x = int(target_piece.split(",")[0])
            target_y = int(target_piece.split(",")[1])
            while True:
                new_move = input("Please type the cordinates of your intended new position for target piece at ({}, {}).".format(target_x, target_y))
                if re.match(r"\d,\s*\d", target_piece):
                    break
                else:
                    print("Incorrect input, please try again.")
            move_x = int(new_move.split(",")[0])
            move_y = int(new_move.split(",")[1])

            self.user_piece_not_used = max(self.user_piece_not_used - 1, 0)
            print("user remained...", self.user_piece_not_used, "; computer remained...", self.computer_piece_not_used)

            return (target_y, target_x), (move_y, move_x)


        

    def is_valid_move(self, cord, phase, target = (-1, -1)):
        """
        Check if new_move's cord is valid given its current phase.
        """
        if phase == 1:
            # place phase.
            return cord in self.get_coords(0)

        elif phase == 2:
            # move phase.
            # 1. target piece should be current player's piece 
            # 2. target cord should be empty and at its neighbor.
            is_belong_player = self.grid[target[0]][target[1]] == self.current_player_key
            is_at_neighbor = cord in self.get_neighbors(target)
            is_empty = cord in self.get_coords(0)
            return is_belong_player and is_at_neighbor and is_empty

        elif phase == 3:
            # fly phase.
            # 1. target piece should be current player's piece 
            # 2. target cord should be empty.
            is_belong_player = self.grid[target[0]][target[1]] == self.current_player_key
            is_empty = cord in self.get_coords(0)
            return is_belong_player and is_empty

    def apply_target_and_move(self, target, new_move):
        """
        Given current State, with new target piece and new_move coordinates to produce new State.

        1. the target and new_move must be valid here, even not optimal.abs
        2. Should handle the isMill situation here. 
            Especially for user, ask for which piece to remove;
            for computer side, temporarily pick random piece to remove.
        """
        # print("new_move...", new_move)
        if target == (-1, -1):
            # in Phase 1, place a new piece at new_move position.
            new_grid = deepcopy(self.grid)
            new_grid[new_move[0]][new_move[1]] = self.current_player_key
        else:
            # in Phase 2 or 3, place piece at new_move and remove target positon.
            new_grid = deepcopy(self.grid)
            new_grid[target[0]][target[1]] = 0
            new_grid[new_move[0]][new_move[1]] = self.current_player_key
        
        # print("New game state after applying move...", printGrid(new_grid))
        
        if (sum(self.getMills(new_grid, self.current_player_key)) > 0) and \
            (not self.getMills(new_grid, self.current_player_key) == self.getMills(self.grid, self.current_player_key)) and \
            (sum(self.getMills(new_grid, self.current_player_key)) >= sum(self.getMills(self.grid, self.current_player_key))):
            # if 
            #   1. new_grid has mill. &&
            #   2. new_grid mills distribution not equal to self.grid's. &&
            #   3. new_grid mills count is larger than and equal to self.grid's.

            # check if current grid forms a mill. For user, ask for which one to remove; For computer, use functions from strategy heuristics.
            # print("applying move...check for mill", self.isMill(new_grid, self.current_player_key))
            tmp = "User" if self.current_player == 'u' else "Computer"
            print("## {} is forming a mill! ##".format(tmp))
            # print("current grid...", new_grid)
            if self.current_player == 'u':
                # User pick a piece to remove.
                while True:
                    target_piece = input("Select one opponent's piece to remove.")
                    target_x = int(target_piece.split(",")[0])
                    target_y = int(target_piece.split(",")[1])
                    if re.match(r"\d,\s*\d", target_piece) and new_grid[target_y][target_x] == self.opponent_player_key:
                        break
                    else:
                        print("Incorrect input, please try again.")
                new_grid[target_y][target_x] = 0
            else:
                # Computer pick a piece by strategy.
                print("Computer will pick a piece by strategy...")

        

        return State(self.opponent, is_new = False, grid = new_grid, user_pieces_num = self.user_piece_not_used, computer_pieces_num = self.computer_piece_not_used)


if __name__ == '__main__':
    new_state = State()
    print(new_state.get_coords(1))