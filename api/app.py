import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import api
from model import Message, MessageTurbo

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, 'dist')
ASSETS_DIR = os.path.join(DIST_DIR, 'assets')
app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")
templates = Jinja2Templates(directory=DIST_DIR)


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        return JSONResponse(content={"code": 500, "error": {"message": f"{type(exc)} {exc}"}})


app.middleware('http')(catch_exceptions_middleware)

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
async def completions(request: Request, message: Message):
    api_key = request.headers.get('api_key')
    res = await api.completions(message, api_key=api_key)
    return res


@app.post("/completions_turbo")
async def completions(request: Request, message: MessageTurbo):
    api_key = request.headers.get('api_key')
    res = await api.completions_turbo(message, api_key=api_key)
    return res


@app.get("/credit_summary")
async def credit_summary(request: Request):
    api_key = request.headers.get('api_key')
    res = await api.credit_summary(api_key=api_key)
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000)
