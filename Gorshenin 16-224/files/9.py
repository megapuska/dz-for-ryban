f = open("golf.txt", "w")

while True:
    name = input("Введите имя игрока (или 'выход' для завершения): ")
    if name == "выход":
        break
    score = input("Введите счет игрока: ")
    f.write(name + "\n")
    f.write(score + "\n")

f.close()
print("Данные сохранены в файл golf.txt")