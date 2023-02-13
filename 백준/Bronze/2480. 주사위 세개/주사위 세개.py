dice1, dice2, dice3 = map(int, input().split())
price = 0

if dice1 == dice2 == dice3:
    price = 10000 + dice1 * 1000
elif (dice1 != dice2) and (dice1 != dice3) and (dice2 != dice3):
    price = max(dice1, dice2, dice3) * 100
else:
    if dice1 == dice2:
        price = 1000 + dice1 * 100
    elif dice1 == dice3:
        price = 1000 + dice1 * 100
    else:
        price = 1000 + dice2 * 100

print(price)
