### Api Gerenciador de Tarefas
* Criado por: Caio Pecellin Costa

## Estrutura do Projeto

Sugestão de estrutura de diretórios:

```
fastapi-task-management/
├── app/
│   ├── controllers/
│   │   └── task_controller.py
│   ├── services/
│   │   └── task_service.py
│   ├── repositories/
│   │   └── task_repository.py
│   ├── models/
│   │   └── task_model.py
│   ├── main.py
│   └── database.py
└── tests/
    ├── test_controllers.py
    ├── test_services.py
    └── test_repositories.py
```

### Descrição dos Componentes

- **Controllers**: Responsáveis por definir os endpoints da API.
- **Services**: Contêm a lógica de negócios e validações.
- **Repositories**: Gerenciam a interação com o banco de dados.

### 1. Modelagem de Dados

Crie um modelo para representar uma tarefa com os seguintes campos:

- `id` (integer, primary key)
- `titulo` (string)
- `descricao` (string)
- `status` (string, pode ser "Pendente", "Em Progresso", "Concluída")
- `criado_em` (datetime)

### 2. Repositório de Tarefas

Implemente a camada de repositório para realizar operações CRUD:

- Criar uma nova tarefa
- Obter uma tarefa pelo ID
- Atualizar uma tarefa
- Deletar uma tarefa
- Listar todas as tarefas

### 3. Serviço de Tarefas

Implemente a camada de serviço para validar os dados e aplicar a lógica de negócios:

- Criar uma nova tarefa
- Obter uma tarefa pelo ID
- Atualizar uma tarefa
- Deletar uma tarefa
- Listar todas as tarefas

### 4. Controlador de Tarefas

Implemente os endpoints da API utilizando FastAPI:

- `POST /tasks/`: Criar uma nova tarefa.
- `GET /tasks/`: Listar todas as tarefas.
- `GET /tasks/{task_id}`: Obter detalhes de uma tarefa específica por ID.
- `PUT /tasks/{task_id}`: Atualizar uma tarefa específica por ID.
- `DELETE /tasks/{task_id}`: Deletar uma tarefa específica por ID.

### 5. Testes Unitários

Escreva testes unitários para os serviços e controladores da aplicação.