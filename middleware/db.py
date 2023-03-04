import psycopg2
from common.preferences import HOSH_DB, USER_DB, PASSWORD_DB, DB_NAME

'''lWglL6Pisq7TCIzsDAjD'''
class DB:
    def __init__(self) -> None:
        try:
    # connect to exist database
            self.connection = psycopg2.connect(
                host=HOSH_DB,
                user=USER_DB,
                password=PASSWORD_DB,
                database=DB_NAME    
            )
            self.connection.autocommit = True
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)


    def create_db(self):
    
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id          serial PRIMARY KEY,    
                    login       varchar(40) UNIQUE NOT NULL,
                    passw       varchar(40) NOT NULL,
                    mail        varchar(100) UNIQUE NOT NULL,
                    mail_status varchar(30) NOT NULL,
                    created_at  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS posts (
                    id          serial PRIMARY KEY,    
                    login       varchar(40) NOT NULL,
                    description TEXT NOT NULL,
                    body        TEXT NOT NULL,
                    label       TEXT,
                    doc         TEXT,
                    status      INTEGER DEFAULT 0,
                    created_at  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS answ (
                    id          serial PRIMARY KEY,
                    id_post     serial NOT NULL,
                    id_answ     serial,
                    statis      serial NOT NULL,
                    login       varchar(40) NOT NULL,
                    body        TEXT NOT NULL,
                    doc         TEXT,
                    status      INTEGER DEFAULT 0,
                    created_at  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
    """)
    
            # connection.commit()
            print("[INFO] Table created successfully")
    
    def write(self, table, param, values):
        with self.connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO {table} ({param}) VALUES ({values});""")
            return 1
        return 0

    def read(self, table, param):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""SELECT {param} FROM {table}""")
                return cursor.fetchall()
        except:
            return 0
    
    def read_one(self, table, param, values):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"""SELECT {param} FROM {table} WHERE {values}""")
                return cursor.fetchone()
        except:
            return 0

    def delete(self, table, column, values):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM {table} WHERE {column} = '{values}'")
                return 1
        except:
            return 0

    def close(self):
        self.connection.close()
        print("[INFO] PostgreSQL connection closed")

    
if __name__ == '__main__':
    db = DB()
    db.create_db()