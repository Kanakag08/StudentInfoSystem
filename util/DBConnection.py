
import mysql.connector as sql
# Database connectivity
class DBConnection:
    def open(conn):
        try:
            conn = sql.connect(host="localhost", database="SIS", user="root", password="Kagrawal@08")
            stmt = conn.cursor()
            return conn, stmt
        except Exception as E:
            print(f"Database cannot connect: {E}")
            return None, None

    def close(conn):
        if conn:
            conn.close()