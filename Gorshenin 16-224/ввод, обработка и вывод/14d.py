general_sum = int(input("Сумма, которую внесли вначале: "))
percent = int(input("Процентная ставка: "))
offer = int(input("Начисления процентного дохода в год: "))
years = int(input("Количество лет: "))

percent = percent / 100
hard_percent = general_sum * (1 + percent / offer ) ** (offer * years)
print(hard_percent)