def find_treasure(pos, steps):
    loc = list(pos)

    up = steps.count('up')
    down = steps.count('down')
    left = steps.count('left')
    right = steps.count('right')

    loc[0] += right
    loc[0] -= left
    loc[1] += up
    loc[1] -= down

    return tuple(loc)
