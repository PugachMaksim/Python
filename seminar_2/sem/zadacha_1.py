# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

n = int(input())
fac = 1
while n:
    fac *= n
    n -= 1
print(fac)

N = int(input('Введите число: '))
num = 2
fact = 1

while num<=N:
    fact *= num
    num +=1
print(fact)