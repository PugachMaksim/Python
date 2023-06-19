# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import math
S = int(input())
P = int(input())
X = int()
Y = int()

D = S**2 - 4*P
print(D)
if D > 0:
    X = (S-math.sqrt(D))//2
    Y = (S + math.sqrt(D))//2
    print(round(X), round(Y))
else:
    print("Это не квадратное уравнение")

