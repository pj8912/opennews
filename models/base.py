class BaseModel:
    def __init__(self, connection):
        self.connection = connection

    def create(self, data):
        raise NotImplementedError

    def read_one(self):
        raise NotImplementedError

    def read_all(self, item_id):
        raise NotImplementedError

    def update(self, item_id, data):
        raise NotImplementedError

    def delete(self, item_id):
        raise NotImplementedError