from flask import Flask, jsonify, request, render_template
from flask_cors import CORS 
import psycopg2

# Configuração do Flask
app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])

# Configuração do banco de dados PostgreSQL
db_config = {
    'dbname': 'humboldt',
    'user': 'humboldt',
    'password': 'humboldt_1234',
    'host': '127.0.0.1',
    'port': '1234'
}

@app.route('/listar', methods=['GET'])
def listar():
    # Conecte-se ao banco de dados
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Execute a consulta SQL
    query = f'select distinct("Nome do aluno / Name des Schülers - der Schülerin"), id FROM testing_new_dados_humboldt order by "Nome do aluno / Name des Schülers - der Schülerin";'
    cursor.execute(query)

    # Obtenha os resultados
    results = cursor.fetchall()

    # Feche a conexão
    cursor.close()
    conn.close()
    
    # Converta os resultados para um formato JSON e retorne
    results = [{"nome": row[0], "id": row[1]} for row in results]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
