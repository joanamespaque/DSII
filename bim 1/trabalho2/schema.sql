CREATE TABLE "Autor" (
	"cod" serial, 
	"nome" VARCHAR(100) NOT NULL,
	"email" VARCHAR(120) UNIQUE NOT NULL,
	CONSTRAINT "AutorPK" PRIMARY KEY (cod));


CREATE TABLE "Trabalho" (
	"cod" serial,
	"conteudo" text NOT NULL,
	"nota" numeric(3,1) NOT NULL,
	"dataEntrega" timestamp,
	"titulo" varchar(100) NOT NULL,
	"dataHoraAtualizacao" timestamp,
	CONSTRAINT "TrabalhoPK" PRIMARY KEY ("cod"));

CREATE TABLE "TrabalhoAutor" (
	"codAutor" int, 
	"codTrabalho" int,
	CONSTRAINT "TrabalhoAutorPK" PRIMARY KEY ("codAutor","codTrabalho"), 
	CONSTRAINT "TrabalhoAutorAutorFK" FOREIGN KEY ("codAutor") REFERENCES "Autor"("cod")
		ON DELETE CASCADE ON UPDATE CASCADE ,
	CONSTRAINT "TrabalhoAutorTrabalhoFK" FOREIGN KEY ("codTrabalho") REFERENCES "Trabalho"("cod")
		ON DELETE CASCADE ON UPDATE CASCADE);
