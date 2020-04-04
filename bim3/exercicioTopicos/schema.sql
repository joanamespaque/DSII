CREATE TABLE "usuario"(
    "cod" serial,
    "nome" varchar(100) NOT NULL,
    "email" varchar(100) NOT NULL,
    "login" varchar(100) UNIQUE,
	"senha" VARCHAR(32) NOT NULL,
    "altura" float(2) NOT NULL,
    "idade" int NOT NULL,
    CONSTRAINT "AutorPK" PRIMARY KEY ("cod")
);

CREATE TABLE "serie"(
    "cod" serial, 
    "titulo" varchar(100) NOT NULL,
    "foto" varchar(200) NOT NULL,
    "codusuario" int NOT NULL,
    CONSTRAINT "seriePK" PRIMARY KEY ("cod"), 
    CONSTRAINT "SerieUserFK" FOREIGN KEY ("codusuario")
        REFERENCES "usuario" 
        ON DELETE SET NULL
        ON UPDATE NO ACTION
);

CREATE TABLE "temporada"(
    "cod" serial, 
    "titulo" varchar(100) NOT NULL,
    "numero" int NOT NULL,
    "codSerie" int NOT NUll,
    CONSTRAINT "temporadaPK" PRIMARY KEY ("cod"),
    CONSTRAINT "serieFK" FOREIGN KEY ("codSerie")
        REFERENCES "serie" ("cod")
        ON DELETE SET NULL
		ON UPDATE CASCADE 
);

CREATE TABLE "episodio"(
    "cod" serial, 
    "titulo" varchar(100) NOT NULL, 
    "codSerie" int NOT NULL, 
    "numero" int NOT NULL,
    "codTemporada" int NOT NULL, 
    CONSTRAINT "episodioPK" PRIMARY KEY ("cod"),
    CONSTRAINT "serieFK" FOREIGN KEY ("codSerie")
        REFERENCES "serie" ("cod")
        ON DELETE SET NULL
		ON UPDATE CASCADE,
    CONSTRAINT "temporadaFK" FOREIGN KEY ("codTemporada")
        REFERENCES "temporada" ("cod")
        ON DELETE SET NULL
		ON UPDATE CASCADE 
);