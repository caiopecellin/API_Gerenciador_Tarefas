from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.task_services import task_service
from database import get_db
from schemas.task_schema import TaskCreate, TaskUpdate

router = APIRouter()
#controller e router de criar task
@router.post("/tasks/", response_model=TaskCreate)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, **task.dict())

#controller e router de puxar tasks
@router.get("/tasks/")
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return task_service.get_tasks(db, skip, limit)

#controller e router de puxar 1 task
@router.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada...")
    return task

#controller e router de update task
@router.put("/tasks/{task_id}", response_model=TaskUpdate)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = task_service.update_task(db, task_id, **task.dict(exclude_unset=True))
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada...")
    return updated_task

#controller e router de deletar task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_service.delete_task(db, task_id)
    return {"detail": "Tarefa excluída!"}
