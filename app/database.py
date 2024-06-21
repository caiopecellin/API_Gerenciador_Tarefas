from pathlib import Path
from typing import Generator

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base, Session

class Config:

    @staticmethod
    def get_database_url():
        #Retorna String do Banco de dados
        return f'sqlite:///{Config.get_project_root()}/tarefas.db'

    @staticmethod
    def get_project_root():
        #Retorna o Diretorio do banco de dados
        return Path(__file__).parent.parent

#cria a engine
engine = create_engine(Config.get_database_url(), echo=False,
                       connect_args={'check_same_thread': False})

#cria a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Funçao para criar sessao
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
