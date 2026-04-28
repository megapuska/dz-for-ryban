f = open("golf.txt", "r")
lines = f.readlines()
f.close()

for i in range(0, len(lines), 2):
    name = lines[i].strip()
    score = lines[i + 1].strip()
    print("Игрок:", name, "Счет:", score)