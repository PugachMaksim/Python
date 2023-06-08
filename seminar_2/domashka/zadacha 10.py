# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно
# перевернуть
import random
orel = 0
reshka = 0
n = int(input())
for n in range(n):
    temp = random.randint(0, 2)
    if temp > 0:
        orel += 1
    elif temp <= 0:
        reshka += 1
if orel > reshka:
    min = reshka
else:
    min = orel
# print(orel)
# print(reshka)
print(min)


# От преподавателя:
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)