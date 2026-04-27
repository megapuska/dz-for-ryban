def log_method_call(func):
    def wrapper(self, *args, **kwargs):
        print(f"Метод {func.__name__} объекта {self.__class__.__name__} вызван с аргументами: {args}")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @log_method_call
    def add(self, x, y):
        return x + y

c = Calculator()
c.add(2, 3)