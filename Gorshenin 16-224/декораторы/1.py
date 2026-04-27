def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__} с аргументами: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Завершение функции {func.__name__}")
        return result
    return wrapper

@logger
def multiply(x, y):
    return x * y

multiply(5, 3)