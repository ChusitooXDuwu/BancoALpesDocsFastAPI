# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://monitoring_user:isis2503@34.28.60.253:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.mydatabase

document_collection = database.get_collection("documents_collection")

def document_helper(document) -> dict:
    return {
        "id": str(document["_id"]),
        "cliente_id": document["cliente_id"],
        "tipo": document["tipo"],
        "estado": document["estado"],
        "archivo": document["archivo"],
        "score_confiabilidad": document["score_confiabilidad"],
        "fecha_subida": document["fecha_subida"]
    }
