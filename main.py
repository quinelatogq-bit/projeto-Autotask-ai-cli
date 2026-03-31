from tarefas import (
    criar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa
)

def exibir_comandos():
    print("\n=== AutoTask AI ===")
    print("Comandos disponíveis:")
    print("criar <nome da tarefa>")
    print("listar")
    print("concluir <indice>")
    print("excluir <indice>")
    print("ajuda")
    print("sair")

def interpretar_comando(comando):
    partes = comando.strip().split()

    if not partes:
        print("Digite um comando válido.")
        return True

    acao = partes[0].lower()

    if acao == "criar":
        if len(partes) < 2:
            print("Digite o nome da tarefa após 'criar'.")
            return True

        nome_tarefa = " ".join(partes[1:])
        criar_tarefa(nome_tarefa)
        print("Tarefa criada com sucesso.")

    elif acao == "listar":
        listar_tarefas()

    elif acao == "concluir":
        if len(partes) < 2:
            print("Digite o índice da tarefa.")
            return True

        try:
            indice = int(partes[1])
            concluir_tarefa(indice)
        except ValueError:
            print("O índice deve ser um número.")

    elif acao == "excluir":
        if len(partes) < 2:
            print("Digite o índice da tarefa.")
            return True

        try:
            indice = int(partes[1])
            confirmacao = input("Tem certeza que deseja excluir? (s/n): ").lower()

            if confirmacao == "s":
                excluir_tarefa(indice)
            else:
                print("Exclusão cancelada.")
        except ValueError:
            print("O índice deve ser um número.")

    elif acao == "ajuda":
        exibir_comandos()

    elif acao == "sair":
        print("Encerrando sistema...")
        return False

    else:
        print("Comando não reconhecido. Digite 'ajuda' para ver os comandos.")

    return True

def main():
    exibir_comandos()

    while True:
        comando = input("\nDigite um comando: ")
        continuar = interpretar_comando(comando)

        if continuar is False:
            break

main()

