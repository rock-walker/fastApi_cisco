from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from controllers.models.info import Info

router = APIRouter(
    prefix="/info",
    responses={404: {"description": "Not found"}},
)

DEFAULT_VALUE = "Cisco is the best!"


@router.get("/")
def get_info():
    info = Info(
        Receiver=DEFAULT_VALUE
    )

    result = jsonable_encoder(info)
    return JSONResponse(content=result)
