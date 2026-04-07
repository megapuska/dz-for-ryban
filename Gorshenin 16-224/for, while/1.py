total_errors = 0
for day in range(1, 6):
    errors_today = int(input("Введите количество ошибок в разные дни: "))
    total_errors += errors_today
print(total_errors)
