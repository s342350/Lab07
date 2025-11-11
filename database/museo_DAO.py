from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO

    def get_all_musei(self):
        """
        Restituisce la lista di tutti i musei presenti nel database.
        """
        conn = ConnessioneDB.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT id, nome, indirizzo
            FROM museo
            ORDER BY nome
        """
        cursor.execute(query)

        result = []
        for row in cursor.fetchall():
            museo = Museo(
                id=row["id"],
                nome=row["nome"],
                indirizzo=row["indirizzo"]
            )
            result.append(museo)

        cursor.close()
        conn.close()
        return result