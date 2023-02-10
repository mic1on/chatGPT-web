import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from model import Message
from api import completions as api_completions

app = FastAPI()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, 'dist')
ASSETS_DIR = os.path.join(DIST_DIR, 'assets')
app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")
templates = Jinja2Templates(directory=DIST_DIR)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root():
    return templates.TemplateResponse("index.html", {"request": {}})


@app.post("/completions")
async def completions(message: Message):
    res = await api_completions(message)
    return res


if __name__ == '__main__':
    import os
    if key := os.environ.get('API_KEY'):
        if not key.startswith('sk-'):
            raise ValueError('API_KEY must start with "sk-"')
    else:
        raise ValueError('API_KEY not found in environment variables')

    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000)
