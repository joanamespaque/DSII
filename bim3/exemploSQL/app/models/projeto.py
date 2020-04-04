from .. import db 
from .. models.funcionario import Funcionario

funcionario_projeto = db.Table('funcionarioprojeto', 
db.Column('idfuncionario',db.Integer, db.ForeignKey('funcionario.id', ondelete='cascade'), primary_key=True), 
db.Column('idprojeto', db.Integer, db.ForeignKey('projeto.id', ondelete='cascade'), primary_key=True), extend_existing=True)

class Projeto(db.Model):
    __tablename__ = 'projeto'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    funcionarios = db.relationship('Funcionario', secondary=funcionario_projeto, backref=('projeto')
    #, cascade="save-update, merge, delete"
    )

    # funcionario com F maiusculo

    def vinculaFuncionarios(self, ids):
        self.funcionarios.clear()
        for id in ids:
            f = Funcionario.query.get(id)
            self.funcionarios.append(f)

        db.session.commit()
        return print(self.funcionarios)

    def salva(self, ids):
        if(self.id):
            aux = Projeto.query.get(self.id)
            aux.nome = self.nome
            self = aux
        else:
            db.session.add(self)
        db.session.commit()
        self.vinculaFuncionarios(ids)

        
    def excluir(self):
        db.session.delete(self)
        db.session.commit()        