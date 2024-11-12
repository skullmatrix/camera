import sqlite3
from typing import Any, Dict, List

DATABASE = 'student.db'

def connect_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE)
    return conn

def create_table() -> None:
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idno TEXT NOT NULL,
                lastname TEXT NOT NULL,
                firstname TEXT NOT NULL,
                course TEXT NOT NULL,
                level TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_record(table: str, **kwargs: Any) -> bool:
    columns = ', '.join(kwargs.keys())
    placeholders = ', '.join('?' for _ in kwargs)
    values = tuple(kwargs.values())
    
    sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
    
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Error adding record: {e}")
        return False

def getall_records(table: str) -> List[Dict[str, Any]]:
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()
        return [
            {column[0]: row[idx] for idx, column in enumerate(cursor.description)}
            for row in rows
        ]


create_table()
