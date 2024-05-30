from .database import document_collection, document_helper
from .schemas import DocumentoCreate, Documento
from bson.objectid import ObjectId
from datetime import datetime
from typing import List

async def get_documento(id: str) -> dict:
    document = await document_collection.find_one({"_id": ObjectId(id)})
    if document:
        return document_helper(document)

async def get_documentos(skip: int = 0, limit: int = 10) -> List[dict]:
    documents = []
    async for document in document_collection.find().skip(skip).limit(limit):
        documents.append(document_helper(document))
    return documents

async def create_documento(document: DocumentoCreate) -> dict:
    document_dict = document.dict()
    document_dict["fecha_subida"] = datetime.utcnow()
    new_document = await document_collection.insert_one(document_dict)
    created_document = await document_collection.find_one({"_id": new_document.inserted_id})
    return document_helper(created_document)

async def delete_all_documentos() -> int:
    result = await document_collection.delete_many({})
    return result.deleted_count

async def delete_documento(id: str) -> bool:
    result = await document_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
