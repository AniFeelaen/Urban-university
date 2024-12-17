import sqlite3

# Создаем подключение к базе данных
connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()

# Создаем таблицу Users, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')
for i in range (10): 
        cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?,?,?,?)''', (f"User{i}", f"example{i*10}@gmail.com", f"{i}", "1000") 
 
)
connect.commit()
connect.close()

