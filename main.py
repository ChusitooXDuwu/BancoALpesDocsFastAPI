from typing import List, Optional, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Cliente(BaseModel):
    id: int
    nombre: str

class Documento(BaseModel):
    id: Optional[int] = None
    cliente_id: int
    tipo: str
    fecha_subida: Optional[datetime] = None
    estado: str
    archivo: str
    score_confiabilidad: float = 0.0

# Datos de ejemplo
clientes = [
    {"id": 1, "nombre": "Cliente 1"},
    {"id": 2, "nombre": "Cliente 2"},
]

documentos = [
    {
        "id": 1,
        "cliente_id": 1,
        "tipo": "cedula",
        "fecha_subida": datetime.now(),
        "estado": "pendiente",
        "archivo": "archivo1.pdf",
        "score_confiabilidad": 0.75,
    },
    {
        "id": 2,
        "cliente_id": 2,
        "tipo": "pasaporte",
        "fecha_subida": datetime.now(),
        "estado": "confirmado",
        "archivo": "archivo2.pdf",
        "score_confiabilidad": 0.85,
    },
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/documentos/", response_model=List[Documento])
def read_documentos():
    return documentos

@app.get("/documentos/{documento_id}", response_model=Documento)
def read_documento(documento_id: int):
    for doc in documentos:
        if doc["id"] == documento_id:
            return doc
    raise HTTPException(status_code=404, detail="Documento not found")

@app.post("/documentos/", response_model=Documento)
def create_documento(documento: Documento):
    documento.id = len(documentos) + 1
    documento.fecha_subida = datetime.now()
    documentos.append(documento.dict())
    return documento

@app.put("/documentos/{documento_id}", response_model=Documento)
def update_documento(documento_id: int, updated_documento: Documento):
    for idx, doc in enumerate(documentos):
        if doc["id"] == documento_id:
            updated_documento.id = documento_id
            updated_documento.fecha_subida = doc["fecha_subida"]
            documentos[idx] = updated_documento.dict()
            return updated_documento
    raise HTTPException(status_code=404, detail="Documento not found")

@app.delete("/documentos/{documento_id}", response_model=Documento)
def delete_documento(documento_id: int):
    for idx, doc in enumerate(documentos):
        if doc["id"] == documento_id:
            removed_doc = documentos.pop(idx)
            return removed_doc
    raise HTTPException(status_code=404, detail="Documento not found")
