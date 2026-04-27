def get_dorogo():
    payment = int(input("Платеж по кредиту: "))
    insurance = int(input("Страховка: "))
    gas = int(input("Бензин: "))
    oil = int(input("Машинное масло: "))
    tires = int(input("Шины: "))
    tech = int(input("Техобслуживание: "))
    return payment + insurance + gas + oil + tires + tech

month = get_dorogo()
year = month * 12
print("Месячные расходы:", month)
print("Годовые расходы:", year)