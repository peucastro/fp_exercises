def division(a, b):
    try:
        res = '{}/{} = {}'.format(a, b, a/b)
    except ZeroDivisionError:
        res = "can't divide by 0!"
    except:
        res = 'unsupported operand type(s) for division'

    return res
