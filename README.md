# 🚀 AutoTask AI CLI

Sistema de automação de tarefas via terminal com priorização inteligente.

## 📌 Funcionalidades

- Criar tarefas por comando
- Listar tarefas ordenadas por prioridade
- Concluir tarefas
- Excluir tarefas com confirmação
- Comando de ajuda
- Priorização automática por palavras-chave
-Geração automática de descrição
-Sugestão automática de categoria 

## 🧠 Inteligência aplicada

O sistema define a prioridade automaticamente com base no texto da tarefa.
Além da prioridade, o sistema também gera automaticamente:
-descrição da tarefa
-categoria estimada

### Regras atuais
- "urgente", "hoje", "agora", "importante", "cliente", "prazo" → alta
- "estudar", "revisar", "organizar", "treinar" → média
- demais casos → baixa

## 💻 Tecnologias usadas

- Python
- JSON
- CLI (Command Line Interface)

## ▶️ Como executar

```bash
python3 main.py
