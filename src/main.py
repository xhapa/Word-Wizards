#Uvicorn
import uvicorn
import os

#FastAPI
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

@app.get('/', response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/text', response_class=HTMLResponse)
def from_text(request: Request):
    return templates.TemplateResponse('from_text.html', {'request': request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)), reload=True)