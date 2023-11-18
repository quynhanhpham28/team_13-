count=0
total=0
while True:
    value = float(input("Enter a number: "))
    if value == 0:
        break
   
    elif value != 0:
        total += value
        count += 1


average = total / count
print("The average is:", average)
