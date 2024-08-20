import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

'''5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela.'''

cursor.execute('CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INT, saldo FLOAT)')
# cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES("Marina",26,1500.56)')
# cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES("Felipe",23,1856.74)')
# cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES("Harry",11,15848795.95)')
# cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES("Hermione",11,415846)')
# cursor.execute('INSERT INTO clientes(nome, idade, saldo) VALUES("Rony",11,1545.84)')


'''6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecione o nome e a idade dos clientes com idade superior a
20 anos.
b) Calcule o saldo médio dos clientes.
c) Encontre o cliente com o saldo máximo.
d) Conte quantos clientes têm saldo acima de 10000.'''

idade_maior_20 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 20')
for i in idade_maior_20:
    print(i)
    
saldo_medio = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
for i in saldo_medio:
    print(i)
    
saldo_maximo = cursor.execute('SELECT nome, idade, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
for i in saldo_maximo:
    print(i)
    
n_clientes_maior_10000 = cursor.execute('SELECT COUNT(*) AS clientes_acima_10000 FROM clientes WHERE saldo > 10000')
for i in n_clientes_maior_10000:
    print(i)
    
'''
7. Atualização e Remoção com Condições
a) Atualize o saldo de um cliente específico.
b) Remova um cliente pelo seu ID.'''

#cursor.execute('UPDATE clientes SET saldo=10000 WHERE nome="Rony"')

#cursor.execute('DELETE FROM clientes WHERE id=2')


'''8. Junção de Tabelas
Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). Insira algumas
compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra.'''

cursor.execute('CREATE TABLE IF NOT EXISTS compras(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INT, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(1,"Notebook", 4200)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(3,"Varinha", 45)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(3,"Caldeirão", 60)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(4,"A História da Magia", 50)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(5,"Feijõeszinhos de Todos os Sabores", 15)')
# cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES(5,"Sapo de Chocolate", 10)')

conexao.commit()
conexao.close()
