DROP TABLE IF EXISTS Funcionario CASCADE;
DROP TABLE IF EXISTS Cliente CASCADE;
DROP TABLE IF EXISTS Pedido CASCADE;
DROP TABLE IF EXISTS Funcao CASCADE;
DROP TABLE IF EXISTS Item_compra CASCADE;
DROP TABLE IF EXISTS Produto CASCADE;

CREATE TABLE Funcao(
	Id_funcao SERIAL PRIMARY KEY,
	Nome_funcao VARCHAR(150)
);

CREATE TABLE Produto(
	Id_produto SERIAL PRIMARY KEY,
	Nome_produto VARCHAR(150)
);

CREATE TABLE Cliente(
	Id_cliente SERIAL PRIMARY KEY,
	Nome_cliente VARCHAR(150),
	Cpf VARCHAR(11),
	Telefone VARCHAR(20),
	Email VARCHAR(150)	
);

CREATE TABLE Funcionario(
	Id_funcionario SERIAL PRIMARY KEY,
	Nome_funcionario VARCHAR(150),
	Id_funcao INT,
	FOREIGN KEY (Id_funcao) REFERENCES Funcao(Id_funcao)
);

CREATE TABLE Pedido(
	Id_pedido SERIAL PRIMARY KEY,
	Id_cliente INT,
	Id_funcionario INT,
	FOREIGN KEY (Id_funcionario) REFERENCES Funcionario(Id_funcionario),
	FOREIGN KEY (Id_cliente) REFERENCES Cliente(Id_cliente)
);

CREATE TABLE Item_compra(
	Id_item_compra SERIAL PRIMARY KEY,
	Id_produto INT,
	Id_pedido INT,
	FOREIGN KEY (Id_pedido) REFERENCES Pedido(Id_pedido),
	FOREIGN KEY (Id_produto) REFERENCES Produto(Id_produto)
);

