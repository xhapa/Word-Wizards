# FastAPI
from fastapi import APIRouter, Request
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