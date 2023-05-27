# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

f = int(input())
i = 0
sum = 0
while sum <= f:
    sum = 2**i
    if sum <= f:
        print (sum)
    i += 1