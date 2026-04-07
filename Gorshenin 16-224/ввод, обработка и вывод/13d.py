long = int(input("Длина гряды: "))
space = int(input("Пространство концевой опоры: "))
distance = int(input("Расстояние между лозами: "))

grape = (long - 2 * space) // distance

print(grape)
