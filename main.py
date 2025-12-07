from fastapi import FastAPI

from routers import links

app = FastAPI()

app.include_router(links.router)


@app.get("/{slug}")
async def redirect(slug: str):
    pass
