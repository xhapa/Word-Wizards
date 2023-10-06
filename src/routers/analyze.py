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
    id_data = request.cookies.get("id_data")
    if id_data == 'None':
        await NLPDataService(db).create_nlp_data(text=text)
        last_data = NLPDataService(db).get_last_nlp_data()
        nlp_id = last_data.nlp_data_id
        lang = last_data.lang   
    else:
        # Handle the case where id_data is an integer
        try:
            nlp_data = NLPDataService(db).get_by_id_nlp_data(int(id_data))
            lang = nlp_data.lang
            nlp_id = nlp_data.nlp_data_id
        except ValueError:
            # Handle the case where id_data is not a valid integer
            # You may want to log or handle this error appropriately
            lang = "default_lang"
            nlp_id = None

    # Convert None to a default value (e.g., an empty string)
    nlp_id = nlp_id or ""

    return templates.TemplateResponse('analyze_menu.html', {'request': request, 'lang': lang, 'nlp_id': nlp_id})

@analyze_route.get('/words-count/{nlp_data_id}', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def words_count(
    nlp_data_id : int,
    request: Request,
    db : Session 
        = Depends(get_session)
)-> Jinja2Templates:
    nlp_data = NLPDataService(db).get_by_id_nlp_data(int(nlp_data_id))
    lang = nlp_data.lang
    nlp_id = nlp_data.nlp_data_id
    count = nlp_data.word_count
    return templates.TemplateResponse('./content/words_count_page.html',
                                      {
                                        'request': request,
                                        'count':count,
                                        'lang':lang,
                                        'nlp_id': nlp_id
                                        })

@analyze_route.get('/entities/{nlp_data_id}', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def entities(
    nlp_data_id : int,
    request: Request,
    db : Session
        = Depends(get_session)
)-> Jinja2Templates:
    nlp_data = NLPDataService(db).get_by_id_nlp_data(int(nlp_data_id))
    nlp_id = nlp_data.nlp_data_id
    ent = nlp_data.entities
    lang = nlp_data.lang
    return templates.TemplateResponse('./content/entities_page.html', 
                                      {
                                        'request': request, 
                                        'entities':ent, 
                                        'lang':lang,
                                        'nlp_id': nlp_id
                                        })

@analyze_route.get('/keywords/{nlp_data_id}', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def keywords(
    nlp_data_id : int,
    request: Request,
    db : Session
        = Depends(get_session)
)-> Jinja2Templates:
    nlp_data = NLPDataService(db).get_by_id_nlp_data(int(nlp_data_id))
    nlp_id = nlp_data.nlp_data_id
    key = nlp_data.keywords
    lang = nlp_data.lang
    return templates.TemplateResponse('./content/keywords_page.html', 
                                      {
                                          'request': request, 
                                          'keywords':key, 
                                          'lang':lang,
                                          'nlp_id': nlp_id
                                          })

@analyze_route.get('/summary/{nlp_data_id}', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def summarize(
    nlp_data_id : int,
    request: Request,
    db : Session 
        = Depends(get_session)
)-> Jinja2Templates:
    nlp_data = NLPDataService(db).get_by_id_nlp_data(int(nlp_data_id))
    nlp_id = nlp_data.nlp_data_id
    summ = nlp_data.summary
    lang = nlp_data.lang
    return templates.TemplateResponse('./content/summary_page.html', 
                                      {
                                          'request': request, 
                                          'summary':summ, 
                                          'lang':lang,
                                          'nlp_id': nlp_id
                                       })