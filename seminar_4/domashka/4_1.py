# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint
array1 = []
array2 = []
array =[]
n = int(input())
m = int(input())
for i in range(n):
    array1.append(randint(0, 10))
for i in range(m):
    array2.append(randint(0, 10))
print(array1)
print(array2)
print(sorted(list((set(array1) & set(array2)))))
