cdcdterCREATE TABLE departamento(
	"codigo" serial,
	"nome" varchar(100),
	"dt_atu" timestamp,
	"codgerente" int,
	CONSTRAINT "departamentoPK" PRIMARY KEY ("codigo"),
	CONSTRAINT "funcionarioDepartamentoFK" FOREIGN KEY ("codgerente")
		REFERENCES Funcionario ("codigo")
		on delete CASCADE
		on update CASCADE
);

CREATE TABLE funcionario(
	"codigo" serial,
	"nome" varchar(100),
	"codDepartamento" int,
	CONSTRAINT "funcionarioPK" PRIMARY KEY ("codigo"),
	CONSTRAINT "funcionarioDepartamentoFK" FOREIGN KEY ("codDepartamento")
			REFERENCES Departamento ("codigo")
			on delete CASCADE 
			on update CASCADE
);

CREATE TABLE projeto(
	"codigo" serial,
	"nome" varchar(100),
	"data" timestamp, 
	CONSTRAINT "projetoPK" PRIMARY KEY ("codigo")
);

CREATE TABLE funcproj(
	"codigofuncionario" int,
	"codigoprojeto" int,
	CONSTRAINT "FuncionarioProjetoPK" PRIMARY KEY ("codigofuncionario", "codigoprojeto"),
	CONSTRAINT "FuncionarioFK" FOREIGN KEY ("codigofuncionario")
			REFERENCES Funcionario ("codigo")
			on delete CASCADE 
			on update CASCADE,
	CONSTRAINT "ProjetoFK" FOREIGN KEY ("codigoprojeto")
			REFERENCES Projeto ("codigo")
			on delete CASCADE
			on update CASCADE
);

SELECT f.nome AS funcionario, f.coddepartamento, p.codigo AS codprojeto, p.nome AS projeto, p.data AS dataprojeto 
	FROM funcionario f INNER JOIN funcproj fp
	ON f.codigo = fp."codigoFuncionario"
	INNER JOIN projeto p ON p.codigo = fp."codigoProjeto"
	WHERE p.codigo = 1

INSERT INTO funcionario (nome, coddepartamento) values ('Thamyris', 1), ('Brenda', 1), ('Tiago',2), ('Lívia', 4), ('Celso', 3), ('José Alfredo', 2), ('Fifilha', 4) 
INSERT INTO departamento (nome, dt_atu) VALUES ('RH', now()), ('TI', now()), ('Comercial', now()), ('Financeiro', now()), ('Administrativo', now()), ('Auditoria', now()), ('Marketing', now()), ('Vendas', now())