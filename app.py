# Cadastrar Livro
if opcao == "1":
    # Arquivo Principal do Sistema


from models.livro import Livro
from services.biblioteca_service import carregar_livro, salvar_livros


livros = carregar_livro()


print("==================================")
print("===== Sistema de Biblioteca =====")
print("==================================")


print("Categoria padrão: ", Livro.categoria_padrao())


while True:
    print("\nMENU")
    print("\n1 -  Cadastrar Livro")
    print("2 -  Listar Livros")
    print("3 -  Alterar Livro")
    print("4 -  Sair")

    opcao = input("\nEscolha uma opção: ")


# Cadastrar Livro
    if opcao == "1":
        print("\nCadastro de Livro")

        titulo = input("\nTítulo: ")
        autor = input("\nAutor: ")
        ano = input("\nAno: ")

        livro = Livro(titulo, autor, ano)
        livros.append(livro)
        salvar_livros(livros)
        print("\nLivro cadastrado!")

    elif opcao == "2":
        print("\n Lista de Livros")
        if len(livros) == 0:
            print("Nenhum livro cadastrado")
        else:
            for i, livro in enumerate(livros):
                print("livro", i)
                livro.exibir()

    elif opcao == "3":
        for i, livro in enumerate(livros):
            print(i, ' - ', livro.titulo)
        pos = int(input("\nEscolha o número do livro"))
        novo = input("\nNovo titulo: ")
        livros[pos].titulo = novo
        salvar_livros(livros)

    elif opcao == "4":
        print("Encerrando o Sistema...")
        break
    else:
        print("Opção inválida!")
