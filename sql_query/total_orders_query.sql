/*
Consulta para retornar os id's dos clientes que possuem um total
de pedidos maior do que 5
*/
SELECT client_id, COUNT(*) AS total_orders
FROM Orders
GROUP BY client_id
HAVING COUNT(*) > 5;