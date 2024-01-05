from base import BaseModel

class Category(BaseModel):
    def __init__(self, conn, cursor):
        self.conn  = conn
        self.cursor = cursor


    def create(self,category_name):
        sql = "INSERT INTO categories(category_name) VALUES(?)"
        self.cursor.execute(sql, (category_name,))
        self.conn.commit()


    def delete(self, id):
        sql = "DELETE FROM categories WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
    
    def update(self,id,name):
        sql = "UPDATE catgeories SET category_name=? WHERE id=?"
        self.cursor.execute(sql, (name,id))
        self.conn.commit()

    def read_one(self,id):
        sql = "SELECT * FROM categories WHERE id=?"
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchall()
        return result
    
    def read_all(self):
        sql ="SELECT * FROM catgeories ORDER updated_at DESC"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    