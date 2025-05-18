from fastapi import FastAPI
from functools import lru_cache

app = FastAPI()

@lru_cache
def compute_fib(n: int) -> int:
    if n < 2:
        return n
    return compute_fib(n - 1) + compute_fib(n - 2)

@app.get("/fib/{n}")
async def fibonacci(n: int):
    return {"result": compute_fib(n)}
