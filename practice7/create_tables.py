from connect import DatabaseConnection

def create_tables():
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
        print("✅ Table 'contacts' created successfully")
    except Exception as e:
        print(f"❌ Error creating table: {e}")
        db.rollback()
    finally:
        db.disconnect()

if __name__ == "__main__":
    create_tables()