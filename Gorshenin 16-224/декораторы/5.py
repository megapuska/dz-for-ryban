import time

class RateLimitExceeded(Exception):
    pass

def rate_limit(max_calls, period):
    def decorator(func):
        calls = []
        def wrapper(*args, **kwargs):
            now = time.time()
            while calls and now - calls[0] > period:
                calls.pop(0)
            if len(calls) >= max_calls:
                raise RateLimitExceeded("Лимит вызовов превышен. Подождите.")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(2, 5)
def request():
    print("Request sent")

request()
request()
request()