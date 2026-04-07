members = int(input("Количество участников пикника: "))
hot_dogs = int(input("Количество хот-догов на 1 участника: "))

total_hotdogs = members * hot_dogs 

sosiski_pack = 10
bags_pack = 8

if total_hotdogs % sosiski_pack == 0:
    packs_of_sosiski = total_hotdogs // sosiski_pack
else:
    packs_of_sosiski = total_hotdogs // sosiski_pack + 1

if total_hotdogs % bags_pack == 0:
    packs_of_bags = total_hotdogs // bags_pack
else:
    packs_of_bags = total_hotdogs // bags_pack + 1

total_sosiski = packs_of_sosiski * sosiski_pack
total_bags = packs_of_bags * bags_pack

leftover_sosiski = total_sosiski - total_hotdogs
leftover_bags = total_bags - total_hotdogs

print(f"Количество участников: {members}")
print(f"Хот‑догов на участника: {hot_dogs}")
print(f"Всего хот‑догов нужно: {total_hotdogs}")
print(f"Минимально необходимое количество упаковок с сосисками: {packs_of_sosiski}")
print(f"Количество оставшихся сосисок: {leftover_sosiski}")
print(f"Минимально необходимое количество упаковок с булочками: {packs_of_bags}")
print(f"Количество оставшихся булочек: {leftover_bags}")
