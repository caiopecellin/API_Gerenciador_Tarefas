import pytest
from unittest.mock import Mock, MagicMock
from sqlalchemy.orm import Session
from services.task_services import task_service
from models.task_model import Task
from repositories.task_repositories import task_repository

@pytest.fixture
def mock_task_repository():
    return Mock(spec=task_repository)

#testa a função service create task
def test_create_task(mock_task_repository):
    db = Mock(spec=Session)
    task_data = {"titulo": "New Task", "descricao": "Task Description", "status": "Pendente"}
    task_instance = Task(id=1, **task_data)
    mock_task_repository.create_task.return_value = task_instance

    task_service.task_repository = mock_task_repository
    task = task_service.create_task(db, **task_data)

    assert task.titulo == "New Task"

#testa a função service get task, usa o magic mock para fazer a requisição da forma correta, por JSON 
def test_get_task(mock_task_repository):
    db = Mock(spec=Session)
    task_instance = Task(id=1, titulo="New Task", descricao="Task Description", status="Pendente")  
    
    mock_query = MagicMock()
    mock_query.filter.return_value.first.return_value = task_instance
    db.query.return_value = mock_query
    
    task_service.task_repository = mock_task_repository
    task = task_service.get_task(db, 1)
    print(task.titulo)

    assert task.titulo == "New Task"

#testa a função service get tasks, usa o magic mock para fazer a requisição da forma correta, por JSON 
def test_get_tasks(mock_task_repository):
    db = Mock(spec=Session)
    task_instance_list = [Task(id=1, titulo="New Task", descricao="Task Description 1", status="Pendente"),
                          Task(id=2, titulo="New Task 2", descricao="Task Description 2", status="Concluída")]
    
    # Mock SQLAlchemy query behavior
    mock_query = MagicMock()
    mock_query.offset.return_value.limit.return_value.all.return_value = task_instance_list
    db.query.return_value = mock_query
    
    task_service.task_repository = mock_task_repository
    tasks = task_service.get_tasks(db, 0, 10)

    assert len(tasks) == 2
    assert tasks[0].titulo == "New Task"
    assert tasks[1].titulo == "New Task 2"

#testa a função service update task
def test_update_task(mock_task_repository):
    db = Mock(spec=Session)
    updated_task_data = {"titulo": "Updated Task", "descricao": "Updated Description", "status": "Concluída"}
    mock_task_repository.update_task.return_value = Task(id=1, **updated_task_data)

    task_service.task_repository = mock_task_repository
    task = task_service.update_task(db, 1, **updated_task_data)

    assert task.titulo == "Updated Task"
    assert task.descricao == "Updated Description"
    assert task.status == "Concluída"

#testa a função service delete task, usa o magic mock para fazer a requisição da forma correta, por JSON 
def test_delete_task(mock_task_repository):
    db = Mock(spec=Session)
    task_instance = Task(id=1, titulo="Updated Task", descricao="Updated Description", status="Concluída")
    
    # Mock SQLAlchemy query behavior
    mock_query = MagicMock()
    mock_query.filter.return_value.first.return_value = task_instance
    db.query.return_value = mock_query
    
    task_service.task_repository = mock_task_repository
    result = task_service.delete_task(db, 1)

    assert result.titulo == "Updated Task"
