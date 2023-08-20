# Python
from typing import Annotated

# FastAPI
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Config
from config.db import engine, Session, get_session

# Services
from services.nlp_data import NLPDataService

#SQLModels
from sqlmodels.nlp_data import NLPData

analyze_route = APIRouter(prefix='/analyze', tags=['Analyze'])

# Static
analyze_route.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

@analyze_route.get('/', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def analyze_it(
    request: Request,
    db : Session
        = Depends(get_session)
)-> Jinja2Templates:
    text = request.cookies.get("text_data")
    await NLPDataService(db).create_nlp_data(text=text)
    lang = NLPDataService(db).get_last_nlp_data().lang
    return templates.TemplateResponse('analyze_menu.html', {'request': request, 'lang':lang})

@analyze_route.get('/words-count', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def words_count(
    request: Request,
    db : Session 
        = Depends(get_session)
)-> Jinja2Templates:
    last_data = NLPDataService(db).get_last_nlp_data()
    count = last_data.word_count
    lang = last_data.lang
    return templates.TemplateResponse('./content/words_count_page.html',
                                      {
                                        'request': request,
                                        'count':count,
                                        'lang':lang
                                        })

@analyze_route.get('/entities', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def entities(
    request: Request,
    db : Session
        = Depends(get_session)
)-> Jinja2Templates:
    last_data = NLPDataService(db).get_last_nlp_data()
    ent = last_data.entities
    lang = last_data.lang
    return templates.TemplateResponse('./content/entities_page.html', 
                                      {
                                        'request': request, 
                                        'entities':ent, 
                                        'lang':lang
                                        })

@analyze_route.get('/keywords', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def keywords(
    request: Request,
    db : Session
        = Depends(get_session)
)-> Jinja2Templates:
    last_data = NLPDataService(db).get_last_nlp_data()
    key = last_data.keywords
    lang = last_data.lang
    return templates.TemplateResponse('./content/keywords_page.html', 
                                      {
                                          'request': request, 
                                          'keywords':key, 
                                          'lang':lang
                                          })

@analyze_route.get('/summary', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def summarize(
    request: Request,
    db : Session 
        = Depends(get_session)
)-> Jinja2Templates:
    last_data = NLPDataService(db).get_last_nlp_data()
    summ = last_data.summary
    lang = last_data.lang
    return templates.TemplateResponse('./content/summary_page.html', 
                                      {
                                          'request': request, 
                                          'summary':summ, 
                                          'lang':lang
                                       })