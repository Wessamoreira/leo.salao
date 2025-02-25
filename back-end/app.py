from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)

# Conexão com o banco de dados
def conectar_banco():
    return sqlite3.connect("database.db")

# Criando tabelas se não existirem
def criar_tabelas():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS promocoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            desconto REAL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            aprovado BOOLEAN DEFAULT 0
        )
        """)
        conn.commit()

# Rota para visualizar serviços
@app.route("/api/servicos", methods=["GET"])
def listar_servicos():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM servicos")
        servicos = cursor.fetchall()
    return jsonify(servicos)

# Rota para adicionar um novo serviço
@app.route("/api/servicos", methods=["POST"])
def adicionar_servico():
    data = request.json
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO servicos (nome, descricao, preco) VALUES (?, ?, ?)", 
                       (data["nome"], data["descricao"], data["preco"]))
        conn.commit()
    return jsonify({"message": "Serviço adicionado com sucesso!"}), 201

# Rota para listar promoções
@app.route("/api/promocoes", methods=["GET"])
def listar_promocoes():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM promocoes")
        promocoes = cursor.fetchall()
    return jsonify(promocoes)

# Rota para adicionar uma promoção
@app.route("/api/promocoes", methods=["POST"])
def adicionar_promocao():
    data = request.json
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO promocoes (nome, descricao, desconto) VALUES (?, ?, ?)", 
                       (data["nome"], data["descricao"], data["desconto"]))
        conn.commit()
    return jsonify({"message": "Promoção adicionada com sucesso!"}), 201

# Rota para cadastro de funcionários (aguardando aprovação)
@app.route("/api/funcionarios", methods=["POST"])
def cadastrar_funcionario():
    data = request.json
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO funcionarios (nome, email, senha) VALUES (?, ?, ?)", 
                       (data["nome"], data["email"], data["senha"]))
        conn.commit()
    return jsonify({"message": "Cadastro enviado para aprovação!"}), 201

# Rota de login do administrador
@app.route("/api/admin/login", methods=["POST"])
def login_admin():
    data = request.json
    email_padrao = "wessleysanttos@icloud.com"
    senha_padrao = "wesley12345"
    if data["email"] == email_padrao and data["senha"] == senha_padrao:
        return jsonify({"message": "Login bem-sucedido!", "auth": True}), 200
    return jsonify({"message": "Credenciais inválidas!"}), 401

@app.route("/api/agendamentos", methods=["POST"])
def criar_agendamento():
    data = request.json
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO agendamentos (cliente_nome, cliente_telefone, servico_id, funcionario_id, data, horario) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (data["cliente_nome"], data["cliente_telefone"], data["servico_id"], data["funcionario_id"], data["data"], data["horario"]))
        conn.commit()
    return jsonify({"message": "Agendamento realizado com sucesso!"}), 201

@app.route("/api/agendamentos", methods=["GET"])
def listar_agendamentos():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT agendamentos.id, agendamentos.cliente_nome, agendamentos.cliente_telefone, 
                   servicos.nome AS servico, funcionarios.nome AS funcionario, 
                   agendamentos.data, agendamentos.horario, agendamentos.status
            FROM agendamentos
            JOIN servicos ON agendamentos.servico_id = servicos.id
            JOIN funcionarios ON agendamentos.funcionario_id = funcionarios.id
        """)
        agendamentos = cursor.fetchall()
    return jsonify(agendamentos)

# Inicializando o banco na primeira execução
if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)
