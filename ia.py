def melhorar_tarefa(nome):
    nome = nome.strip().capitalize()
    return nome

def sugerir_prioridade(nome):
    nome = nome.lower()

    palavras_alta = ["urgente", "agora", "cliente", "prazo", "dinheiro", "entregar"]
    palavras_media = ["estudar", "organizar", "treinar", "revisar", "planejar"]

    for palavra in palavras_alta:
        if palavra in nome:
            return "alta"

    for palavra in palavras_media:
        if palavra in nome:
            return "média"

    return "baixa"

def gerar_descricao(nome):
    return f"Tarefa criada automaticamente para: {nome}"

def sugerir_categoria(nome):
    nome = nome.lower()

    if "estudar" in nome or "curso" in nome or "python" in nome:
        return "estudos"
    elif "cliente" in nome or "vender" in nome or "dinheiro" in nome:
        return "trabalho"
    elif "treinar" in nome or "academia" in nome:
        return "saúde"
    else:
        return "geral"
