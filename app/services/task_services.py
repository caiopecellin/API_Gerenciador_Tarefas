from sqlalchemy.orm import Session
from models.task_model import Task
from repositories.task_repositories import task_repository


class task_service:
    #services de criar task
    def create_task(db: Session, titulo: str, descricao: str, status: str):
        task = Task(titulo=titulo, descricao=descricao, status=status)
        return task_repository.create_task(db, task)

    #services de puxar 1 task
    def get_task(db: Session, task_id: int):
        return task_repository.get_task(db, task_id)
    
    #services de 1 ou mais task
    def get_tasks(db: Session, skip: int = 0, limit: int = 10):
        return task_repository.get_tasks(db, skip, limit)

    #services de atualizar task
    def update_task(db: Session, task_id: int, titulo: str = None, descricao: str = None, status: str = None):
        task_data = {k: v for k, v in {"titulo": titulo, "descricao": descricao, "status": status}.items() if v is not None}
        return task_repository.update_task(db, task_id, task_data)

    #services de deletar task
    def delete_task(db: Session, task_id: int):
        return task_repository.delete_task(db, task_id)
