imya_faila = input("Введите имя файла: ")

f = open(imya_faila, "r")
stroki = f.readlines()
f.close()

kolichestvo = len(stroki)
if kolichestvo > 5:
    kolichestvo = 5

for i in range(kolichestvo):
    print(stroki[i].strip())