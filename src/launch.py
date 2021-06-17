from fastapi import FastAPI
from route.user import router

app = FastAPI()

app.include_router(router)
