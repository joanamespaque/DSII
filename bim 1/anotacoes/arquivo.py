# arquivos em python: 
# função open:
#     - nome arquivo
#     - modo leitura
#        - binario: b
#        - texto: t
#        - w: escrita
#        - r: leitura
#        - a: escrita fim arquivo (append)
#        - x: cria novo p/ escrita 
#        - +: le e escreve
# funções para leitura:
#     read -> le o texto e coloca em uma string 
#     readline -> ler uma linha - procura pelo "/n"
#     readlines -> le o texto e retorna uma lista de strings 
# função write:
#     escreve um conjunto de caracteres 

def leArq(nome):
    try: 
        arq = open(nome, 'r')
    except FileNotFoundError as fnfe:
        print(fnfe.strerror)
        print("erro abrindo arquivo!")
    else:
        for linha in arq: #usa o readline() 
            print(linha.rstrip())  #tirar o /n no final
        arq.close() #fecha o arquivo -> poderia estar dentro de um finally (se der erro ou nao, fecha o arquivo)

def addArq(nome, linha):
    with open(nome,'a') as arq: 
        arq.write(linha)

# def addArq(nome, linha):
#     try:
#         arq = open(nome,a)
#         arq.write(linha)
#     finally:
#         arq.close()


def ain():
