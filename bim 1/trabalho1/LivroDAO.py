from Livro import *
class LivroDAO:
    def __init__(self):
        self._nome_arq = 'arquivo.txt'
        arquivo = open(self._nome_arq, 'r+')
        self._contArq = arquivo.readlines()
        # self._nlinhas = self._contArq.__len__()
    def busca(self, cod):
        try:
            with open(self._nome_arq, 'r') as arquivo:
                contArq = arquivo.readlines()
                nlinhas = contArq.__len__()
                if(nlinhas != 0):
                    for i in range(0, len(contArq)):
                        # nlinhas = self._contArq.__len__()
                        linha = contArq[i].split(',')
                        if(int(linha[0]) == cod):
                            print("Buscando...")
                            print("Título:{}, Data de Publicação:{}, Número de Páginas:{}, Autor(a):{}".format(linha[1], linha[2], linha[3], linha[4]))
                            break
                else:
                    print("o arquivo está vazio, não há itens para buscar!")
        except FileNotFoundError as fnfe:
            print(fnfe.strerror)
            print("Arquivo não econtrado!")
       
    def listar(self):
        try:
            with open(self._nome_arq, 'r+') as arquivo:
                contArq = arquivo.readlines()
                nlinhas = contArq.__len__()
                if(nlinhas != 0):
                    for i in range(0, nlinhas):
                        linha = contArq[i].split(',')
                        l = Livro(0, linha[1], linha[2], linha[3], linha[4])
                        l._set_cod(linha[0])
                        print(l._str_()+'\n')
                else:
                    print("O arquivo está vazio, não há itens para listar!")
        except FileNotFoundError as fnfe:
            print(fnfe.strerror)
            print("Arquivo não encontrado!")


    def inserir(self, obj):
        try: 
            with open(self._nome_arq, 'a') as arquivo:
                contArq = arquivo.readlines()
                nlinhas = contArq.__len__()
                # print(nlinhas)
                cod_obj = nlinhas + 1
                obj._cod = cod_obj
                string = obj.objSTR()
                arquivo.write(string)
        except FileNotFoundError as fnfe:
            print(fnfe.strerror)
            print("Arquivo não encontrado!")

    def alterar(self, obj):
        try:
            with open(self._nome_arq, 'r+') as arquivo:
                nlinhas = self._contArq.__len__()
                if(nlinhas != 0):
                    for i in range(0, len(self._contArq)):
                        linha = self._contArq[i].split(',')
                        # print(obj._get_cod())
                        if(int(linha[0]) == obj._get_cod()):
                            string = obj.objSTR()
                            self._contArq[i] = string
                            # print(self._contArq)
                            break
                    vetor = self._contArq
                    arquivoNovo = open(self._nome_arq , 'w')
                    for i in range (0, len(vetor)):
                        arquivoNovo.writelines(vetor[i])
                else:
                    print("O arquivo está vazio, não há livros para alterar")
        except FileNotFoundError as fnfe:
            print(fnfe.strerror)
            print("Arquivo não encontrado!")

    def deletar(self, cod):
        try:
            with open(self._nome_arq, 'w') as arquivo:
                nlinhas = self._contArq.__len__()
                if(nlinhas != 0):
                    for i in range(0, len(self._contArq)):
                        linha = self._contArq[i].split(',')
                        if (int(linha[0]) == cod):
                            p = i
                            self._contArq.pop(p)
                            # print(self._contArq)
                            break
                    # arquivo = open('arquivo.txt', 'w')
                    # print(self._contArq)
                    arquivo.writelines(self._contArq)
                else:
                    print("O arquivo está vazio, não há itens para excluir!")
        except FileNotFoundError as fnfe:
            print(fnfe.strerror)
            print("Arquivo não encontrado!")


ld = LivroDAO()
l1 = Livro(0, "Harry Potter e a Pedra Filosofal", "26/06/1997", 244, "jk biscoiteira")
l2 = Livro(0, "Harry Potter e a Camara Secreta", "02/07/1998", 327, "jk biscoiteira")
l3 = Livro(0, "Harry Potter e o Prisioneiro de Azkaban", "08/07/1999", 348, "jk biscoiteira")
l4 = Livro(0, "Harry Potter e o Cálice de Fogo", "08/07/2000", 636, "jk biscoiteira")
l5 = Livro(4, "teste", "22/03/2000", 333, "alo celso")
# ld.inserir(l1)
# ld.inserir(l2)
# ld.inserir(l3)
# ld.inserir(l4)
ld.alterar(l5)
# ld.deletar(333)


# ld.deletar(1)