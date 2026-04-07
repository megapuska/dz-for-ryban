speed = int(input("Введите скорость: "))
hours = int(input("Введите общее время движения: "))
s_total = 0
for i in range(1, hours + 1):
    s_hour = speed
    s_total += s_hour
print(s_total)