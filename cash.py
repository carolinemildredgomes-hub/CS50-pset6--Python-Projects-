from cs50 import get_float

# prompt until non-negative
while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

# convert to cents and avoid floating-point surprises
cents = int(round(change * 100))

coins = 0
for coin in (25, 10, 5, 1):
    coins += cents // coin
    cents %= coin

print(coins)
