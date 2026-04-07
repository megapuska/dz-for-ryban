years = int(input("Введите количество лет: "))
total_months = 0
total_osadki = 0.0

for year in range(1, years + 1):
    for month in range(1, 13):
        osadki = float(input(f"Месяц {month}: количество осадков (мм): "))
        total_osadki += osadki
        total_months += 1

if total_months > 0:
    average_osadki = total_osadki / total_months
else:
    average_osadki = 0.0

print(f"Общее количество месяцев: {total_months}")
print(f"Общее количество осадков: {total_osadki} мм")
print(f"Средняя толщина слоя осадков в месяц: {average_osadki} мм")