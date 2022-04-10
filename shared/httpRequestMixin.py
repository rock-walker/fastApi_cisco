import asyncio
import httpx as httpx


class HttpRequestMixin:
    async def http(self, client, url: str):
        response = await client.get(url)
        return response.text

    async def request_url(self, url: str):
        async with httpx.AsyncClient() as client:
            task = self.http(client, url)
            return await asyncio.gather(task)
