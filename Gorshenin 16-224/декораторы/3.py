def positive_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Аргументы должны быть положительными")
        return func(*args, **kwargs)
    return wrapper

@positive_args
def rectangle_area(a, b):
    return a * b

rectangle_area(5, 3) # OK
rectangle_area(5, -2) # Аргументы должны быть положительными