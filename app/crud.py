from sqlalchemy.orm import Session
from . import models, schemas

def get_documento(db: Session, documento_id: int):
    return db.query(models.Documento).filter(models.Documento.id == documento_id).first()

def get_documentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Documento).offset(skip).limit(limit).all()

def create_documento(db: Session, documento: schemas.DocumentoCreate):
    db_documento = models.Documento(**documento.dict())
    db.add(db_documento)
    db.commit()
    db.refresh(db_documento)
    return db_documento

def delete_all_documentos(db: Session):
    db.query(models.Documento).delete()
    db.commit()

def delete_documento(db: Session, documento_id: int):
    db_documento = db.query(models.Documento).filter(models.Documento.id == documento_id).first()
    if db_documento:
        db.delete(db_documento)
        db.commit()
        return True
    return False
