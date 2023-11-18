total_cost=0
while True:
    age=input()
    if age=="":
        break
    age=int(age)
    if age<=2:
        cost=0
    elif 2<age<=12:
        cost=14
    elif age>=65:
        cost=18
    else:
        cost=23
    total_cost+=cost
print(round(total_cost,2))  

