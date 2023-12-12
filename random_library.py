from random import choice, randint

# Coin toss application
coin_result = choice(["Heads", "Tails"])
print(coin_result)

# Rondom number between two specified values
x = int(input("Write the lowest value: "))
y = int(input("Write the maximum value: "))
rondom_num = randint(x,y)
print(rondom_num)