def calculate():
    a = int(input("Билетов класса A: "))
    b = int(input("Билетов класса B: "))
    c = int(input("Билетов класса C: "))
    total = a * 20 + b * 15 + c * 10
    print(total)

print(calculate())