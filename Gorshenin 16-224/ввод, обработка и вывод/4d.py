tovar1 = int(input("Введите цену товара 1:"))
tovar2 = int(input("Введите цену товара 2:"))
tovar3 = int(input("Введите цену товара 3:"))
tovar4 = int(input("Введите цену товара 4:"))
tovar5 = int(input("Введите цену товара 5:"))
nalog = 0.07
final_tovar1 = tovar1 - (tovar1 * nalog)
final_tovar2 = tovar2 - (tovar2 * nalog)
final_tovar3 = tovar3 - (tovar3 * nalog)
final_tovar4 = tovar4 - (tovar4 * nalog)
final_tovar5 = tovar5 - (tovar5 * nalog)
total = sum([final_tovar1, final_tovar2, final_tovar3, final_tovar4, final_tovar5]) #Ввел список, потому что sum принимает ток 2 значения
print(f"Общая сумма всех товаров после вычета 7% налога: {total} руб.")

