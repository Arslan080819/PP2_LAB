import psycopg2
from config import DB_CONFIG

class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
            print("✅ Connected to PostgreSQL")
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            raise
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("🔌 Connection closed")
    
    def commit(self):
        if self.conn:
            self.conn.commit()
    
    def rollback(self):
        if self.conn:
            self.conn.rollback()
    
    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor
        except Exception as e:
            print(f"❌ Query failed: {e}")
            self.rollback()
            raise