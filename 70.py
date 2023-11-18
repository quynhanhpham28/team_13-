text = input("Plain Text : ")
k = int(input("Shift pattern :"))
result = ''
for i in text:
    char = i
    if "A"<=char<="Z":
        result = result + chr((ord(char) + k-65) % 26 + 65 )
    elif 97<=ord(char)<=122:
        result = result + chr((ord(char) + k - 97) % 26 + 97)
    else:
        result = result + char
print(result)
