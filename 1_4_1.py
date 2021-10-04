#Все просроченные домашние задания я делала самостоятельно, не подсматривая в расмотренные на лекции примеры.

#1
import random
randomList = []
i = 0
while i < 10:
    randomList.append(random.random())
    i += 1
print(randomList)
print(max(randomList))
#2
import random
randomIntList = []
i = 0
while i < 10:
    randomIntList.append(random.randint(0,100))
    i += 1
print(randomIntList)
print(sorted(randomIntList)[-1])
#3
import random
randomList1 = []
i = 0
while i < 10:
    randomList1.append(random.random())
    i += 1
else:
    print(randomList1)
    print(max(randomList1))


