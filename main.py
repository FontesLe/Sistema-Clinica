import sys
import os
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.pacientes import listar_pacientes
from src.medicos import listar_medicos
from src.consultas import listar_consultas
from src.convenios import listar_convenios
from src.especializacao import listar_especializacoes
from src.usuarios import listar_usuarios
from src.pagamentos import listar_pagamentos
from src.agenda import listar_agenda
from src.pacientes import criar_paciente
from src.medicos import criar_medico
from src.pagamentos import criar_pagamento

@app.route('/pacientes', methods=['POST'])
def criar_novo_paciente():
    try:
        dados = request.get_json()
        resultado = criar_paciente(
            nome=dados['nome'],
            sobrenome=dados['sobrenome'],
            cpf=dados['cpf'],
            data_nascimento=dados['data_nascimento'],
            telefone=dados['telefone'],
            email=dados['email']
        )
        return jsonify({"mensagem": "Paciente criado com sucesso!", "id": resultado}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/medicos', methods=['POST'])
def criar_novo_medico():
    try:
        dados = request.get_json()
        resultado = criar_medico(
            nome=dados['nome'],
            crm=dados['crm'],
            id_especializacao=dados['id_especializacao'],
            telefone_emergencia=dados['telefone_emergencia']
        )
        return jsonify({"mensagem": "Médico criado com sucesso!", "id": resultado}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/pagamentos', methods=['POST'])
def criar_novo_pagamento():
    try:
        dados = request.get_json()
        resultado = criar_pagamento(
            id_consulta=dados['id_consulta'],
            valor=dados['valor'],
            forma_pagamento=dados['forma_pagamento'],
            status=dados['status']
        )
        return jsonify({"mensagem": "Pagamento criado com sucesso!", "id": resultado}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    try:
        pacientes = listar_pacientes()
        return jsonify(pacientes)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/medicos', methods=['GET'])
def get_medicos():
    try:
        medicos = listar_medicos()
        return jsonify(medicos)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/consultas', methods=['GET'])
def get_consultas():
    try:
        consultas = listar_consultas()
        return jsonify(consultas)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/especializacoes', methods=['GET'])
def get_especializacoes():
    try:
        especializacoes = listar_especializacoes()
        return jsonify(especializacoes)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        usuarios = listar_usuarios()
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/convenios', methods=['GET'])
def get_convenios():
    try:
        convenios = listar_convenios()
        return jsonify(convenios)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/pagamentos', methods=['GET'])
def get_pagamentos():
    try:
        pagamentos = listar_pagamentos()
        return jsonify(pagamentos)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/agenda', methods=['GET'])
def get_agenda():
    try:
        agenda = listar_agenda()
        return jsonify(agenda)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5801)