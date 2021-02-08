https://stackoverflow.com/questions/64840826/pgadmin-4-v4-28-keeps-loading
https://www.devmedia.com.br/manipulacao-de-erros-em-pl-pgsql/7280
https://www.postgresql-archive.org/Tratar-erro-em-transaction-td2040839.html#a2040841


- Existem 4 FN

- Registro, tupla e linha são a mesma coisa. 
- Registro é um conjunto de atributos que acaba formando uma linha, uma composição de atributos.
- BD - é um repositório de dados, gerenciado pelo SGBD

- Data Manipulation Language (DML)
    - consultas e modificações nas tabelas do bd
    - SELECT, INSERT, UPDATE, DELETE, MERGE, BULK INSET
    - o SELECT pode ser considerado um DQL (Data Query Language) - Categoria para realizar a leitura de dados (tabelas, views e etc)

- Data Definiton Language (DDL)
    - instruções usadas para criar e modificar as estruturas dos objetos no BD
    - ALTER, CREATE, DROP, DISABLE TRIGGER, ENABLE TRIGGER, TRUNCATE TABLE, UPDATE TABLE

- Data Control Language (DCL) - comandos para controle de acesso e gerenciamento de permissões para usuários no BD
    -  GRANT, REVOKE, DENY

- Transactional Control Language (TCL) - comandos usados para gerenciar as mudanças feitas por instruções DML
    - COMMIT, ROLLBACK
