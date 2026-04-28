name = input("Введите имя файла: ")

f = open(name, "r")
lines = f.readlines()
f.close()

num = 1
for line in lines:
    print(str(num) + ": " + line.strip())
    num = num + 1