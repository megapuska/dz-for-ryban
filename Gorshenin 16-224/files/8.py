name = input("Введите имя файла: ")

f = open(name, "r")
lines = f.readlines()
f.close()

total = 0
count = 0

for line in lines:
    number = int(line.strip())
    print(number)
    total = total + number
    count = count + 1

print("Сумма чисел:", total)
print("Количество чисел:", count)