# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random

n = int(input())
list = [random.randint(0, 20) for i in range(n)]
print(*list)

list2 = []
for i in range(len(list)):
    if 5 <= list[i] <= 15:
        list2.append(i)
print(*list2)