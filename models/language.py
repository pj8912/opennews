class Language:
    def __init__(self, conn, cursor):
        self.conn  = conn
        self.cursor = cursor


    def create(self,category_name):
        sql = "INSERT INTO languages(language_name) VALUES(?)"
        self.cursor.execute(sql, (category_name,))
        self.conn.commit()


    def delete(self, id):
        sql = "DELETE FROM languages WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
    
    def update(self,id,name):
        sql = "UPDATE languages SET language_name=? WHERE id=?"
        self.cursor.execute(sql, (name,id))
        self.conn.commit()

    def read_one(self,id):
        sql = "SELECT * FROM languages WHERE id=?"
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchall()
        return result
    
    def read_all(self):
        sql ="SELECT * FROM languages ORDER updated_at DESC"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

