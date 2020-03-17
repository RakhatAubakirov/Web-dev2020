from math import sqrt
a = int(input())
i = 0
while i < a:
    if sqrt(i).is_integer == True:
        print(i)
    i += 1
