try:
    octa = input('Enter octa: ')
    decim = int(octa, base=8)
    print(decim)
except ValueError:
    print('Not a valid number.')
