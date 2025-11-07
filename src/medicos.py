from src.db_connection import conectar

def listar_medicos():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM medicos")
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar médicos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    return []

def criar_medico(nome, crm, id_especializacao, telefone_emergencia):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO medicos (nome, crm, id_especializacao, telefone_emergencia)
                VALUES (%s, %s, %s, %s)
                """,
                (nome, crm, id_especializacao, telefone_emergencia)
            )
            conn.commit()
            return cursor.lastrowid  
        except Exception as e:
            print(f"Erro ao cadastrar médico: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            conn.close()
    return None