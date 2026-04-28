import random

name = input("Введите имя файла: ")
count = int(input("Сколько случайных чисел записать в файл: "))

f = open(name, "w")

for i in range(count):
    number = random.randint(1, 500)
    f.write(str(number) + "\n")

f.close()
print("Готово!")