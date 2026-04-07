moneta_5 = int(input("Введите количество монет по 5 копеек: "))
moneta_10 = int(input("Введите количество монет по 10 копеек: "))
moneta_50 = int(input("Введите количество монет по 50 копеек: "))

total_rubles = (moneta_5 * 0.05) + (moneta_10 * 0.10) + (moneta_50 * 0.50)

if total_rubles == 1:
    print("Поздравляем, вы выиграли!")
elif total_rubles > 1:
    print("Сумма слишком большая — вы превысили один рубль.")
else:
    print("Сумма слишком мала — не хватает до одного рубля.")

print(total_rubles)