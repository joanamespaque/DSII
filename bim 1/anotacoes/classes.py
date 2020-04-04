class Pessoa: 
    def _init_(self, nome, cpf, idade):
        self._cpf = cpf
        self._nome = nome
        self._idade = idade
        def _str_(self):
            return "nome:{}, idade:{}, cpf:{}".format(self._nome, self._idade, self._cpf)
        def _get_nome(self):
            return self._nome
        def _set_nome(self, nome):
            self.nome = nome
        nome = property(_get_nome, _set_nome)

# p = Pessoa('Julio')
# p.nome = 'junio'

        

