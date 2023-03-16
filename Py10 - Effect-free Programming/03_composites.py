def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def get_composites(n):
    for i in range(4, n+1):
        if is_prime(i):
            pass
        else:
            yield i
