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

def pieces_left_onboard(self, board, player):
    """

    >>> b = [['u' for i in range(7)] for j in range(7)]
    >>> pieces_left_onboard(b, 'u')
    49
    >>> pieces_left_onboard(b, 'b')
    0
    >>> pieces_left_onboard(b, 'w')
    0
    >>> b[0][0] = 'b'
    >>> pieces_left_onboard(b, 'u')
    48
    >>> pieces_left_onboard(b, 'b')
    1
    >>> pieces_left_onboard(b, 'w')
    0
    """
    # Flatten the board from 2D to 1D
    flattened = [item for sublist in board for item in sublist]
    return sum(list(map(lambda piece: 1 if piece == player else 0, flattened)))

if __name__ == '__main__': 
    import doctest
    doctest.testmod()
