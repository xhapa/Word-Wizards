# FastAPI
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

text_router = APIRouter(prefix='/text', tags=['Tetx'])

# Static
text_router.mount("/assets", StaticFiles(directory="../assets"), name="assets")
templates = Jinja2Templates(directory='../templates')

@text_router.get('/', response_class=HTMLResponse, response_model=None, status_code=200,)
async def from_text(request: Request):
    return templates.TemplateResponse('from_text.html', {'request': request})