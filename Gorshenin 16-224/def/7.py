def calculate():
    sales = int(input("Общий объем продаж за месяц: "))
    federal = sales * 0.05
    municipal = sales * 0.025
    total = federal + municipal
    print("Федеральный налог:", federal)
    print("Муниципальный налог:", municipal)
    print("Общий налог:", total)

print(calculate())