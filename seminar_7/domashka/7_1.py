# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

text = input().upper()
spisok = text.split()
max_syllable = 0
max_syllable_2 = 0
Temp = spisok[0]
vowels = ('А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я',)
for i in range(0, len(Temp)):
    if Temp[i] in vowels:
        max_syllable += 1
if max_syllable != 0:
    for i in range(1, len(spisok)):
        max_syllable_2 = 0
        temp = spisok[i]
        for j in range(0, len(temp)):
            if temp[j] in vowels:
                max_syllable_2 += 1
        if max_syllable != max_syllable_2:
            print('Пам парам')
            break
elif max_syllable == 0:
    print('Пам парам')
if max_syllable == max_syllable_2 and max_syllable != 0: print('Парам пам-пам')
