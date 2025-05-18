# MT

A minimal FastAPI example demonstrating an optimized Fibonacci endpoint.

## Running the Application

Install dependencies:

```bash
pip install fastapi uvicorn[standard]
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/fib/10` to see the result.

## Testing

Install test dependencies and run:

```bash
pip install pytest httpx
pytest
```
