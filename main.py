from fastapi import FastAPI

app = FastAPI()


@app.post("/long_url")
async def long_url():
    return ...

@app.get("/short_url")
async def short_url():
    return ...

@app.get("/{slug}")
async def redirect_to_url(slug: str):
    return ...