from move import Move


class TippyMove(Move):
    ''' A move in the game of Tippy.
    
    position: int --- the position of the game chosen.
    '''
    
    def __init__(self, position):
        ''' (TippyMove, int) -> NoneType
        
        Initialize a new TippyMove for choosing the position.
        
        Assume: position is a positive integer.
        '''
        self.position = position
        
    def __repr__(self):
        ''' (TippyMove) -> str
        
        Return a string representation of this TippyMove.
        >>> t = TippyMove(1)
        >>> t
        TippyMove(1)
        '''
        return 'TippyMove({})'.format(str(self.position))
    
    def __str__(self):
        ''' (TippyMove) -> str
        
        Return a string representation of this TippyMove
        that is suitable for users to read.
        
        >>> t = TippyMove(1)
        >>> print(t)
        Position: 1
        '''
        return 'Position: {}'.format(str(self.position))
    
    def __eq__(self, other):
        ''' (TippyMove, TippyMove) -> bool
        
        Return True iff this TippyMove is the same as other.
        
        >>> t1 = TippyMove(1)
        >>> t2 = TippyMove(1)
        >>> t3 = TippyMove(2)
        >>> print(t1 == t2)
        True
        >>> print(t1 == t3)
        False
        '''
        return (isinstance(other, TippyMove) and 
                self.position == other.position)