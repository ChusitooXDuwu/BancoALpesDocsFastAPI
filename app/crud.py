from .database import document_collection, document_helper
from .schemas import DocumentoCreate, Documento
from bson.objectid import ObjectId
from datetime import datetime
from typing import List

async def get_document_by_id(id: str) -> dict:
    document = await document_collection.find_one({"_id": ObjectId(id)})
    if document:
        return document_helper(document)

async def get_all_documents(skip: int = 0, limit: int = 10) -> List[dict]:
    documents = []
    async for document in document_collection.find().skip(skip).limit(limit):
        documents.append(document_helper(document))
    return documents

async def create_new_document(document: DocumentoCreate) -> dict:
    document_dict = document.dict()
    document_dict["fecha_subida"] = datetime.utcnow()
    try:
        new_document = await document_collection.insert_one(document_dict)
        created_document = await document_collection.find_one({"_id": new_document.inserted_id})
        return document_helper(created_document)
    except Exception as e:
        print(f"Error creating document: {e}")
        raise

async def delete_all_documents() -> int:
    result = await document_collection.delete_many({})
    return result.deleted_count

async def delete_document_by_id(id: str) -> bool:
    result = await document_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
