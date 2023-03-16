def bagdiff(xs, ys):
    for i in xs:
        if i in ys:
            xs.remove(i)
    return xs
