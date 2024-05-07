import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS BILLS(id INTEGER PRIMARY KEY, bill TEXT, ammount TEXT, notes TEXT, date TEXT)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM BILLS")
        rows = self.cur.fetchall()
        return rows 

    def insert(self, bill, ammount, notes, date):
        self.cur.execute("INSERT INTO BILLS VALUES(NULL,?,?,?,?)", (bill, ammount, notes, date))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM BILLS WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, bill, ammount, notes, date):
        self.cur.execute("UPDATE BILLS SET bill=?, ammount=?, notes=?, date=? WHERE id=?", (bill, ammount, notes, date, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('store.db')

