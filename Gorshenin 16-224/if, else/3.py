age = int(input("Введите возраст:"))
if age <= 1:
    print("Младенец")
elif 1 < age < 13:
    print("Ребенок")
elif 13 <= age < 20:
    print("Подросток")
else:
    print("Взрослый")
