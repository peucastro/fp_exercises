def change(money):
    coins = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    for coin in coins:
        while money >= coin:
            money -= coin
            coins[coin] += 1
    return coins
