from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# NOME DO BANCO PADRONIZADO: tarefas.db
DB_NAME = "tarefas.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, texto TEXT)")
    conn.commit()
    conn.close()

init_db()

class Tarefa(BaseModel):
    texto: str

@app.get("/tarefas")
def listar():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    dados = [{"id": row[0], "texto": row[1]} for row in cursor.fetchall()]
    conn.close()
    return dados

@app.post("/tarefas")
def adicionar(tarefa: Tarefa):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (texto) VALUES (?)", (tarefa.texto,))
    conn.commit()
    conn.close()
    return {"status": "sucesso"}

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    conn = sqlite3.connect(DB_NAME) # <--- AQUI ESTAVA O ERRO (estava database.db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    conn.commit()
    conn.close()
    return {"status": "removido com sucesso"}