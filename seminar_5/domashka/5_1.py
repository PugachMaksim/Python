# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

A = int(input())
B = int(input())

#sum = 0
def stepen(num, b):
    if b == 1:
        return num
    return num * stepen(num, b-1)
print(stepen(A, B))
2*2*2*2*2