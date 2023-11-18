import random
max_num = random.randint(1, 100)
updates = 0
print( max_num)
for _ in range(99):
    new_num = random.randint(1, 100)
    if new_num > max_num:
        max_num = new_num
        updates += 1
        print(new_num,"<== Update")
    else:
        print(new_num)
print("the maximum value found was", max_num)
print("the maxium value was updated", updates,"times")
