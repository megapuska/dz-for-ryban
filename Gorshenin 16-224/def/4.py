def calculate():
    actual = int(input("Фактическая стоимость: "))
    review = actual * 0.6
    tax = review / 100 * 0.72
    print("Оценочная стоимость:", review)
    print("Налог на имущество:", tax)

print(calculate())