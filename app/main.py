from fastapi import FastAPI
from .routers import documents
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#:)

# @app.get("/health")
# async def health_check():
#     return {"status": "ok"}

app.include_router(documents.router, prefix="/api")
