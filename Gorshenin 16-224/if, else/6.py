day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

magic = day * month
if magic == year:
    print("Дата является магической!")
else:
    print("Дата не является магической")
