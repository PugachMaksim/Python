# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

s = input().split()
result = {}
for n in s:
    if n in result:
        print(f'{n}_{result[n]}', end=' ')
    else:
        print(n, end=' ')
    result[n] = result.get(n, 0) + 1


st, dct = input(), {}
for i in st.split():
    if dct.setdefault(i, 0) > 0:
        print(f'{i}_{dct[i]}', end=' ')
    else:
        print(f'{i}', end=' ')
    dct[i] += 1