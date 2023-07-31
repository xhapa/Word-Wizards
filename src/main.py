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

# Home page
@app.get('/', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/about', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def about(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/doc', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def doc(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/history', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def history(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/text', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def from_text(request: Request):
    return templates.TemplateResponse('from_text.html', {'request': request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)), reload=True)