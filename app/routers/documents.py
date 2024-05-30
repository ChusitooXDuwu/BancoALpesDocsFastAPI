from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/documentos/", response_model=list[schemas.Documento])
def read_documentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    documentos = crud.get_documentos(db, skip=skip, limit=limit)
    return documentos

@router.get("/documentos/{documento_id}", response_model=schemas.Documento)
def read_documento(documento_id: int, db: Session = Depends(get_db)):
    db_documento = crud.get_documento(db, documento_id=documento_id)
    if db_documento is None:
        raise HTTPException(status_code=404, detail="Documento not found")
    return db_documento

@router.post("/documentos/", response_model=schemas.Documento)
def create_documento(documento: schemas.DocumentoCreate, db: Session = Depends(get_db)):
    return crud.create_documento(db=db, documento=documento)

@router.delete("/documentos/{documento_id}", response_model=schemas.Documento)
def delete_documento(documento_id: int, db: Session = Depends(get_db)):
    if not crud.delete_documento(db, documento_id=documento_id):
        raise HTTPException(status_code=404, detail="Documento not found")
    return {"detail": "Documento deleted"}

@router.delete("/documentos/", response_model=dict)
def delete_all_documentos(db: Session = Depends(get_db)):
    crud.delete_all_documentos(db)
    return {"detail": "All documentos deleted"}
