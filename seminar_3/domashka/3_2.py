# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint


mass = []
K = int(input())
for i in range(K):
    mass.append(randint(0, 20))
print(mass)

X = int(input())
massMin = mass[0]
razn = (mass[0] - X)
if razn < 0:
    razn = razn * -1
for i in range(1, len(mass)):
    temp = mass[i]-X
    if temp < 0:
        temp = temp * -1
    if razn > temp:
        razn = temp
        massMin = mass[i]
print(f"Ближайшее значение к {X} -> {massMin}")