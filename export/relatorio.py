import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os

try:
    load_dotenv()  # carrega variáveis do .env

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    print("Conexão bem-sucedida!")
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
    exit()

query = "SELECT * FROM consultas;"  

try:
    df = pd.read_sql(query, connection)
    print("Dados carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    exit()

try:
    df.to_excel("relatorios.xlsx", index=False)  
    print("Relatório exportado para relatorios.xlsx com sucesso!")
except Exception as e:
    print(f"Erro ao exportar o relatório: {e}")

connection.close()
print("Conexão com o MySQL encerrada.")
