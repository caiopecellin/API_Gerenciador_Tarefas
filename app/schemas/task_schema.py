from pydantic import BaseModel, Field
from typing import Literal

class TaskCreate(BaseModel):
    titulo: str
    descricao: str
    #Aqui define status como uma dessas 3 opções
    status: Literal["Pendente", "Em Progresso", "Concluída"]


#Não tem preenchimento obrigatório
class TaskUpdate(BaseModel):
    titulo: str = None
    descricao: str = None
    #Aqui define status como uma dessas 3 opções, mas nao com preenchimento obrigatorio
    status: Literal["Pendente", "Em Progresso", "Concluída"] = None
