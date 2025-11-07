from src.db_connection import conectar

def listar_pagamentos():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM pagamentos")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar pagamentos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    return []

def criar_pagamento(id_consulta, valor, forma_pagamento, status):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO pagamentos (id_consulta, valor, forma_pagamento, status)
                VALUES (%s, %s, %s, %s)
                """,
                (id_consulta, valor, forma_pagamento, status)
            )
            conn.commit()
            return cursor.lastrowid 
        except Exception as e:
            print(f"Erro ao cadastrar pagamento: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            conn.close()
    return None