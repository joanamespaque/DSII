from TrabalhoDAO import *

if (__name__ == '__main__'):
    daoA = AutorDAO()
    daoT = TrabalhoDAO()
    # autor1 = Autor("Raquel Barbosa", "raquelmbarbosa@gmail.com")
    # autor2 = Autor("Márcio Torres", "josue@gmail.com")
    # autor3 = Autor("America Singer", "singer@gmail.com")
    
    # lista = daoA.listar()
    # for a in lista:
    #     print(a)

    # try:
        # daoA.salvar(autor1)
        # daoA.salvar(autor2)
    #     daoA.salvar(autor3)
    # except psycopg2.errors.UniqueViolation:
    #     print("email duplicado, tetahead!")
    
    # try:
    #     print(daoA.buscar(3))
    #     alteraAutor = daoA.buscar(1)
    #     alteraAutor.nome = "Joana Mespaque"
    #     alteraAutor.email = "jojo@gmail.com"
    #     daoA.salvar(alteraAutor)
    # except psycopg2.errors.InvalidTextRepresentation:
    #     print("O formato de código deve ser int")
    # except TypeError:
    #     print("Valor do código de autor errado")
    # daoA.excluir(3)


    # trabalho = Trabalho("Pesquisa de Acessibilidade", "A acessibilidade no IFRS campus Rio Grande", 5.5)
    # trabalho2 = Trabalho("Química Orgânica", "Funções oxigenadas", 8)
    # trabalho3 = Tabalho("Inteligência Artificial", "pipipipopopo", 3)
    # trabalho4 = Trabalho("Python é minha morte", "socorro", 1)
    # daoT.salvar(trabalho)
    # # daoT.salvar(trabalho2)
    # # daoT.salvar(trabalho3)
    # # daoT.salvar(trabalho4)
    # try:
    #     #entrega e altera
    #     trabalho = daoT.buscar(trabalho.cod)
    #     trabalho.entregaTrabalho()
    #     daoT.salvar(trabalho)


    #     #alterar
    #     trabalho3 = daoT.buscar(1)
    #     trabalho3.titulo = "Trabalho da Lívia"
    #     trabalho3.conteudo = "Se a vida é uma festa, o que falar da morte?"
    #     trabalho3.entregaTrabalho()
    #     daoT.salvar(trabalho3)

    #     #codigo errado
    #     trabalho5 = daoT.buscar(90)
    # except IndexError:
    #     print("Valor do código de Trabalho errado")


    # autorTrab1 = daoA.buscar(1)
    # autorTrab2 = daoA.buscar(2)
    # autorTrab3 = daoA.buscar(3)
    # trabalho3.vinculaAutor(autorTrab1)
    # trabalho3.vinculaAutor(autorTrab2)
    # daoT.vinculaAutor(trabalho3)
    # daoT.salvar(trabalho3)
    
    # lista = daoT.listar()
    # for t in lista:
    #     print(t)
    # print(daoT.buscar(6))
    # daoT.excluir(7)



    



    

    



