from src.db_connection import conectar

def listar_usuarios():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    return []