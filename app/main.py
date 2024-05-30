from fastapi import FastAPI
from .database import engine, Base
from .routers import documents

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(documents.router, prefix="/api")
