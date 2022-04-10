from fastapi import APIRouter

from controllers.models.ping import Target
from services.PingService import PingService

router = APIRouter(
    prefix="/ping",
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def ping_url(url: Target):
    return await PingService().ping(url)
