# 1) Classe: Pessoa
# Atributos: nome, idade, altura, peso
# Construtor que receba no mínimo o nome e no máximo todos atributos
# Métodos:
# -faz_aniversario(): incrementa em um a idade;
# -emagrece(qtde);
# -engorda(qtde);
# -cresce(qtdeEmcm);
# -to_s.
# Testes: Crie diferentes pessoas passando os parâmetros ou não. Caso
# não passe os parâmetros, altere os atributos após a criação. Faça alguns
# aniversários, emag
class Pessoa: 
    def __init__(self, nome=, idade, altura, peso):
        self._nome = nome
        self._idade = idade
        self._altura = altura
        self._peso = peso

        def _get_nome(self):
            return self._nome
        def _set_nome(self, nome):
            self.nome = nome
        nome = property(_get_nome, _set_nome)

        def _get_idade(self):
            return self._idade
        def _set_idade(self, idade):
            self.idade = idade
        idade = property(_get_idade, _set_idade)

        def _get_altura(self):
            return self._altura
        def _set_altura(self, altura):
            self.altura = altura
        altura = property(_get_altura, _set_altura)

        def _get_peso(self):
            return self._peso
        def _set_peso(self, peso):
            self.peso = peso
        peso = property(_get_peso, _set_peso)
        
        def to_s(self):
            return "nome:{}, idade:{}, altura:{}, peso:{}".format(self._nome, self._idade, self._altura, self._peso)

        def faz_aniversario(self):
            self.idade += 1
        
        def emagrece(self, qtd):
            self.peso -= qtd

        def engorda(self, qtd):
            self.peso += qtd 

        def cresce(self, qtd):
            self.altura += (qtd*100)
