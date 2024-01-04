class Language:
    def __init__(self, conn, cursor):
        self.conn  = conn
        self.cursor = cursor