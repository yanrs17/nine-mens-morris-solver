# Nine-Mens-Morris-Solver
```
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
```