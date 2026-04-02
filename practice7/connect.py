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
def create_table():
    db = DatabaseConnection()
    db.connect()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        surname VARCHAR(100),
        phone VARCHAR(20) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE INDEX IF NOT EXISTS idx_contacts_name ON contacts(name);
    CREATE INDEX IF NOT EXISTS idx_contacts_phone ON contacts(phone);
    """
    
    try:
        db.execute_query(create_table_query)
        db.commit()
        print("✅ Table ready")
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.disconnect()
def get_connection():
    return psycopg2.connect(**DB_CONFIG)