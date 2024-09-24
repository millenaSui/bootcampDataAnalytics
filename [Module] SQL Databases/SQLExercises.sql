--- SQL Puro ---
-- 1. Crie uma tabela chamada "alunos" com os seguintes campos: 
--    id (inteiro), nome (texto), idade (inteiro) e curso (texto).
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    curso TEXT
);

-- 2. Insira pelo menos 5 registros na tabela
INSERT INTO alunos (id, nome, idade, curso) VALUES 
(1, 'Mauricio', 32, 'Engenharia'),
(2, 'Vivian', 20, 'Odontologia'),
(3, 'Joel', 25, 'Medicina Veterinária'),
(4, 'Luana', 29, 'Design'),
(5, 'Fernanda', 18, 'Engenharia');

-- 3. Consultas Básicas 
--    (Escreva consultas SQL para realizar as seguintes tarefas:)
--    a. Selecionar todos os registros da tabela "alunos".
SELECT * FROM alunos;
--    b. Selecionar o nome e a idade dos alunos com mais de 20 anos.
SELECT nome, idade FROM alunos WHERE idade > 20;
--    c. Selecionar alunos de "Engenharia" em ordem alfabética.
SELECT nome FROM alunos WHERE curso = 'Engenharia' ORDER BY nome;
--    d. Contar o número total de alunos na tabela.
SELECT COUNT(*) FROM alunos;

-- 4. Atualização e Remoção
--    a. Atualize a idade de um aluno específico na tabela.
UPDATE alunos SET idade = 17 WHERE nome = 'Fernanda';
--    b. Remova um aluno pelo seu ID.
DELETE FROM alunos WHERE id = 5;

-- 5. Criar uma Tabela e Inserir Dados
--    Crie uma tabela chamada "clientes" com os campos: 
--    id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    saldo FLOAT
);

--    Insira alguns registros de clientes na tabela.
INSERT INTO clientes (id, nome, idade, saldo) VALUES 
(1, 'Juliano', 20, 1380.00),
(2, 'Marcela', 31, 103.75),
(3, 'Danilo', 36, 2900.39),
(4, 'Fabiana', 22, 1410.23);

-- 6. Consultas e Funções agregadas 
--    (Escreva consultas SQL para realizar as seguintes tarefas:)
--    a. Selecione o nome e a idade dos clientes com idade superior a 30 anos.
SELECT nome, idade FROM clientes WHERE idade > 30;
--    b. Calcule o saldo médio dos clientes.
SELECT AVG(saldo) FROM clientes;
--    c. Encontre o cliente com o saldo máximo.
SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1;
--    d. Conte quantos clientes têm saldo acima de 1000.
SELECT COUNT(*) FROM clientes WHERE saldo > 1000;

-- 7. Atualização e Remoção com Condições
--    a. Atualize o saldo de um cliente específico.
UPDATE clientes SET saldo = 1950.00 WHERE idade = 20;
--    b. Remova um cliente pelo seu ID.
DELETE FROM clientes WHERE id = 1;

-- 8. Junção de Tabelas
--    Crie uma segunda tabela chamada "compras" com os campos: 
--    id (chave primária), cliente_id (chave estrangeira referenciando 
--    o id da tabela "clientes"), produto (texto) e valor (real). 
CREATE TABLE compras (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto TEXT,
    valor FLOAT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
--    Insira algumas compras associadas a clientes existentes na 
--    tabela "clientes". 
INSERT INTO compras (id, cliente_id, produto, valor) VALUES 
(1, 4, 'Livro', 57.10),
(2, 3, 'Tablet', 1680.00),
(3, 2, 'Salgado', 9.99);
--    Escreva uma consulta para exibir o nome do cliente, o 
--    produto e o valor de cada compra.
SELECT clientes.nome, compras.produto, compras.valor
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id;
