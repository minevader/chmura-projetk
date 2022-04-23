from os import name
from typing import Text
import pypyodbc
import azurecred


class AzureDB:
    dsn='DRIVER='+azurecred.AZDBDRIVER+';SERVER='+azurecred.AZDBSERVER+';PORT=1433;DATABASE='+azurecred.AZDBNAME+';UID='+azurecred.AZDBUSER+';PWD='+azurecred.AZDBPW


    def __init__(self):
        self.conn = pypyodbc.connect(self.dsn)
        self.cursor = self.conn.cursor()


    def finalize(self):
        if self.conn:
            self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finalize()

    def __enter__(self):
        return self


    def azureGetData(self):
        try:
            self.cursor.execute("SELECT name,text, data_wpisu from data")
            data = self.cursor.fetchall()
            return data
        except pypyodbc.DatabaseError as exception:
            print('Failed to execute query')
            print(exception)
            exit(1)

    def azureAddData(self, name_, comment):
        self.cursor.execute(
            f"INSERT into guestbook (name, text,data_wpisu ) values ('{name_}', '{text}',{data_wpisu})")
        self.conn.commit()

# zakomentowana funkcja dodająca do bazy
# zakomentowana funkcjausuwająca rekord z bazy gdziename== Adam
# def azureDeleteData(self):
# self.cursor.execute("DELETE FROM data WHERE name = 'Adam'")
# self.conn.commit()