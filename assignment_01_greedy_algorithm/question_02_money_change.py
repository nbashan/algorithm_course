def change(bill, c, k):
    coins = [c**i for i in range(k+1)][::-1]
    number_coins = 0
    while bill > 0:
        x = bill // coins[0]
        bill -= x * coins[0]
        number_coins += x
        coins = coins[1:]
    return number_coins


print(change(100,2,3))
