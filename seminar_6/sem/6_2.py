# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном
# массиве определит количество элементов,
# у которых два соседних и, при этом,
# оба соседних элемента меньше данного.

# Сначала вводится число N — количество
# элементов в массиве. Далее записаны N
# чисел — элементы массива.
# Массив состоит из целых чисел.

lst = list(map(int, input().split()))
print(sum(0 < i < len(lst) - 1 and lst[i - 1] < lst[i] and lst[i + 1] < lst[i] for i in range(len(lst))))

#________________

n = list(map(int, input().split()))
print(sum([1 for i in range(1, len(n) - 1) if n[i-1] < n[i] and n[i+1] < n[i]]))

#___________________

nums = [int(i) for i in input().split()]
print(len([i for i in range(1, len(nums) - 1) if nums[i - 1] < nums[i] > nums[i + 1]]))