sugar = 1.5
oil = 1
muka = 2.75
pirozki = 48
need_pirozki = int(input("Введите количество пирожков: "))
need_sugar = (sugar / pirozki) * need_pirozki
need_oil = (oil / pirozki) * need_pirozki
need_muka = (muka / pirozki) * need_pirozki
print(f"Вот нужное количество ингридиентов: {need_sugar}, {need_oil}, {need_muka} ")
