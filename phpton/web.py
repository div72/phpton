from functools import wraps

ROUTES = {}


def route(path: str):
    def decorator(f):
        ROUTES[path] = f

        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return decorator
