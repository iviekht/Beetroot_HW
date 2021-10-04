#1 Если следовать условию и создать именно список.
import random
random1 = []
random2 = []
i = 0
while i < 10:
    random1.append(random.randint(1,10))
    random2.append(random.randint(1,10))
    i += 1
else:
    random1 = set(random1)
    random2 = set(random2)

print ('Set 1: %s;  Set 2: %s;' %(random1, random2))
print(random1 & random2)

#2 Изначально создавая множество
import random
random3 = {0,}
random4 = {0,}
i = 0
while i < 10:
    random1.add(random.randint(1,10))
    random2.add(random.randint(1,10))
    i += 1

print ('Set 1: %s;  Set 2: %s;' %(random1, random2))
print(random1 & random2)