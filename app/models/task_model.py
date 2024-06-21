from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from database import Base, engine

Base = declarative_base()

#Cria Modelo
class Task(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String, index=True)
    status = Column(String, index=True)
    criado_em = Column(DateTime, default=datetime.utcnow)


#Apaga e recria modelo toda vez que iniciar a aplicação
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
