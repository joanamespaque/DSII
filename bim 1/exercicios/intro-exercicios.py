for(i=0;i<10;i++) -> for i in range(10)
list(range(10));

    def soma(x,y=10):
        return x+y
    print(soma(2)) 

    def fatorial(x)
        for i in ramge(x,1,-1)
            x = x*(x-1)
        return x    

1) Leia um número e o imprima o seu quadrado invertido. Exemplo, entrada: 12 | saída: 441.
n = int(input('informe um numero:'))
n = str(n**2)
a = len(n)-1
string = ''
while (a >= 0):
    string += n[a]
    a = a-1
print('alo celso'+string)
2) Crie um programa em Python que leia um nome completo e mostre na tela somente o seu nome e
sobrenome. Ex.: "João Marcos Cavalcante Bezerra", o programa deverá mostrar quantas palavras
possui o nome e o nome de maneira reduzida "João M. C. Bezerra".

nome = input('digite um nome aquiiiiiii:')
vetor = nome.split(' ')
string = vetor[0]
c = 1
while (c < len(vetor)-1):
    string += ' '+vetor[c][0]+'.'
    c = c+1
string += vetor[len(vetor)-1]
print(string)
 
3) Escreva uma função, chamada fat, que retorne o fatorial de um número. A função deve verificar se o
parâmetro passado é inteiro e maior do que zero, caso contrário deve retornar -1.

n = int(input('digite um number para calcular o famoso fatorial:'))
def fat(x):
    f = x 
    c = x-1
    if x > 0:
        while c > 0:
            f = f*c
            c = c-1
    else:
        if x == 0:
            f = 1
        else:
            f = -1
    return f
print(fat(n))


4) Faça uma função que receba um vetor de inteiro e imprima o somatório dos n termos, retorne a
média dos elementos.
def media(vetor):
    c = 0
    soma = 0
    while c < len(vetor):
        soma += vetor[c]
        c = c+1
    return soma/(len(vetor))
print(media([1,2,3,4,5]))

5)Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar
de 1 a 100.

ehprimo = int(input('digite um numero para saber se eh primo:'))
def primo(n):
    c = 0
    i = 1
    while i <= ehprimo:
        if ehprimo%i == 0:
            c=c+1
        i = i+1
    if c == 2:
        return "eh primo"
    else:
        return "nao eh"
print(primo(ehprimo))

6)Escreva uma função que receba uma frase como parâmetro. Retorne uma nova frase com cada
palavra com as letras invertidas.

f = input("digita uma frase ai:")
def inverte(frase):
    nova = ""
    c = len(frase)-1
    while c >= 0:
        nova = nova+frase[c]
        c = c-1
    return nova
print(inverte(f))