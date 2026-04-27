def calculate():
    fat = int(input("Граммы жиров: "))
    carbs = int(input("Граммы углеводов: "))
    kal_fat = fat * 9
    kal_carbs = carbs * 4
    print("Калории от жиров:", kal_fat)
    print("Калории от углеводов:", kal_carbs)

print(calculate())