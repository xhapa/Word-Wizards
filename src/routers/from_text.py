# Python
from typing import Annotated

# FastAPI
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Config
from config.db import engine, Session

# Services
from services.nlp_data import NLPDataService

#SQLModels
from sqlmodels.nlp_data import NLPData

text_router = APIRouter(prefix='/text', tags=['Text'])

# Static
text_router.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

@text_router.get('/', response_class=HTMLResponse, response_model=None, status_code=200,)
async def from_text(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('from_text.html', {'request': request})

@text_router.post('/analyze', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def analyze_it(
    request: Request,
    textarea : Annotated[
        str, 
        Form(
            title= 'Text',
            description='Text to nlp analysis'
        )
    ] = None
)-> Jinja2Templates:
    db = Session(engine)
    await NLPDataService(db).create_nlp_data(text=textarea)
    lang = NLPDataService(db).get_last_nlp_data().lang
    return templates.TemplateResponse('analyze_menu.html', {'request': request, 'lang':lang})

@text_router.get('/analyze/words-count', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def words_count(
    request: Request,
)-> Jinja2Templates:
    db = Session(engine)
    last_data = NLPDataService(db).get_last_nlp_data()
    count = last_data.word_count
    lang = last_data.lang
    return templates.TemplateResponse('./content/words_count_page.html',
                                      {
                                        'request': request,
                                        'count':count,
                                        'lang':lang
                                        })

@text_router.get('/analyze/entities', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def entities(
    request: Request,
)-> Jinja2Templates:
    db = Session(engine)
    last_data = NLPDataService(db).get_last_nlp_data()
    ent = last_data.entities
    lang = last_data.lang
    return templates.TemplateResponse('./content/entities_page.html', 
                                      {
                                        'request': request, 
                                        'entities':ent, 
                                        'lang':lang
                                        })

@text_router.get('/analyze/keywords', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def keywords(
    request: Request,
)-> Jinja2Templates:
    db = Session(engine)
    last_data = NLPDataService(db).get_last_nlp_data()
    key = last_data.keywords
    lang = last_data.lang
    return templates.TemplateResponse('./content/keywords_page.html', 
                                      {
                                          'request': request, 
                                          'keywords':key, 
                                          'lang':lang
                                          })

@text_router.get('/analyze/summary', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def summarize(
    request: Request,
)-> Jinja2Templates:
    db = Session(engine)
    last_data = NLPDataService(db).get_last_nlp_data()
    summ = last_data.summary
    lang = last_data.lang
    return templates.TemplateResponse('./content/summary_page.html', 
                                      {
                                          'request': request, 
                                          'summary':summ, 
                                          'lang':lang
                                       })