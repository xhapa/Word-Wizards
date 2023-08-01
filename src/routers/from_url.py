# Python
from typing import Annotated

# FastAPI
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

url_router = APIRouter(prefix='/url', tags=['URL'])
# Static
url_router.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

@url_router.get('/', response_class=HTMLResponse, response_model=None, status_code=200,)
async def from_url(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('from_url.html', {'request': request})

@url_router.post('/analyze', response_class=HTMLResponse, response_model=None, status_code=200,)
async def analyze_it(
    request: Request,
    url : Annotated[
        str, 
        Form(
            title= 'URL',
            description='Url to nlp analysis'
        )
    ] = None
)-> Jinja2Templates:
    return templates.TemplateResponse('analyze_menu.html', {'request': request})