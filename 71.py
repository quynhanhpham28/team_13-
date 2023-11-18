x = float(input('X: '))


guess = x / 2
prev = x


DP = 4 # no. of decimal places accuracy
MARGIN = 10 ** -DP


while abs(guess - prev) > MARGIN:
    prev = guess
    guess = (guess + x / guess) / 2


print("{:.2f}".format(guess))
