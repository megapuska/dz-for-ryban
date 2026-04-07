pocket_number = int(input("Введите число кармана рулетки: "))

if pocket_number == 0:
    color = "зелёный"
elif 1 <= pocket_number <= 10:
    if pocket_number % 2 == 1:  
        color = "красный"
    else:  
        color = "чёрный"
elif 11 <= pocket_number <= 18:
    if pocket_number % 2 == 1:  
        color = "чёрный"
    else:  
        color = "красный"
elif 19 <= pocket_number <= 28:
    if pocket_number % 2 == 1:  
        color = "красный"
    else:  
        color = "чёрный"
elif 29 <= pocket_number <= 36:
    if pocket_number % 2 == 1:  
        color = "чёрный"
    else:  
        color = "красный"

if 0 <= pocket_number <= 36:
    print(f"Карман {pocket_number} — {color}.")
else:
    print("Ошибка: номер кармана должен быть в диапазоне от 0 до 36.")
