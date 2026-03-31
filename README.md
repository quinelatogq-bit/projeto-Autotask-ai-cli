# 🚀 AutoTask AI CLI

Sistema de automação de tarefas via terminal com priorização inteligente.

## 📌 Funcionalidades

- Criar tarefas
- Listar tarefas
- Concluir tarefas
- Excluir tarefas
- Priorização automática por palavras-chave

## 🧠 Inteligência aplicada

O sistema identifica prioridade automaticamente com base no texto da tarefa.

### Regras:
- "urgente", "hoje", "agora", "importante", "cliente", "prazo" → prioridade alta
- "estudar", "revisar", "organizar", "treinar" → prioridade média
- demais casos → prioridade baixa

## 💻 Tecnologias usadas

- Python
- JSON
- CLI (interface via terminal)

## ▶️ Como executar

```bash
python3 main.py
