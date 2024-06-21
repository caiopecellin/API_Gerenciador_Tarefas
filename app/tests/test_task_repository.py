import pytest
from sqlalchemy.orm import Session
from unittest.mock import Mock
from repositories.task_repositories import task_repository
from models.task_model import Task

@pytest.fixture
def db():
    return Mock(spec=Session)

#testa a função repository create task
def test_create_task(db):
    task_data = Task(titulo="New Task", descricao="Task Description", status="Pendente")
    db.add.return_value = None
    db.commit.return_value = None
    db.refresh.return_value = task_data

    task = task_repository.create_task(db, task_data)

    assert task.titulo == "New Task"
    db.add.assert_called_once_with(task_data)
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(task_data)

#testa a função repository get task
def test_get_task(db):
    task_data = Task(id=1, titulo="Task 1", descricao="Description 1", status="Pendente")
    db.query.return_value.filter.return_value.first.return_value = task_data

    task = task_repository.get_task(db, 1)

    assert task.titulo == "Task 1"
    db.query.return_value.filter.return_value.first.assert_called_once()

#testa a função repository get tasks
def test_get_tasks(db):
    task_data = [Task(id=1, titulo="Task 1", descricao="Description 1", status="Pendente")]
    db.query.return_value.offset.return_value.limit.return_value.all.return_value = task_data

    tasks = task_repository.get_tasks(db)

    assert len(tasks) == 1
    assert tasks[0].titulo == "Task 1"
    db.query.return_value.offset.return_value.limit.return_value.all.assert_called_once()

#testa a função repository update
def test_update_task(db):
    task_data = Task(id=1, titulo="Task 1", descricao="Description 1", status="Pendente")
    updated_data = {"titulo": "Updated Task", "descricao": "Updated Description", "status": "Concluída"}
    db.query.return_value.filter.return_value.first.return_value = task_data

    task = task_repository.update_task(db, 1, updated_data)

    assert task.titulo == "Updated Task"
    db.commit.assert_called_once()
    db.refresh.assert_called_once_with(task_data)

#testa a função repository delete
def test_delete_task(db):
    task_data = Task(id=1, titulo="Updated Task", descricao="Updated Description", status="Concluída")
    db.query.return_value.filter.return_value.first.return_value = task_data

    task = task_repository.delete_task(db, 1)
    print(task.titulo)
    assert task.titulo == "Updated Task"
    db.delete.assert_called_once_with(task_data)
    db.commit.assert_called_once()
