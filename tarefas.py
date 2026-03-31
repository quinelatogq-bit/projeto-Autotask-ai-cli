from storage import carregar, salvar

def criar_tarefa(nome):
    tarefas = carregar()

    prioridade = definir_prioridade(nome)

    nova = {
        "nome": nome,
        "status": "pendente",
        "prioridade": prioridade
    }

    tarefas.append(nova)
    salvar(tarefas)

def listar_tarefas():
    tarefas = carregar()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    prioridade_ordem = {"alta": 0, "média": 1, "baixa": 2}

    tarefas_com_indice = list(enumerate(tarefas))

    tarefas_ordenadas = sorted(
        tarefas_com_indice,
        key=lambda item: prioridade_ordem[item[1]["prioridade"]]
    )

    print("\n=== LISTA DE TAREFAS ===")
    print("-" * 40)

    for indice_real, t in tarefas_ordenadas:
        print(f"[{indice_real}] {t['nome']}")
        print(f"     Status: {t['status']}")
        print(f"     Prioridade: {t['prioridade']}")
        print("-" * 40)

def concluir_tarefa(indice):
    tarefas = carregar()

    if 0 <= indice < len(tarefas):
        tarefas[indice]["status"] = "concluída"
        salvar(tarefas)
        print("Tarefa concluída com sucesso.")
    else:
        print("Índice inválido.")

def excluir_tarefa(indice):
    tarefas = carregar()

    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        salvar(tarefas)
        print(f"Tarefa removida: {removida['nome']}")
    else:
        print("Índice inválido.")

def definir_prioridade(nome):
    nome = nome.lower()

    palavras_alta = ["urgente", "hoje", "agora", "importante", "cliente", "prazo"]
    palavras_media = ["estudar", "revisar", "organizar", "treinar"]

    for palavra in palavras_alta:
        if palavra in nome:
            return "alta"

    for palavra in palavras_media:
        if palavra in nome:
            return "média"

    return "baixa"
