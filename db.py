import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute ("CREATE TABLE IF NOT EXISTS parts (id INTERGER PRIMARY KEY, 班级 text, 课室编号 text, 日期 text, 时间 text, 报备事项 text)")
        self.conn.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, 班级, 课室编号, 日期, 时间, 报备事项):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?, ?,)", (班级, 课室编号, 日期, 时间, 报备事项))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()
    
    def update(self, id, 班级, 课室编号, 日期, 时间, 报备事项):
        self.cur.execute("UPDATE parts SET 班级 = ?, 课室编号 = ?, 日期 = ?, 时间 = ?, 报备事项 = ? WHERE id = ?", (班级, 课室编号, 日期, 时间, 报备事项, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('reports.db')
db.insert("J3D","D210","20/1/2020","5:23pm","Fan Exploded")
