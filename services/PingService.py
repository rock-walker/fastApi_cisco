from fastapi import HTTPException

from controllers.models.ping import Target
from shared.httpRequestMixin import HttpRequestMixin


class PingService(HttpRequestMixin):
    async def ping(self, target: Target) -> str:

        if target.url is None:
            raise HTTPException(status_code=404, detail="Provide URL for ping")

        try:
            response = await self.request_url(target.url)
            # log response
            return response
        except Exception as ex:  # it's too broad exception, but for sake of time space
            raise HTTPException(status_code=500, detail=f"Custom 500 error has been intercepted. Msg: {ex}")
