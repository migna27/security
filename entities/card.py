from secutiry.crypto import encrypt, decrypt
from persistence.db import get_connection


class Card:
    def __init__(self, id, number, type, id_usuario, Banco):
        self.id = id
        self.number = number
        self.type = type
        self.id_usuario = id_usuario
        self.Banco = Banco


    def card_insert(number, type, id_usuario, Banco):
        connection = get_connection()
        cursor = connection.cursor()
        number_encrypt = encrypt(number)
        sql = "INSERT INTO card(number, type, id_usuario, Banco) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (number_encrypt, type, id_usuario, Banco))
        connection.commit()
        cursor.close()
        connection.close()
    

    def get_cards_by_user_id(id_usuario):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT id, number, type, id_usuario, Banco FROM card WHERE id_usuario = %s"
        cursor.execute(sql, (id_usuario,))
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return [
            Card(
                id=row["id"],
                number=decrypt(row["number"]),
                type=row["type"],
                id_usuario=row["id_usuario"],
                Banco=row["Banco"]

            )
            for row in rows
        ]
    