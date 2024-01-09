class RssLink:
    def __init__(self, conn, cursor):
        self.conn  = conn
        self.cursor = cursor
        self.table = "rss_links"
    
    def create(self,rss,language_id, category_id):
        sql = f"INSERT INTO {self.table}(rss_link,category_id,language_id) VALUES(?,?,?)"
        self.cursor.execute(sql,(rss, language_id, category_id))
        self.conn.commit()
    

    def update(self,rss, language_id, category_id,id):
        sql = f"UPDATE {self.table} SET rss_link=?, category_id=?,language_id=? WHERE id=?"
        self.cursor.execute(sql,(rss, language_id, category_id))
        self.conn.commit()
        

    def delete(self , id):
        sql = f"DELETE FROM {self.table} WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()

    def get_all(self):
        sql = f"SELECT * FROM {self.table}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_one_by_id(self,id):
        sql = f"SELECT * FROM {self.table} WHERE id=?"
        self.cursor(sql,(id,))
        return self.cursor.fetchall()
        

