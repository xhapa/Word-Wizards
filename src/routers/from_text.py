# Python
from typing import Annotated

# FastAPI
from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Config
from config.db import engine, Session, get_session

# Services
from services.nlp_data import NLPDataService

#SQLModels
from sqlmodels.nlp_data import NLPData

from .analyze import analyze_route

text_router = APIRouter(prefix='/text', tags=['Text'])

# Static
text_router.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

@text_router.get('/', response_class=HTMLResponse, response_model=None, status_code=200)
async def from_text(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('from_text.html', {'request': request})

@text_router.post('/submit', response_class=HTMLResponse, response_model=NLPData, status_code=200,)
async def submit(
    textarea : Annotated[
        str, 
        Form(
            title= 'Text',
            description='Text to nlp analysis'
        )
    ] = None
)-> Jinja2Templates:
    url = analyze_route.url_path_for('analyze_it')
    response = RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="text_data", value=textarea.encode("utf-8"))
    response.set_cookie(key="id_data", value=None)
    return response