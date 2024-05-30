from fastapi import APIRouter, HTTPException, Depends
from ..crud import get_document_by_id, get_all_documents, create_new_document, delete_all_documents, delete_document_by_id
from ..schemas import Documento, DocumentoCreate
from typing import List
import requests

router = APIRouter()

@router.get("/documentos/", response_model=List[Documento])
async def read_all_documents(skip: int = 0, limit: int = 10):
    documents = await get_all_documents(skip=skip, limit=limit)
    return documents

@router.get("/documentos/{documento_id}", response_model=Documento)
async def read_document_by_id(documento_id: str):
    document = await get_document_by_id(documento_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Documento not found")
    return document

@router.post("/documentos/", response_model=Documento)
async def create_new_document_endpoint(documento: DocumentoCreate):
    # try:
    #     return await create_new_document(documento)
    # except Exception as e:
    #     print(f"Error creating document: {e}")
    #     raise HTTPException(status_code=500, detail=str(e))
    
    try:
        response = requests.get(f"{CLIENTE_API_URL}{documento.cliente_id}/")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Cliente not found")
        return await create_new_document(documento)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/documentos/{documento_id}", response_model=dict)
async def delete_document_by_id_endpoint(documento_id: str):
    if not await delete_document_by_id(documento_id):
        raise HTTPException(status_code=404, detail="Documento not found")
    return {"detail": "Documento deleted"}

@router.delete("/documentos/", response_model=dict)
async def delete_all_documents_endpoint():
    count = await delete_all_documents()
    return {"detail": f"{count} documentos deleted"}
