from fastapi import Request
from time import time

async def log_request_time(request: Request, call_next):
    start = time.time()
    
    response = await call_next(request)
    duration = time.time() - start
    response.headers["X-Process-Time"] = str(round(duration, 4))
    print(f"[Middleware] {request.method} {request.url.path} took {duration:.4f}s")
    return response
    