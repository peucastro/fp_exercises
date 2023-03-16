km = int(input('Distance to travel: '))
liter = float(input('Number of litres of fuel needed to travel 100 km: ')) / 100
price = float(input('Price per liver: '))
cost = km * liter * price
print(round(cost, 2))
