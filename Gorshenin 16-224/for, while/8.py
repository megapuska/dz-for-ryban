total = 0
while True:
    num = int(input("Введите число: "))
    if num < 0:
        break
    total += num
print(total)