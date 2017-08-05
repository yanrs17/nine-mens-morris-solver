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
        [b[0][0], b[3][0], b[6][0]],
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


    return True in list(map(lambda m: all(list(map(lambda p: p == player, m))), all_mill_possibilities))

if __name__ == '__main__': 
    import doctest
    doctest.testmod()
