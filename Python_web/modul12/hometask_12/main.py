import time
from ipaddress import ip_address
from typing import Callable

import redis.asyncio as redis
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import text
from starlette.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter

from src.database.db import get_db
from src.routes import contacts, auth, users
from src.conf.config import settings

app = FastAPI()


@app.on_event("startup")
async def startup():
    """
    The startup function is called when the application starts up.
    It's a good place to initialize things that are needed by your app,
    such as connecting to databases or initializing caches.

    :return: A coroutine
    :doc-author: Trelent
    """
    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0)
    await FastAPILimiter.init(r)

origins = [
    "http://localhost:5500", "http://127.0.0.1:5500"
    ]
# захист від браузерів
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# білий список дозволених ip
ALLOWED_IPS = [ip_address('192.168.1.0'), ip_address('172.16.0.0'), ip_address("127.0.0.1")]


@app.middleware("http")
async def limit_access_by_ip(request: Request, call_next: Callable):
    ip = ip_address(request.client.host)
    """
    The limit_access_by_ip function is a middleware function that limits access to the API by IP address.
    It checks if the client's IP address is in ALLOWED_IPS, and if not, returns a 403 Forbidden response.
    
    :param request: Request: Get the ip address of the client
    :param call_next: Callable: Pass the next function in the chain to be called
    :return: A Json response object with a status code of 403
    :doc-author: Trelent
    """
    if ip not in ALLOWED_IPS:
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={"detail": "Not allowed IP address"})
    response = await call_next(request)
    return response


@app.middleware('http')
async def custom_middleware(request: Request, call_next):
    """
    The custom_middleware function is a middleware function that adds the time it took to process the request
    to the response headers. This can be used to measure performance of an API endpoint.

    :param request: Request: Get the request object
    :param call_next: Pass the request to the next middleware in line
    :return: A response with a header 'performance' that contains the time it took to process
    :doc-author: Trelent
    """
    start_time = time.time()
    response = await call_next(request)
    during = time.time() - start_time
    response.headers['performance'] = str(during)
    return response

templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse, description='Main Page')
async def root(request: Request):
    """
    The **root** function is the main function of the application.
    It returns a TemplateResponse object, which renders an HTML template with data from a context dictionary.
    The context dictionary contains information about the request and response objects, as well as any other variables
    you want to pass into your templates.

    :param request: Request: Get information about the request that is being made
    :return: A template response
    :doc-author: Trelent
    """
    return templates.TemplateResponse('index.html', {"request": request, "title": "Contacts App"})


@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    """
    The healthchecker function is a simple function that checks the health of the database.
    It does this by making a request to the database and checking if it returns any results.
    If there are no results, then we know something is wrong with our connection to the database.

    :param db: Session: Get the database session from the dependency
    :return: A dictionary with a message
    :doc-author: Trelent
    """
    try:
        # Make request
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


app.include_router(auth.router, prefix='/api')
app.include_router(contacts.router, prefix='/api')
app.include_router(users.router, prefix='/api')
