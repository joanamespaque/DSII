CREATE TABLE "filme"(
id serial,
titulo varChar(50) NOT NULL,
direcao varChar(50) NOT NULL,
genero varChar(200) NOT NULL,
duracao TIME NOT NULL,
sinopse varChar(500) NOT NULL,
elenco varChar(500) NOT NULL,
"dataLancamento" DATE NOT NULL,
classificacao varChar(5) NOT NULL,
CONSTRAINT "FilmePK" PRIMARY KEY (id)
);

INSERT INTO filme ("titulo", "direcao", "genero", "duracao", "sinopse", "elenco", "dataLancamento", "classificacao") VALUES ('Homem de Ferro', 'Jon Favreau', 'Ação, aventura, ficcao cientifica', '02:06:00', 'DescriçãoTony Stark é um industrial bilionário e inventor brilhante que realiza testes bélicos no exterior, mas é sequestrado por terroristas que o forçam a construir uma arma devastadora. Em vez disso, ele constrói uma armadura blindada e enfrenta seus sequestradores. Ao voltar para os EUA, Stark aprimora a armadura e a utiliza para combater o crime.', 'Robert Downey Jr., Terrence Howard, Jeff Bridges, Shaun Toub, Gwyneth Paltrow', '12/04/2008', '12'), ('Harry Potter e a Pedra Filosofal', 'Chris Columbus
', 'Aventura, fantasia', '02:39:00', 'Conheça Harry Potter, um menino que soube em seu aniversário de onze anos que é filho órfão de dois bruxos e possui poderes mágicos únicos. De filho indesejado, passa a ser um estudante de Hogwarts, uma escola inglesa para bruxos. Lá ele conhece vários amigos que o ajudam a descobrir a verdade sobre as mortes misteriosas de seus pais.', 'Daniel Radcliffe, Rupert Grint e Emma Watson', '16/11/2001', 'Livre'), ('Titanic', 'James Cameron', 'Épico, drama, romance', '03:15:00', 'Um artista pobre e uma jovem rica se conhecem e se apaixonam na fatídica jornada do Titanic, em 1912. Embora esteja noiva do arrogante herdeiro de uma siderúrgica, a jovem desafia sua família e amigos em busca do verdadeiro amor.', 'Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates, Frances Fisher, Gloria Stuart, Bernard Hill, Victor Garber, Jonathan Hyde, Danny Nucci, Bill Paxton', '01/11/1997', '12');
SELECT * FROM filme;
