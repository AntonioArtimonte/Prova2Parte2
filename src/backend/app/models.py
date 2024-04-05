from tinydb import TinyDB, Query
import time


class Database:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
        
    def insert_onlytime(self):
        return self.db.insert({'timestamp': time.asctime()})
    
    def insert(self, data):
        return self.db.insert({'mensagem': data, 'timestamp': time.asctime()})
        
    def get_all_data(self):
        return self.db.all()