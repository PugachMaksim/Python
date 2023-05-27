# Иван Васильевич пришел на рынок и решил купить
# два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком
# много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса соответствующего арбуза


number = 0
while number <= 0:
    number = int(input("Input number: "))

max_num = 0
min_num = 999

for i in range(number):
    watermelon = int(input(f"Input {i+1} watermelon's weight: "))
    if watermelon > max_num:
        max_num = watermelon
    if watermelon < min_num:
        min_num = watermelon

print(max_num, min_num)
