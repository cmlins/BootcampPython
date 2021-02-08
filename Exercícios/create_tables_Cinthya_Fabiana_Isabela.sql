-- DROP TABLE IF EXISTS Clientes CASCADE;
-- DROP TABLE IF EXISTS Ingressos;
-- DROP TABLE IF EXISTS Sessoes;
-- DROP TABLE IF EXISTS Filmes;
-- DROP TABLE IF EXISTS Salas;

CREATE DATABASE Cinema;

CREATE TABLE Filmes (
	Id_filme SERIAL PRIMARY KEY,
	Nome VARCHAR(255),
	Duracao INT,
	Genero VARCHAR(100),
	Classificacao_indicativa VARCHAR(10),
	Sinopse TEXT
);

CREATE TABLE Salas (
	Id_sala SERIAL PRIMARY KEY,
	Nome VARCHAR(255),
	Lotacao INT,
	Numero INT,
	Is_3d BOOLEAN
);

CREATE TABLE Clientes (
 	Id_cliente SERIAL PRIMARY KEY,
 	Nome VARCHAR(255) NOT NULL,
 	Cpf VARCHAR(11) NOT NULL,
 	Data_nascimento DATE,
 	Email VARCHAR(100),
 	Telefone VARCHAR(11)	
 );
 
CREATE TABLE Sessoes (
	Id_sessao SERIAL PRIMARY KEY,
	Datas DATE,
	Hora TIME,
	Duracao INT,
	Id_sala INT,
	Id_filme INT,
	FOREIGN KEY (Id_sala) REFERENCES Salas(Id_sala),
	FOREIGN KEY (Id_filme) REFERENCES Filmes(Id_filme)
);

CREATE TABLE Ingressos (
	Id_ingresso SERIAL PRIMARY KEY,
	Id_cliente INT,
	Id_sessao INT,
	FOREIGN KEY (Id_cliente) REFERENCES Salas(Id_sala),
	FOREIGN KEY (Id_sessao) REFERENCES Sessoes(Id_sessao)
);