# FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

file_router = APIRouter(prefix='/file', tags=['File'])

# Static
file_router.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

@file_router.get('/', response_class=HTMLResponse, response_model=None, status_code=200,)
async def from_file(request: Request)-> Jinja2Templates:
    return templates.TemplateResponse('from_file.html', {'request': request})