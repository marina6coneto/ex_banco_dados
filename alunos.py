'''1 - Crie uma tabela chamada "alunos" com os seguintes campos:

id (inteiro), nome (texto), idade (inteiro) e curso (texto).'''

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(200));')


''' 2 -Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.'''

#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Marina", 26, "Análise e Desenvolvimento de Sistemas")')
# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Felipe", 23, "Sistemas da Informação")')
# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Luis Fernando", 61, "Engenharia Civil")')
# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Nazareno", 57, "Administração")')
# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Luzia", 60, "Pedagogia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Harry", 11, "Hogwarts")')
# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7,"Amanda", 25, "Engenharia")')
# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(8,"Bernardo", 32, "Engenharia")')
# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(9,"Ariel", 18, "Engenharia")')
# cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(10,"Arnaldo", 58, "Engenharia")')



'''3 - Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
    a) Selecionar todos os registros da tabela "alunos".
    b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
    c) Selecionar os alunos do curso de "Engenharia" em ordem
    alfabética.
    d) Contar o número total de alunos na tabela'''
    
#a)

# registros_alunos = cursor.execute('SELECT * FROM alunos')
# for dados in registros_alunos:
#     print(dados)

#b)

# nome_idade_maior_20 = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20') 
# for dados in nome_idade_maior_20:
#     print(dados)
    
#c)

# alunos_engenharia_ordem_alfabetica = cursor.execute('SELECT * FROM alunos GROUP BY nome HAVING curso="Engenharia"')
# for dados in alunos_engenharia_ordem_alfabetica:
#     print(dados)
    
#d)

# total_alunos = cursor.execute('SELECT COUNT(*) FROM alunos')
# print(total_alunos.fetchone()[0])


'''4. Atualização e Remoção:
    a) Atualize a idade de um aluno específico na tabela.
    b) Remova um aluno pelo seu ID.'''
    
#A)

#cursor.execute('UPDATE alunos SET idade = 12 WHERE nome = "Harry"')

#B)

#cursor.execute('DELETE FROM alunos where id = 10')

conexao.commit()
conexao.close()
