decimal = int(input("Enter a decimal number: "))


result = ""
q = decimal


while q > 0:
    r = q % 2
    result = str(r) + result
    q = q // 2


print("The binary representation of", decimal, "is", result)
