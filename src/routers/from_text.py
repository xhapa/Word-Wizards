# Python
from typing import Annotated

# FastAPI
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

text_router = APIRouter(prefix='/text', tags=['Text'])

# Static
text_router.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

@text_router.get('/', response_class=HTMLResponse, response_model=None, status_code=200,)
async def from_text(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('from_text.html', {'request': request})

@text_router.post('/analyze', response_class=HTMLResponse, response_model=None, status_code=200,)
async def analyze_it(
    request: Request,
    text : Annotated[
        str, 
        Form(
            title= 'Text',
            description='Text to nlp analysis'
        )
    ] = None
)-> Jinja2Templates:
    return templates.TemplateResponse('analyze_menu.html', {'request': request})