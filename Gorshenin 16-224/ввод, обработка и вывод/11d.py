group = int(input("Количество учеников: "))
boy = int(input("Учащиеся мужского пола:"))
girl = int(input("Учащиеся женского пола: "))
group = boy + girl
boys = (boy / group) * 100
girls = (girl / group) * 100
print(boys,girls)
