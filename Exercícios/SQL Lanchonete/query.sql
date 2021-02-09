SELECT 	Funcionario.Nome_funcionario, 
		Funcao.Nome_funcao, 
		Pedido.Id_pedido,
		Cliente.Nome_cliente,
		Produto.Nome_produto
FROM Funcionario
INNER JOIN Funcao
ON Funcionario.Id_funcao = Funcao.Id_funcao
INNER JOIN Pedido
ON Funcionario.Id_funcionario = Pedido.Id_funcionario
INNER JOIN Cliente
ON Pedido.Id_cliente = Cliente.Id_cliente
INNER JOIN Item_compra
ON Item_compra.Id_pedido = Pedido.Id_pedido
INNER JOIN Produto
ON Item_compra.Id_produto = Produto.Id_produto
WHERE Cliente.Nome_cliente = 'Mary'
AND Pedido.Id_pedido = 1;




