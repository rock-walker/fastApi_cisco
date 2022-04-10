from fastapi import Query
from pydantic import BaseModel


class Target(BaseModel):
    url: str = Query(..., title="ping provided query", min_length=3, max_length=100)
