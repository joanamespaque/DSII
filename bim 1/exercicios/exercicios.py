7) Escreva um programa leia três números e monte uma data, referente a sua data de nascimento.
Imprima a data como nos formatos do exemplo (analise o pacote datetime):
# a) 2018, 09 of August

from datetime import datetime
d = int(input("digite um dia:"))
m = int(input("digite um mes:"))
a = int(input("digite um ano:"))
d = datetime(a,m,d)
string = d.strftime("%Y, %d of %B")
print(string)

# b) 09/08/2018
from datetime import datetime
d = int(input("digite um dia:"))
m = int(input("digite um mes:"))
a = int(input("digite um ano:"))
d = datetime(a,m,d)
string = d.strftime("%d/%m/%Y")
print(string)

# c) ano: 2018, dia: 221
from datetime import datetime
d = int(input("digite um dia:"))
m = int(input("digite um mes:"))
a = int(input("digite um ano:"))
d = datetime(a,m,d)
string = d.strftime("ano: %Y, dia: %j")
print(string)

8) Leia os dados de uma pessoa: nome, dataNascimento, telefone (1 ou mais). Guarde-os em uma só
variável e imprima os dados. Use a classe dict.

nome = input("digite seu nome:")
data = input("digite sua data de nascimento:")
qtd = int(input("digite quantos numero de telefone você quer informar:"))
cont = 1
telefones = list()
while(cont <= qtd):
    novo = input("digite o numero de telefone")
    telefones.append(novo) 
    cont = cont+1   
d = dict()
d = {'nome':nome, 'data':data, 'telefone': telefones}
print(d)  

9) Em Python, para a geração de um número aleatório usamos o pacote random. Escreva um programa (jogo) que gere um número entre 0 e 1000 e peça para o usuário adivinhar o número. A cada tentativa o programa informa se o número informado pelo usuário é maior ou menor que o número a ser descoberto. Ao final o programa deve informar quantas tentativas foram feitas até a descoberta do número.

from random import random
r = int(random()*1000)
print(r)
n = int(input("adivinhe o numero:"))
c = 0
while(n!=r):
    if(n>r):
        print("o numero é menor que o que vc digitou, tente novamente")
        n = int(input("adivinhe o numero:"))
        c=c+1
    else:
        if(n<r):
            print("o numero é maior que o que vc digitou, tente novamente")
            n = int(input("adivinhe o numero:"))
            c=c+1
print("parabens vc acertou hehe depois de tentar "+str(c)+" vezes")
    
10) Faça uma função para cada situação:

#gerar uma matriz
# l = int(input("digite o numero de linhas da sua matriz:"))
# c = int(input("digite o numero de colunas da sua matriz:"))
# i = 1
# m = list()
# while(i<=l):
#     i2 = 1
#     m2 = list()
#     while(i2<=c):
#         n = input("digite o numero "+str(i2)+" da linha "+str(i)+"    ")
#         m2.append(n)
#         i2 = i2+1
#     m.append(m2)
#     i = i+1
# print(m)

a) Gere a matriz transposta
# [[1,2,3],[4,5,6]] => [[1,4],[2,5],[3,6]]
def transposta(m):
    c = 0
    trans = list()
    while(c<len(m[0])):
        new = list()
        i = 0
        while(i<len(m)):
            # print(c)
            # print(i)
            new.append(m[i][c])
            i = i+1
        c = c+1
        trans.append(new)
    return trans
print(transposta([[1,2,3],[4,5,6]]))

b) Some duas matrizes
def somaMatriz(m1,m2):
    new = list()
    if (len(m1)==len(m2) and type(m1[0])==list and type(m2[0])==list):
        c = 0 
        while(c<len(m1)):
            valor = list()
            i = 0
            while(i<len(m1[c])):
                valor.append(m1[c][i]+m2[c][i])
                i=i+1
                # print(valor)
            c = c+1
            new.append(valor)
    else:
        return "porra ai nao dá né meu amigo"
    return new
print(somaMatriz([[1,2],[3,4]], [[5,6],[7,8]]))
print(somaMatriz([[1,2],[3,4]], [5,6]))

c) Faça a multiplicação de duas matrizes.

def multMatriz(m1,m2):
    if(len(m1)==len(m2[0])):

    else:
        return "o numero de linhas da matriz1 precisa ser igual ao numero de colunas da 2"

11) Escreva uma classe pessoa com suas propriedades e um método __str__ para refazer o exercício 8.

# 8) Leia os dados de uma pessoa: nome, dataNascimento, telefone (1 ou mais). Guarde-os em uma só
# variável e imprima os dados. Use a classe dict.

class Pessoa:
    def _init_(self, nome, dataNascimento, telefone):
        self._nome = nome
        self._dataNascimento = dataNascimento
        self._telefone = []
    def _get_nome(self):
        print("getting...")
        return self.nome
    def _set_nome(self,nome):
        print("setting...")
        self._nome = nome 
    nome = property(_get_nome, _set_nome)

    def _get_dataNascimento(self):
        print("getting...")
        return self.dataNascimento
    def _set_dataNascimento(self, data):
        print("setting...")
        self._dataNascimento = data
    dataNascimento = property(_get_dataNascimento, _set_dataNascimento)

    def _get_telefone(self, pos):
        print("getting...")
        return self._telefone[pos]
    def _set_telefone(self, telefone):
        print("setting...")
        self._telefone.append(telefone)
    def mudaTelefone(pos, novo):
        self._telefone[pos] = novo
    telefone = property(_get_telefone, _set_telefone)
    def _str_(self):
    return "nome:{}, dataNascimento:{}, telefones:{}".format(self._nome, self._dataNascimento, self._telefone)

# p1 = Pessoa("joana", "22/03/2000")

12) Escreva uma classe, chamada Ponto, que representa um ponto no plano cartesiano.
atributos: x e y referentes as posições

import math 
class Ponto:
    def __init__(self, x, y):
        self._x = x 
        self._y = y
    def _get_x(self):
        return self._x 
    def _set_x(self, x):
        self._x = x 
    x = property(_get_x, _set_x)
    def _get_y(self):
        return self._y 
    def _set_y(self, y):
        self._y = y 
    y = property(_get_y, _set_y)
    def distancia_origem(self):
        d = self.x**2 + self.y**2
        d = math.sqrt(d)
        return d 
    def distancia_para(self, p):
        d = (p.x - self.x)**2 + (p.y - self.y)**2
        d = math.sqrt(d)
        return d 

p1 = Ponto(4,5)
p2 = Ponto(1,1)
p3 = Ponto(3,4)
p4 = Ponto(6,8)
print(p1.distancia_para(p2))
print(p3.distancia_origem())
print(p4.distancia_origem())

14) Escreva uma classe, chamada triângulo
atributos: ponto1, ponto2, ponto3
métodos: isosceles (retorno boolean), equilatero (retorno boolean), escaleno (retorno boolean) e
perimetro()
import math
class Triangulo:
    def __init__(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    def _get_p1(self):
        return self._p1 
    def _set_p1(self, p1):
        self._p1 = p1 
    p1 = property(_get_p1, _set_p1)

    def _get_p2(self):
        return self._p2 
    def _set_p2(self, p2):
        self._p2 = p2 
    p2 = property(_get_p2, _set_p2)

    def _get_p3(self):
        return self._p3 
    def _set_p3(self, p3):
        self._p3 = p3 
    p3 = property(_get_p3, _set_p3)
    def isosceles(self):
        d1 = (self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2
        d2 = (self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2
        d3 = (self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2
        if(((d1==d2)and(d2!=d3)) or ((d2==d3)and(d2!=d1)) or ((d1==d3)and(d2!=d3))):
            return True
        else:
            return False
    def equilatero(self):
        d1 = (self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2
        d2 = (self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2
        d3 = (self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2
        if((d1==d2)and(d2==d3)):
            return True
        else:
            return False
    def escaleno(self):
        d1 = (self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2
        d2 = (self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2
        d3 = (self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2
        if((d1!=d2)and(d2!=d3)and(d1!=d3)):
            return True
        else:
            return False
    def perimetro(self):
        d1 = (self.p1[0] - self.p2[0])**2 + (self.p1[1] - self.p2[1])**2
        d2 = (self.p2[0] - self.p3[0])**2 + (self.p2[1] - self.p3[1])**2
        d3 = (self.p3[0] - self.p1[0])**2 + (self.p3[1] - self.p1[1])**2
        return (d1+d2+d3)



        
t1 = Triangulo([5,6],[5,9], [2,3])
t2 = Triangulo([1,3],[4,3], [1,0])
print(t1.isosceles())
print(t1.equilatero())
print(t1.escaleno())
print(t1.perimetro())
print(t2.isosceles())
print(t2.equilatero())
print(t2.escaleno())
print(t2.perimetro())

15) Escreva um programa que leia três coordenadas, verifique se as mesmas formam um triângulo e
construam o objeto da classe triângulo. Por fim o programa mostra o tipo do triângulo: Escaleno,
Isósceles ou Equilátero.
x1 = int(input("digite x1:"))
y1 = int(input("digite y1:"))
x2 = int(input("digite x2:"))
y2 = int(input("digite y2:"))
x3 = int(input("digite x3:"))
y3 = int(input("digite y3:"))
c1 = [x1, y1]
c2 = [x2, y2]
c3 = [x3, y3]
d1 = (c1[0] - c2[0])**2 + (c1[1] - c2[1])**2
d2 = (c2[0] - c3[0])**2 + (c2[1] - c3[1])**2
d3 = (c3[0] - c1[0])**2 + (c3[1] - c1[1])**2
print(d1)
print(d2)
print(d3)

if(d1>d2+d3 or d2>d3+d1 or d3>d2+d1):
    print("nao eh triangulo")
else:
    triangulo = Triangulo(c1, c2, c3)
    if(triangulo.isosceles() == True):
        print("eh um triangulo isosceles")
    elif(triangulo.equilatero() == True):
        print("eh um triangulo equilatero")
    else:
        print("eh um triangulo escaleno")





