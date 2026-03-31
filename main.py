from tarefas import (
    criar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa
)

def menu():
    while True:
        print("\n=== AutoTask AI ===")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Excluir tarefa")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome da tarefa: ")
            criar_tarefa(nome)
            print("Tarefa criada com sucesso.")

        elif op == "2":
            listar_tarefas()

        elif op == "3":
            listar_tarefas()
            try:
                indice = int(input("Digite o índice da tarefa concluída: "))
                concluir_tarefa(indice)
            except ValueError:
                print("Digite um número válido.")

        elif op == "4":
            listar_tarefas()
            try:
                indice = int(input("Digite o índice da tarefa que deseja excluir: "))
                excluir_tarefa(indice)
            except ValueError:
                print("Digite um número válido.")

        elif op == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")

menu()
