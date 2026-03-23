# Full Stack To-Do List (React + Python)

Projeto desenvolvido para colocar em prática conceitos de integração entre Front-end (React com Vite) e Back-end (FastAPI com Python), utilizando SQLite para persistência de dados.

## 🛠️ Tecnologias Utilizadas

- **Front-end:** React, Vite, CSS3 (Custom Properties).
- **Back-end:** Python 3, FastAPI, Uvicorn.
- **Banco de Dados:** SQLite (CRUD Completo).

## 🚀 Como executar o projeto

### 1. Back-end
```bash
cd backend
python -m venv venv
# Ativar venv: .\venv\Scripts\Activate (Windows) ou source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
### 2. Front-end

```bash
cd frontend
npm install
npm run dev
```

### 🧠 O que eu aprendi:

Consumo de APIs REST com fetch e Hooks (useState, useEffect).

Criação de rotas assíncronas com FastAPI.

Persistência de dados e manipulação de banco de dados SQL.