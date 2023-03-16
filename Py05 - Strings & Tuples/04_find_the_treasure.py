def map(pos, steps):
    coord = list(pos)
    steps = steps.replace('-', ' ').split()
    
    for i in steps:
        if i == 'up':
            coord[1] += 1
        elif i == 'down':
            coord[1] -= 1
        elif i == 'left':
            coord[0] -= 1
        elif i == 'right':
            coord[0] += 1
            
    return tuple(coord)
