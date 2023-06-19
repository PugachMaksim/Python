# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

list_nums = list(map(int, input().split()))
steps = int(input())

for i in range(steps):
            list_nums.insert(0, list_nums.pop())
print(list_nums)


lst = list(map(int, input().split()))
k = int(input()) % len(lst) + 1
lst = [lst[i - k] for i in range(len(lst))]
print(lst)