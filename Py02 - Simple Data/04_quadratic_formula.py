a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
x1 = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
print('The solutions are {} and {}'.format(round(x1, 2), round(x2, 2)))
