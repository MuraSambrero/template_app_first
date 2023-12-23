from fastapi import FastAPI, status
from routes.index_router import index_router

app = FastAPI()
app.include_router(index_router, tags=['Index'], prefix='/api')