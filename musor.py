# Обновляем баланс у каждой второй записи начиная с первой
for i in range (1, 11, 2):
    cursor.execute('''
    UPDATE Users
    SET balance = 500
''')
# WHERE id % 2 == 1

# Удаляем каждую третью запись начиная с первой
for i in range (1, 11 3):
    cursor.execute('''
    DELETE FROM Users 
''')
#  WHERE id % 3 == 1
# Выполняем выборку всех записей, кроме тех, у кого возраст равен 60
cursor.execute('''
SELECT username, email, age, balance
FROM Users
WHERE age != 60
''')

# Получаем все строки результата
rows = cursor.fetchall()

# Выводим результат в нужном формате
for row in rows:
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

# Закрываем соединение с базой данных
connect.commit()
cursor.close()
connect.close()
