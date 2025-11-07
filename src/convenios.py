from src.db_connection import conectar

def listar_convenios():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM convenios")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar convênios: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    return []