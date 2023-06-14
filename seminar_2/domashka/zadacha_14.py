# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

# f = int(input())
# i = 0
# sum = 0
# while sum <= f:
#     sum = 2**i
#     if sum <= f:
#         print (sum)
#     i += 1
#     
# От преподавателя
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1