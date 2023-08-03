#Python
from typing import Annotated

#Uvicorn
import uvicorn
import os

#FastAPI
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Config
from config.db import create_db_and_tables

# Router
from routers.from_file import file_router
from routers.from_text import text_router
from routers.from_url import url_router

# NLP
from nlp.pipeline_downloader import pipeline_downloader

app = FastAPI()
app.title = 'Word Wizards'
app.version = '0.0.1'

# Static
app.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

# Database
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    pipeline_downloader()

# Routers
app.include_router(file_router)
app.include_router(text_router)
app.include_router(url_router)

# Home page
@app.get('/', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def home(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/about', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def about(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/doc', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def doc(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/history', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def history(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('home.html', {'request': request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)), reload=True)