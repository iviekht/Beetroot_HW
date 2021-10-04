intList = list(range(1,101))
list1 = []
i = 0
while i < 100:
    if (i%7==0) and (i%5!=0):
        list1.append(i)
        i += 1
    else:
        i += 1
print(list1)