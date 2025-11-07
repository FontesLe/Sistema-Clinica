from src.db_connection import conectar

def listar_especializacoes():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM especializacao")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar especializações: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    return []