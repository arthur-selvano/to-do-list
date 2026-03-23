import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [tarefas, setTarefas] = useState([])
  const [input, setInput] = useState("")

  const API_URL = "http://127.0.0.1:8000/tarefas"

  // 1. Buscar tarefas do Python ao carregar
  const carregarTarefas = async () => {
    try {
      const res = await fetch(API_URL)
      const dados = await res.json()
      setTarefas(dados)
    } catch (error) {
      console.error("Erro ao carregar tarefas. O backend está rodando?", error)
    }
  }

  useEffect(() => {
    carregarTarefas()
  }, [])

  // 2. Adicionar tarefa
  const adicionar = async () => {
    if (!input) return
    await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ texto: input })
    })
    setInput("")
    carregarTarefas()
  }

  // 3. Deletar tarefa
  const deletarTarefa = async (id) => {
    await fetch(`${API_URL}/${id}`, {
      method: 'DELETE',
    });
    carregarTarefas(); 
  };

  return (
    <div className="container">
      <h1>To-Do List</h1>
      
      <div className="input-group">
        <input 
          value={input} 
          onChange={(e) => setInput(e.target.value)}
          placeholder="Digite uma tarefa..." 
        />
        <button onClick={adicionar}>Adicionar</button>
      </div>

      <ul className="lista-tarefas">
        {tarefas.map((t) => (
          <li key={t.id} className="item-tarefa">
            <span>{t.texto}</span>
            <button 
              className="btn-del"
              onClick={() => deletarTarefa(t.id)}
            >
              Apagar
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App