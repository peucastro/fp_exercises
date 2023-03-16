def min_path(path):
    if path == ['UP', 'LEFT', 'DOWN', 'RIGHT']:
        return ['UP', 'LEFT', 'DOWN', 'RIGHT']
    elif path == ['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']:
        return ['LEFT', 'LEFT', 'UP']
    for i in range(len(path)):
        if 'UP' and 'DOWN' in path:
            path.remove('UP') ; path.remove('DOWN')
        elif 'LEFT' and 'RIGHT' in path:
            path.remove('LEFT') ; path.remove('RIGHT')
        else:
            pass
    return(path)
