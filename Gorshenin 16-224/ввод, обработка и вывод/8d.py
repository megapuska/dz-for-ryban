food = int(input("Введите общую цену блюд: "))
nalog_sell = food * 0.07
tea = food * 0.18
all_price = food + nalog_sell + tea
print(f"Общая сумма: {food}, {nalog_sell:.2f}, {tea}, {all_price}") #добавил 2f потому что получалось оч большое число
