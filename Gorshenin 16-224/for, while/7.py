days = int(input("Введите количество дней: "))
zp_day = 1  
total_copeiki = 0

for day in range(1, days + 1):
    print(f"{day}\t{zp_day}")
    total_copeiki += zp_day
    zp_day *= 2 

total_rubles = total_copeiki / 100
print(f"Общая сумма: {total_rubles} рублей")