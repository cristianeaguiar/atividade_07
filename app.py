# Biblioteca
import os

# lista de nomes
nomes = []

#loop
while True:
    #menu
    print("1 - Cadastre novo nome.")
    print("2 - Exibir lista.") 
    print("3 - Ordenar.")
    print("4 - Alterar nome da lista.")
    print("5 - Excluir nome da lista.")
    print("6 - Sair do programa.")

# usuário informa a opção deseja 
    opcao = input("opção desejada: ")

# Limpa console
    os.system("cls")

# program verifica a opção escolhidapelo usuário
    match opcao:
        case "1":
            novo_nome = input("Informe o nome a ser cadastrado: ")
            nomes.append(novo_nome)
            print(f"{novo_nome} cadastrado com sucesso!")
            continue
        case "2":
            print("Lista:\n")
            for i in range(len(nomes)):
                print(f"Índice {i}: {nomes[i]}.")
            print("\n")
            continue
        case "3":
            nomes.sort()
            print("Lista ordenada com sucesso!")
            continue
        case "4":
            try:
                indice = int(input("Informe o índice do nome a ser alterado: "))
                confirmar = input(f"Deseja alterar o nome {nomes [indice]}? Digite 'sim' para confirmar: ")

                if confirmar == "sim":
                    nomes[indice] = input("Informe o novo nome: ")
                    print("Nome alterado com sucesso!")
                else:
                    print(f"Não foi possível alterar. {e}.")
            except Exception as e:
                print(f"Não foi possível alterar. {e}.")
            finally:
                continue
        case "5":
            try:
                indice = int(input("Informe o índice que deseja excluir: "))
                confirmar = input(f"Deseja excluir o nome {nomes[indice]} da lista? Digite 'sim' para confirmar: ")

                if confirmar == "sim":
                    del(nomes[indice])
                    print("Nome excluído com sucesso.")
                else:
                    print("Nome não foi excluído.")
            except Exception as e:
                print(f"Não foi possível excluir nome.{e}.")
            finally:
                continue
        case "6":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue


    







      
