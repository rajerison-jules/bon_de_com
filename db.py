import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS produits (id INTEGER PRIMARY KEY, produit text, client text, magasin text, prix text )")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM produits")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self,produit,client,magasin,prix):
        self.cur.execute("INSERT INTO produits VALUES (NULL, ?, ?, ?, ?)",(produit,client,magasin,prix))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM produits WHERE id=?", (id,))
        self.conn.commit()
    
    def update(self, id, produit, client, magasin, prix):
        self.cur.execute("UPDATE produits SET produit = ?, client = ?, magasin = ?, prix = ? WHERE id = ?", (produit,client,magasin,prix,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close() 
"""
bd = Database('store.db')
bd.insert("chapeau rouge","ferdinand eliot","hat center","30")
bd.insert("carton de bonbon","clarisse feng","candy shop","100")
bd.insert("ordinateur ASUS","Léon paul","PCUP","500")
bd.insert("lunnette de soleil","soulia nilia","optica","50")
"""
