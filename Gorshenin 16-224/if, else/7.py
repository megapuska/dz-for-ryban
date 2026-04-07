color1 = input("Введите первый цвет:").lower() #чтобы читало с нижней буквы
color2 = input("Введите второй цвет:").lower()

colors = ["красный", "синий", "желтый"]

if color1 not in colors or color2 not in colors:
    print("Ошибка: введены недопустимые цвета. Используйте только 'красный', 'синий' или 'жёлтый'.")
else:
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        result = "фиолетовый"
    elif (color1 == "красный" and color2 == "жёлтый") or (color1 == "жёлтый" and color2 == "красный"):
        result = "оранжевый"
    elif (color1 == "синий" and color2 == "жёлтый") or (color1 == "жёлтый" and color2 == "синий"):
        result = "зелёный"

    print(result)
