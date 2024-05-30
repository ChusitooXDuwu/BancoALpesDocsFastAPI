from typing import List
from fastapi import APIRouter, HTTPException
from ..crud import create_new_document, get_all_documents, get_document_by_id, delete_document_by_id, delete_all_documents
from ..schemas import Documento, DocumentoCreate
import requests

router = APIRouter()

CLIENTE_API_URL = "http://34.170.157.181:8080/cliente/"

@router.post("/documentos/", response_model=Documento)
async def create_documento(documento: DocumentoCreate):
    try:
        response = requests.get(f"{CLIENTE_API_URL}{documento.cliente_id}")
        print(f"{CLIENTE_API_URL}{documento.cliente_id}/")
        print(response)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Cliente not found")
        cliente_data = response.json()
        if not cliente_data:
            raise HTTPException(status_code=404, detail="Cliente not found")
        return await create_new_document(documento)
    except Exception as e:
        print(f"Error creating document: {e}")
        raise HTTPException(status_code=500, detail=str(e))

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

#create health 
@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.delete("/documentos/{documento_id}", response_model=dict)
async def delete_document_by_id_endpoint(documento_id: str):
    if not await delete_document_by_id(documento_id):
        raise HTTPException(status_code=404, detail="Documento not found")
    return {"detail": "Documento deleted"}

@router.delete("/documentos/", response_model=dict)
async def delete_all_documents_endpoint():
    count = await delete_all_documents()
    return {"detail": f"{count} documentos deleted"}
