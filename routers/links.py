from fastapi import APIRouter

router = APIRouter(
    prefix="/v1",
)


@router.post("/links")
async def create_link():
    pass
