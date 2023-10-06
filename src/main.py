#Python
from typing import Annotated

#Uvicorn
import uvicorn
import os

#FastAPI
from fastapi import FastAPI, Form, Query, Request, Depends, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Config
from config.db import engine, Session, create_db_and_tables, get_session

# Router
from routers.from_file import file_router
from routers.from_text import text_router
from routers.from_url import url_router
from routers.analyze import analyze_route

# NLP
from nlp.pipeline_downloader import pipeline_downloader

# Services
from services.nlp_data import NLPDataService

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
app.include_router(analyze_route)

# Home page
@app.get('/', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def home(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/about', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def about(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/doc', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def doc()-> RedirectResponse:
    return RedirectResponse(url='https://github.com/xhapa/Word-Wizards')

@app.get('/history', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def history(request: Request, db : Session = Depends(get_session))-> Jinja2Templates:
    nlp_data_list = NLPDataService(db).get_all_nlp_data()
    return templates.TemplateResponse('history.html', {'request': request, 'nlp_list': nlp_data_list})

@app.get('/history/{nlp_data_id}', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def to_analyze(nlp_data_id : int,
    db : Session = Depends(get_session)
    ):
    nlp_data = NLPDataService(db).get_by_id_nlp_data(nlp_data_id)
    text = nlp_data.text
    id_data = nlp_data.nlp_data_id
    url = analyze_route.url_path_for('analyze_it')
    response = RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="text_data", value=text.encode("utf-8"))
    response.set_cookie(key="id_data", value=id_data)
    return response

@app.post('/history/update/{nlp_data_id}', response_class=HTMLResponse, response_model=None, status_code=200, tags=["Home"])
async def update_text(nlp_data_id : int ,text_up : Annotated[
        str, 
        Form(
            title= 'Text',
            description='Text to nlp analysis'
        )
    ] = None, 
    db : Session = Depends(get_session)
    ):
    await NLPDataService(db).update_nlp_data(nlp_data_id, text_up)
    url = app.url_path_for('history')
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND) 

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)), reload=True)