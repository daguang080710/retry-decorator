import time, random, functools

class RetryError(Exception):
    def __init__(self, last_exception, attempts):
        self.last_exception = last_exception
        self.attempts = attempts
        super().__init__(f"Failed after {attempts} attempts: {last_exception}")

def retry(max_attempts=3, backoff=1.0, max_backoff=30.0, jitter=True, exceptions=(Exception,)):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    if attempt == max_attempts:
                        raise RetryError(e, attempt)
                    wait = min(backoff * (2 ** (attempt - 1)), max_backoff)
                    if jitter:
                        wait *= (0.5 + random.random())
                    time.sleep(wait)
            raise RetryError(last_exc, max_attempts)
        return wrapper
    return decorator
