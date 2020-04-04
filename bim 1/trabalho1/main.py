from LivroDAO import *
import os
def main():
    os.system("cls")
    print("Seja bem-vindo ao livrinho da minha tragédia")
    print("Primeiramente você precisa saber o que digitar para chamar os comandos, então aqui vai:")
    print("0 para inserir um livro")
    print("1 para excluir um livro")
    print("2 para alterar um livro")
    print("3 para buscar um livro")
    print("4 para acessar a lista de livros")
    print("5 para sair")
    print("6 para limpar")
    livroDAO = LivroDAO()
    while True:
        try:
            option = int(input("Digite o número correspondente ao comando >"))
        except ValueError:
            print("Poxa... você inseriu um formato inválido!")
        else:
            if(option == 0):
                print("Você escolheu inserir um livro. Agora crie o objeto em etapas:")
                titulo = input("Título do livro > ")
                data = input("Data de publicação > ")
                c = True 
                while (c):
                    try: 
                        npaginas = int(input("Número de páginas > "))
                    except ValueError:
                        print("Você precisa digitar inteiros para número de páginas!")
                    else:
                        c = False
                autor = input("Nome do autor(a) > ")
                try:
                    livro = Livro(0, titulo, data, npaginas, autor)
                except BaseException:
                    print("Você digitou a data em um formato inválido!")
                else:
                    livroDAO.inserir(livro)
                    print("Livro inserido com sucesso!")
            elif(option == 1):
                print("Você escolheu excluir um livro. Abaixo, digite o código do livro que deseja excluir: ")
                c = True 
                while(c):
                    try:
                        codigo = int(input(" > "))
                    except ValueError:
                        print("Você precisa digitar apenas inteiros!")
                    else:
                        livroDAO.deletar(codigo)
                        print("Livro deletado com sucesso!")
                        c = False
            elif(option == 2):
                print("Você escolheu alterar um livro. Se preprare para criar o objeto em etapas:")
                c = True
                while(c):
                    try: 
                        codigo = int(input("Digite o código do livro que você quer alterar"))
                    except ValueError:
                        print("Você precisa digitar inteiros e um código válido!")
                    else:
                        c = False 
                titulo = input("Título do livro a alterar > ")
                data = input("Data de publicação a alterar > ")
                c = True 
                while (c):
                    try: 
                        npaginas = int(input("Número de páginas a alterar > "))
                    except ValueError:
                        print("Você precisa digitar inteiros para número de páginas!")
                    else:
                        c = False
                autor = input("Nome do(a) autor(a) a alterar > ")
                try:
                    livro = Livro(codigo, titulo, data, npaginas, autor)
                except BaseException:
                    print("Você digitou a data em um formato inválido!")
                else:
                    livroDAO.alterar(livro)
                    print("Livro alterado com com sucesso!")
            elif(option == 3):
                print("Você escolheu buscar por um livro. Abaixo, digite o código do livro que deseja:")
                c = True
                while(c):
                    try: 
                        codigo = int(input(" > "))
                    except ValueError:
                        print("Você precisa digitar inteiros e um código válido!")
                    else:
                        c = False 
                        livroDAO.busca(codigo)
            elif(option == 4):
                livroDAO.listar()
            elif(option == 5): 
                break
            elif(option == 6):
                os.system("cls")
                print("Seja bem-vindo ao livrinho da minha tragédia")
                print("Primeiramente você precisa saber o que digitar para chamar os comandos, então aqui vai:")
                print("0 para inserir um livro")
                print("1 para excluir um livro")
                print("2 para alterar um livro")
                print("3 para buscar um livro")
                print("4 para acessar a lista de livros")
                print("5 para sair")
                print("6 para limpar")
            else:
                print("poxa, tu nao ta colaborando... digita uma das opções, migo")

if __name__ == '__main__':
    main()
