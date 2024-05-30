from fastapi import APIRouter, HTTPException, Depends
from ..crud import get_documento, get_documentos, create_documento, delete_all_documentos, delete_documento
from ..schemas import Documento, DocumentoCreate
from typing import List

router = APIRouter()

@router.get("/documentos/", response_model=List[Documento])
async def read_documentos(skip: int = 0, limit: int = 10):
    documentos = await get_documentos(skip=skip, limit=limit)
    return documentos

@router.get("/documentos/{documento_id}", response_model=Documento)
async def read_documento(documento_id: str):
    documento = await get_documento(documento_id)
    if documento is None:
        raise HTTPException(status_code=404, detail="Documento not found")
    return documento

@router.post("/documentos/", response_model=Documento)
async def create_documento(documento: DocumentoCreate):
    return await create_documento(documento)

@router.delete("/documentos/{documento_id}", response_model=dict)
async def delete_documento(documento_id: str):
    if not await delete_documento(documento_id):
        raise HTTPException(status_code=404, detail="Documento not found")
    return {"detail": "Documento deleted"}

@router.delete("/documentos/", response_model=dict)
async def delete_all_documentos():
    count = await delete_all_documentos()
    return {"detail": f"{count} documentos deleted"}
