from src.db_connection import conectar  

def listar_consultas():
    conn = conectar()  
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    id,
                    id_pacientes,  # ← 3. Coluna correta: id_pacientes (não id_medico)
                    id_medicos,    # ← 4. Coluna correta: id_medicos
                    DATE_FORMAT(data_consulta, '%Y-%m-%d') as data_consulta,  # ← 5. Nome correto da coluna
                    TIME_FORMAT(hora_consulta, '%H:%i:%s') as hora_consulta,  # ← 6. Nome correto da coluna
                    Observacoes,
                    status
                FROM consultas
            """)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar consultas: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    return []