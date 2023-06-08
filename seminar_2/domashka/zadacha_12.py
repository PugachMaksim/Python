# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# S = int(input())
# P = int(input())
# X = int()
# Y = int()
# x2+(-sum*x)+proizv = 0
# S = a + b
# P = a * b
# for X in range(1, P+1):
#     for Y in range(1, P+1):
#         if X+Y == S and X*Y == P:
#             print(X, Y)
#             break
# found = False
# for X in range(1, P+1):
#     for Y in range(1, P+1):
#         if X+Y == S and X*Y == P:
#             print(X, Y)
#             found = True
#             break
#     if found:
#         break

# От преподавателя
x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)