from game_state import GameState
from tippy_move import TippyMove


class TippyGameState(GameState):
    ''' The state of a tippy game.
    
    size: int   --- size of the game
    '''
    
    def __init__(self, p, interactive=False, position=[]):
        ''' (TippyGameState, int, bool, list of moves) -> NoneType

        Initialize TippyGameState self with position to be []

        Assume: self.size is always an positive integer.
        '''
        self.position = position
        # Ask for the size of the game.
        if interactive:
            self.size = int(input('Size of the game? '))
            while self.size < 3:
                self.size = int(input('Size of the game? '))
            self.position = []
            for i in range(self.size * self.size):
                self.position.append(str(i + 1))            
        self.size = int((len(self.position)) ** 0.5)      
        # Inherit from the upperclass.
        GameState.__init__(self, p, interactive=False)
        
        # Get instructions
        self.instructions = 'Choose a number available. '
        self.instructions += 'You are X and the computer is O.'
        
        # Get the winner. There is no winner at the beginning of the game.
        self.won = None   
        
        # Track the moves made by 2 players and the moves available.
        self.current = []
        self.oppo = []
        self.available = []
        if self.next_player == 'p2':
            sign1 = 'O'
            sign2 = 'X'
        elif self.next_player == 'p1':
            sign1 = 'X'
            sign2 = 'O'
        position = 1
        for i in self.position:
            if i == sign1:
                self.current.append(position)
            elif i == sign2:
                self.oppo.append(position)
            else:
                self.available.append(position)
            position += 1

        if is_tippy(self.size, self.current):
            self.won = self.next_player
            self.over = True
        elif is_tippy(self.size, self.oppo):
            self.won = self.opponent()   
            self.over = True
        
        if self.available == []:
            self.over = True
            
    def __repr__(self):
        ''' (TippyGameState) -> str

        Return a string representation of TippyGameState self
        that evaluates to an equivalent TippyGameState
        
        >>> s = TippyGameState('Player1', False)
        >>> s
        Next Player: Player1
        '''
        return 'Next Player: {0}'.format(self.next_player)

    def __str__(self):
        ''' (TippyGameState) -> str

        Return a convenient string representation of TippyGameState self.	
        '''
        import math
        size = int(math.sqrt(len(self.position)))
        current = '\n' + self.__repr__()
        for i in range(len(self.position)):
            if i % size == 0:
                current += '\n'
            current += self.position[i] + '\t'
        return current

    def __eq__(self, other):
        ''' (TippyGameState, TippyGameState) -> bool

        Return True iff this TippyGameState is the equivalent to other.

        >>> s1 = TippyGameState('p1', False)
        >>> s2 = TippyGameState('p1', False)
        >>> s1 == s2
        True
        '''
        return (isinstance(other, TippyGameState) and
                self.next_player == other.next_player)
    
    def get_move(self):
        '''(TippyGameState) -> Move

        Prompt user and return a move.
        '''
        return input('Make a move: ')

    def apply_move(self, move):
        '''(GameState, Move) -> GameState

        Return the new game state reached by applying move to
        state self, or None if the move is illegal.
        '''
        if move in self.possible_next_moves():
            new_position = self.position[:]
            if self.next_player == 'p1':
                new_position[int(move) - 1] = 'X'
            else:
                new_position[int(move) - 1] = 'O'
                
            return TippyGameState(self.opponent(), False, new_position)
        else:
            return None

    def winner(self, player):
        ''' (GameState, str) -> bool

        Return whether player has won the game.

        Assume: player is either 'p1' or 'p2'
                and there are no more legal moves; the game is over
        '''
        if self.won == player:
            return True
        return False

    def possible_next_moves(self):
        ''' (GameState) -> list of Move

        Return a (possibly empty) list of moves that are legal
        from the present state.
        '''
        possible_moves = []
        for i in self.position:
            if i not in ['X', 'O']:
                possible_moves.append(i)
        #self.won = self.next_player        
        
        if self.current != []:
            if is_tippy(self.size, self.current):
                return []    
        
        return possible_moves

    def rough_outcome(self):
        '''(GameState) -> float

        Return estimate of outcome based only on current state. Value
        is in interval [LOSE, WIN]
        >>> TGS = TippyGameState('p1', False)
        >>> TGS.position = ['1', 'X', '3', 'O', 'X', 'X', 'O', '8', 'O']
        >>> TGS.rough_outcome()
        0.0
        '''
        
        if len(self.current) <= 2:
            return TippyGameState.DRAW
        else:
            for j in self.moves_available:
                moves_current = self.current[:]
                
                # If there is at one move leads to win.
                if is_tippy(self.size, moves_current + [j]):
                    return TippyGameState.WIN
                
                # If all the moves lead to lose.
                elif all([is_tippy(self.size, self.moves_opponent + [k])
                          for k in moves_current.remove(j)]):
                    return TippyGameState.LOSE
                
                # Else: It is a tie.
                else:
                    return TippyGameState.DRAW


def is_tippy(size, move):
    ''' (int, list of int) -> bool
    
    Return whether all the moves made can make a tippy.
    
    Assume: All the integers in move are in the interval [1, size*size]
    Assume: len(move) >= 4
    >>> is_tippy(3, [1, 2, 5 ,6])
    True
    >>> is_tippy(4, [1, 5, 6, 10])
    True
    >>> is_tippy(3, [1, 2, 3, 4, 6])
    False
    >>> is_tippy(3, [5, 6, 7, 8])
    True
    '''
    # There are 4 possibilities:
    # -|   |- |   | 
    #  |- -|  -- --
    #          | |
    
    move.sort()
    tippy = []
    
    for i in move:
        # -|  <- This possibility
        #  |-        
        if i % size not in [0, size - 1]:

            if all([(i + 1) in move, 
                    (i + size + 1) in move, 
                    (i + size + 2) in move]):
                tippy += [True]

        #  |- <- This possibility
        # -|        
        if i % size not in [0, 1]:
            if all([(i + 1) in move, 
                    (i + size - 1) in move, 
                    (i + size) in move]):
                tippy += [True]
        
        # |  <- This possibility
        # --
        #  |
        if (i % size != 0) and ((i - 1) // size != (size - 2)):
            if all([(i + size)in move,
                    (i + size + 1)in move,
                    (i + size * 2 + 1)in move]):
                tippy += [True]
        #  | <- This possibility
        # --
        # |
        if (i % size != 1) and ((i - 1) // size != (size - 2)):
            if all([(i + size) in move,
                    (i + size - 1) in move,
                    (i + size * 2 - 1) in move]):
                tippy += [True]
    # Return whether there is at least one tippy.
    return (True in tippy)


if __name__ == '__main__':
    import doctest
    doctest.testmod()