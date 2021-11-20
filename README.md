# API Lista de Tarefas
API desenvolvida com o propositor de Agenda utilizando [Django Rest](https://www.django-rest-framework.org/) que permite ao usuário inserir, consultar e deletar tarefas que são armazenadas em um banco de dados [MySQL](https://www.mysql.com/).

## Tecnologia requerida

- Python 3.7
- Django 2.1.15
- Django Rest Framework 3.11.0
- PyMySQL 0.9.3
- django-cors-headers 3.2.1

Usando o [Postman](https://www.postman.com/) para testar as APIs, onde todas as ações realizadas são salvas no banco de dados MySQL.

### Metodo POST
- Criando uma nova tarefa usando POST
<div align="center">
	<img src="./github/post.png" alt="Metodo POST" height="auto">
</div>

### Metodo GET
- Recuperando todas as tarefas usando GET
<div align="center">
	<img src="./github/get.png" alt="Metodo GET" height="auto">
</div>

- Recuperando uma única tarefa por id usando GET
<div align="center">
	<img src="./github/get_id.png" alt="Metodo GET" height="auto">
</div>

### Metodo PUT
- Atualizando uma tarefa usando PUT
<div align="center">
	<img src="./github/put.png" alt="Metodo PUT" height="auto">
</div>

### Metodo DELETE
- Excluindo uma tarefa usando DELETE
<div align="center">
	<img src="./github/delete.png" alt="Metodo DELETE" height="auto">
</div>


