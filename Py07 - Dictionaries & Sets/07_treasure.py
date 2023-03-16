def treasure(clues):
    loc = (0, 0)
    while loc in clues.keys():
        goto = clues[loc]
        clues.pop(loc)
        loc = goto
    return loc
