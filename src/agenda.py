from src.db_connection import conectar  
def listar_agenda():
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    id,
                    id_medico,
                    DATE_FORMAT(data, '%%Y-%%m-%%d') as data,
                    TIME_FORMAT(hora, '%%H:%%i:%%s') as hora,
                    status
                FROM agenda
            """)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Erro ao listar agenda: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    return []