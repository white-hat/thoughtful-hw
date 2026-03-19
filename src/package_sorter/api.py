from importlib.resources import files

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.templating import Jinja2Templates

from package_sorter.sorting import sort

app = FastAPI(title="Package Sorter")
app.mount(
    "/static", StaticFiles(directory=str(files("package_sorter").joinpath("static"))), name="static"
)

templates = Jinja2Templates(directory=str(files("package_sorter").joinpath("templates")))


class SortRequest(BaseModel):
    width: float
    height: float
    length: float
    mass: float


class SortResponse(BaseModel):
    stack: str


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    template = templates.get_template("index.html")
    return HTMLResponse(content=template.render())


@app.post("/sort", response_model=SortResponse)
async def sort_package(request: SortRequest) -> SortResponse:
    try:
        stack = sort(
            width=request.width,
            height=request.height,
            length=request.length,
            mass=request.mass,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return SortResponse(stack=stack)
