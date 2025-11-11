from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_artefatti(self):
        """
        Restituisce tutti gli artefatti presenti nel database.
        """
        conn = ConnessioneDB.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT a.id AS id,
                   a.nome AS nome,
                   a.tipologia AS tipologia,
                   a.epoca AS epoca,
                   a.id_museo AS id_museo
            FROM artefatto a
            ORDER BY a.nome
        """
        cursor.execute(query)

        result = []
        for row in cursor.fetchall():
            artefatto = Artefatto(
                id=row["id"],
                nome=row["nome"],
                tipologia=row["tipologia"],
                epoca=row["epoca"],
                id_museo=row["id_museo"]
            )
            result.append(artefatto)

        cursor.close()
        conn.close()
        return result

    def get_artefatti_filtrati(self, museo_nome=None, epoca=None):
        """
        Restituisce gli artefatti filtrati per museo e/o epoca.
        Se uno dei parametri è None, non viene applicato quel filtro.
        """
        conn = ConnessioneDB.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT a.id AS id,
                   a.nome AS nome,
                   a.tipologia AS tipologia,
                   a.epoca AS epoca,
                   a.id_museo AS id_museo,
                   m.nome AS museo_nome
            FROM artefatto a
            JOIN museo m ON a.id_museo = m.id
            WHERE (%s IS NULL OR m.nome = %s)
              AND (%s IS NULL OR a.epoca = %s)
            ORDER BY m.nome, a.nome
        """

        cursor.execute(query, (museo_nome, museo_nome, epoca, epoca))

        result = []
        for row in cursor.fetchall():
            artefatto = Artefatto(
                id=row["id"],
                nome=row["nome"],
                tipologia=row["tipologia"],
                epoca=row["epoca"],
                id_museo=row["id_museo"]
            )
            result.append(artefatto)

        cursor.close()
        conn.close()
        return result