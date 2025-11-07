from src.db_connection import conectar

def listar_pacientes():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)  
            cursor.execute("SELECT * FROM pacientes")
            resultados = cursor.fetchall()  
            return resultados  
        except Exception as e:
            print(f"Erro ao listar pacientes: {e}")
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()
            conn.close()
    return []

def criar_paciente(nome, sobrenome, cpf, data_nascimento, telefone, email):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO pacientes (nome, sobrenome, cpf, data_nascimento, telefone, email)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (nome, sobrenome, cpf, data_nascimento, telefone, email)
            )
            conn.commit()
            return cursor.lastrowid  
        except Exception as e:
            print(f"Erro ao cadastrar paciente: {e}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            conn.close()
    return None