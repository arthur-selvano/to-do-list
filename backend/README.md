# To-Do List Backend

Backend da aplicação To-Do List, construído com **Python** e **FastAPI**, utilizando **SQLite** como banco de dados.

## Funcionalidades
- Criar, listar, atualizar e deletar tarefas (CRUD)
- Persistência de dados em SQLite

## 1. Como rodar

Crie um ambiente virtual** (recomendado):

```
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```
## 2. Instale as dependências:
```
pip install -r requirements.txt
```
## 3. Rode o servidor:
```
uvicorn main:app --reload
```
## 4. Documentação automática da API:
```
http://127.0.0.1:8000/docs
```

## Tecnologias

```
Python 3.x
FastAPI
SQLite
Uvicorn (servidor ASGI)
```

