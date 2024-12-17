import sqlite3

# Создаем подключение к базе данных
connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()

# Удаление таблицы Users
cursor.execute('''DROP TABLE IF EXISTS Users''')
connect.commit()

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

# cursor.execute("CREATE INDEX IF NOT EXISTS idx_emal ON USERS (email)")
for i in range(1, 11):
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?,?,?,?)
    ''', (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

# Обновляем баланс у каждой второй записи начиная с первой
for i in range(1, 11, 2):
    cursor.execute('''
        UPDATE Users
        SET balance = 500
        WHERE id = ?
    ''', (i,))

# Удаляем каждую третью запись начиная с первой
for i in range(1, 11, 3):
    cursor.execute('''
        DELETE FROM Users
        WHERE id = ?
    ''', (i,))

# Выполняем выборку всех записей, кроме тех, у кого возраст равен 60
cursor.execute('''
    SELECT username, email, age, balance
    FROM Users
    WHERE age != 60
''')

# Получаем все строки результата
rows = cursor.fetchall()
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

connect.commit()
cursor.close()
connect.close()