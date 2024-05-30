from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

class Documento(Base):
    __tablename__ = 'documentos'

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    tipo = Column(String, index=True)
    fecha_subida = Column(DateTime, default=datetime.datetime.utcnow)
    estado = Column(String, index=True)
    archivo = Column(String, index=True)
    score_confiabilidad = Column(Float, default=0.0)

    cliente = relationship("Cliente")
