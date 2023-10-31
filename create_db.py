import sqlite3

def create_connection(db_file):

        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)

        return conn
    



conn= create_connection("file2.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS simulations (
            sim_id integer PRIMARY KEY AUTOINCREMENT,
            date text);""")

c.execute("""CREATE TABLE IF NOT EXISTS iterations (
            sim_id integer NOT NULL,
            step integer NOT NULL,
            num_workers integer,
            num_products integer,
            num_food integer,
            FOREIGN KEY (sim_id) REFERENCES projects (sim_id))""")