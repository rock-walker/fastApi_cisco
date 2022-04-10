from fastapi import FastAPI
from controllers import info, ping

app = FastAPI()

app.include_router(info.router)
app.include_router(ping.router)
