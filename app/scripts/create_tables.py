from sqlalchemy import create_engine
from sqlalchemy.schema import CreateTable

from app.models import User, Task, Base


# Создаем движок для подключения к базе данных
engine = create_engine('sqlite:///taskmanager.db', echo=True)

# Генерируем SQL-запросы для создания таблиц
user_create_table = CreateTable(User.__table__)
task_create_table = CreateTable(Task.__table__)

# Выводим SQL-запросы в консоль
print(user_create_table.compile(engine))
print(task_create_table.compile(engine))

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)