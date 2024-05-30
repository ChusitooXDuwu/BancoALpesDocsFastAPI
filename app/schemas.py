from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentoBase(BaseModel):
    cliente_id: int
    tipo: str
    estado: str
    archivo: str
    score_confiabilidad: float

class DocumentoCreate(DocumentoBase):
    pass

class Documento(DocumentoBase):
    id: Optional[str]
    fecha_subida: datetime

    class Config:
        orm_mode = True
