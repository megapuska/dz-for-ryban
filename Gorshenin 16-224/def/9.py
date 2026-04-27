import random
def math_test():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    print(num1)
    print("+", num2)
    answer = int(input())
    if answer == num1 + num2:
        print("Поздравляем! Правильно!")
    else:
        print("Неправильно. Правильный ответ:", num1 + num2)

print(math_test())