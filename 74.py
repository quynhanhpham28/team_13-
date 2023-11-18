print("        ", end="  ")
for i in range(1, 11):
    print(i, end="\t")
print("")
for i in range(1, 11):
    print(i, end="\t  ")
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")