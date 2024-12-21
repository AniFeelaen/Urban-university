import sqlite3
import random

# Создаем подключение к базе данных
def initiate_db():
    connect = sqlite3.connect('Urban-university/module_14/products.db')
    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    connect.commit
    connect.close
def add_product(title, description, price):
    with sqlite3.connect('Urban-university/module_14/products.db') as conn:
        cursor = conn.cursor()
        
        # Добавление нового продукта
        cursor.execute('''
            INSERT INTO Products (title, description, price)
            VALUES (?, ?, ?)
        ''', (title, description, price))
        conn.commit()
        
def get_all_products():
    connect = sqlite3.connect('Urban-university/module_14/products.db')
    cursor = connect.cursor()
    
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    
    connect.close()
    return products    
