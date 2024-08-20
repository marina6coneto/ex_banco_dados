# Bootcamp Back-End Python e Django Exercícios Banco de Dados (WOMAKERS CODE)

Este repositório contém exercícios práticos relacionados à criação e manipulação de bancos de dados utilizando SQL. Aqui, explorei conceitos de criação de tabelas, inserção de dados, junções de tabelas, e funções agregadas.

## Estrutura dos Exercícios

### 1. Criar Tabela e Inserir Dados
Criei uma tabela chamada `clientes` com os campos `id`, `nome`, `idade`, e `saldo`, e inserimos alguns registros de clientes.

### 2. Consultas SQL e Funções Agregadas
Realizamos consultas para:
- Selecionar clientes com idade superior a 20 anos.
- Calcular o saldo médio dos clientes.
- Encontrar o cliente com o maior saldo.
- Contar quantos clientes têm saldo acima de 10.000.

### 3. Junção de Tabelas
Criamos uma segunda tabela chamada `compras`, associada à tabela `clientes` através de uma chave estrangeira. A tabela `compras` inclui os campos `cliente_id`, `produto`, e `valor`. A junção das duas tabelas exibe o nome do cliente, o produto adquirido, e o valor da compra.

## Tecnologias Utilizadas

- **SQL**: Structured Query Language para manipulação dos dados.
- **SQLite**: Banco de dados relacional leve utilizado nos exercícios.
- **Python**: Linguagem de programação utilizada para realizar operações no banco de dados.
- **DBeaver**: Ferramenta gráfica de administração de banco de dados (SGBD) utilizada para gerenciar o SQLite.


