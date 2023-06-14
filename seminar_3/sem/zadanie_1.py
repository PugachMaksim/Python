# Дан список чисел. Определите,
# сколько в нем встречается различных чисел.

# list_nums = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
import random
print("\033c")

number = int(input("Введите максимум чисел: "))
num = []
for i in range (number):
    num.append(random.randint(-3, 3))
print (num)
print(len(set(num)))


print(len(set(input().split())))