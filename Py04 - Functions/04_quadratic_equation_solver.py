def solver(a, b, c):
    delta = (b ** 2 - 4 * a * c)
    list = []
    if delta > 0:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        list = [x1, x2]
    if delta == 0:
        x = (-b + delta ** (1 / 2)) / (2 * a)
        list = [x]
    if delta < 0:
        list = []
    return (sorted(list))
