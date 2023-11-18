num = int(input("Enter an integer (2 or greater): "))
print("the prime factors of",num,"are:")
factor = 2
while factor <= num:
    if num % factor == 0:
        print(factor)
        num //= factor
    else:
        factor += 1
