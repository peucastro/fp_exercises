import math

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

le = int(input('LE = '))
re = int(input('RE = '))
pe = int(input('PE = '))
te = int(input('TE = '))

grade = (le + re + 13 * pe + 5 * te) / 100

if (not 0<=le<=100) or (not 0<=re<=100) or (not 0<=pe<=100) or (not 0<=te<=100):
    print('Input error')
    
elif pe < 40 or te < 40:
    print('RFF')
    
elif (0<=le<=100) and (0<=re<=100) and (40<=pe<=100) and (40<=te<=100):
    print(int(round_half_up(grade)))
    
