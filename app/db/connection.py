import sqlite3

def get_connection():
    conn = sqlite3.connect('items.db')
    return conn