n = int(input("Enter the first positive integer: "))
m = int(input("Enter the second positive integer: "))
d = min(n, m)
while d > 0:
    if n % d == 0 and m % d == 0:
        break
    d -= 1
print("The greatest common divisor of", n, "and", m, "is", d)
