budget = int(input("Введите сумму, выделенную на месяц: "))
total_rasxodi = 0.0
print("Введите суммы расходов по статьям (для завершения введите 0):")
while True:
    rasxodi = int(input("Сумма расхода: "))
    if rasxodi == 0:
        break
    total_rasxodi += rasxodi
    print(f"Нарастающий итог расходов: {total_rasxodi}")
difference = budget - total_rasxodi
if difference > 0:
    print(f"Вы сэкономили {difference} рублей.")
elif difference < 0:
    print(f"Вы перерасходовали {abs(difference)} рублей.") # абс убирает знак минус от числа
else:
    print("Ваши расходы точно соответствуют бюджету")
