
import math


approximation = 3
sign = 1
denominator = 2


i = 1
while i <= 15:
    term = 4 / (denominator * (denominator + 1) * (denominator + 2))
    approximation += sign * term
    sign *= -1
    denominator += 2
    i += 1
    print(f"Approximation {i}: {approximation}")
print(f"Actual value of π: {math.pi}")

