import datetime
class Livro:
    def __init__(self, cod, titulo, data_publicacao, npaginas, autor):
        if(cod==0):
            self._cod = None
        else:
            self._cod = cod 
        self._titulo = titulo
        if(isinstance(data_publicacao, datetime.date)):
            self._data_publicacao = data_publicacao
        elif(isinstance(data_publicacao, str)):
            try:
                self._data_publicacao =  datetime.datetime.strptime(data_publicacao, '%d/%m/%Y').date()
            except ValueError as vrData:
                # print("Poxa... você inseriu um formato de data inválido!")
                raise ValueError("Poxa... você inseriu um formato de data inválido!")
        else:
            raise ValueError("Ops! O tipo informado deve ser data ou string.")
        self._npaginas = npaginas
        self._autor = autor
 
    def _str_(self): 
        return "Código:{} \n Título:{} \n Data de Publicação:{} \n Número de Páginas:{} \n Autor(a):{}".format(str(self._cod), self._titulo, self._data_publicacao.strftime("%d/%m/%Y"), str(self._npaginas), self._autor)

    def objSTR(self):
	    return str(self._cod) + "," + self._titulo + "," + self._data_publicacao.strftime("%d/%m/%Y")+ "," +  str(self._npaginas) + "," + self._autor + "; \n"

    def _get_cod(self):
        return self._cod
    def _set_cod(self, cod):
        self._cod = cod
    cod = property(_get_cod, _set_cod)

    def _get_titulo(self):
        return self._titulo
    def _set_titulo(self, titulo):
        self._titulo = titulo
    titulo = property(_get_titulo, _set_titulo)

    def _get_data_publicacao(self):
        return self._data_publicacao
    def _set_data_publicacao(self, data):
        if(isinstance(data, datetime.date)):
            self._data_publicacao = data
        elif(isinstance(data, str)):
            try:
                self._data_publicacao =  datetime.datetime.strptime(data, '%d/%m/%Y').date()
            except ValueError:
                raise ValueError("Poxa... você inseriu um formato de data inválido!")
        else:
            raise ValueError("Ops! O tipo informado deve ser data ou string.")
    data_publicacao = property(_get_data_publicacao, _set_data_publicacao)

    def _get_npaginas(self):
        return self._npaginas
    def _set_npaginas(self, npaginas):
        self._npaginas = npaginas
    npaginas = property(_get_npaginas, _set_npaginas)

    def _get_autor(self):
        return self._autor 
    def _set_autor(self, autor):
        self._autor = autor 
    autor = property(_get_autor, _set_autor)




