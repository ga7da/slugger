from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

from routers import links

app = FastAPI()

app.include_router(links.router)


@app.get("/{slug}")
async def redirect(slug: str):
    return RedirectResponse(url=..., status_code=status.HTTP_302_FOUND)
