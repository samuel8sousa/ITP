# Inicializando uma lista vazia para armazenar os nomes
nomes = []

# Função para adicionar um nome à lista
def adicionar_nome():
    nome = input("Digite o nome que deseja adicionar: ")
    nomes.append(nome)
    print(f"{nome} foi adicionado com sucesso!")

# Função para exibir a lista de nomes
def exibir_nomes():
    if nomes:
        print("Lista de nomes armazenados:")
        for i, nome in enumerate(nomes, start=1):
            print(f"{i}. {nome}")
    else:
        print("A lista de nomes está vazia.")

# Menu principal do programa
while True:
    print("\n1. Adicionar nome")
    print("2. Exibir nomes")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_nome()
    elif opcao == '2':
        exibir_nomes()
    elif opcao == '3':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")



