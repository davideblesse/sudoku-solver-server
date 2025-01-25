import concurrent.futures
from fastapi import HTTPException

def timeout(seconds: int):
    """
    Decorator to limit the execution time of a function.
    If the function does not complete within the given time, raise an HTTPException.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(func, *args, **kwargs)
                try:
                    return future.result(timeout=seconds)
                except concurrent.futures.TimeoutError:
                    raise HTTPException(
                        status_code=408,
                        detail=f"Request timed out. The operation exceeded the time limit of {seconds} seconds."
                    )
        return wrapper
    return decorator
