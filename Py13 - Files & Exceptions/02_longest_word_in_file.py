def longest(filename):
    with open(filename) as f:
        content = f.read()
        alist = content.split(' ')
        return max(alist, key=len)
