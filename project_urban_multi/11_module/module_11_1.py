#библиотека pandas

#1 Чтение данных из CSV-файла
import pandas as pd
df = pd.read_csv('sales_data.csv')
print(df.head())


#2 Выясняем количество продаж за месяц по каждому продукту
# Группировка данных по продуктам и суммирование цены * количества
grouped_df = df.groupby('Product')['Price', 'Quantity'].sum()
# Умножаем цену на количество для получения общей суммы продаж
total_sales = grouped_df['Price'] * grouped_df['Quantity']
# Добавляем новую колонку с общей суммой продаж
grouped_df['Total Sales'] = total_sales
# Выводим результат
print(grouped_df)

#3 Работа с датами и временем
# Преобразование столбца Date в формат даты
df['Date'] = pd.to_datetime(df['Date'])
# Группировка данных по месяцам и суммирование количества
monthly_sales = df.groupby(pd.Grouper(key='Date', freq='M'))['Quantity'].sum()
# Выводим результат
print(monthly_sales)

#библиотека NumPy
#1 Создание массивов
import numpy as np
# Создание одномерного массива
array_1d = np.array([1, 2, 3])
print(array_1d)  # Output: [1 2 3]
# Создание двумерного массива
matrix = np.array([[1, 2], [3, 4]])
print(matrix)  # Output: [[1 2] [3 4]]

#2 математические операции с массивами
a = np.arange(10)  # Массив от 0 до 9
b = np.ones(10)    # Массив из единиц
c = a + b          # Элементарная сумма двух массивов
print(c)           # Output: [1. 2. 3. 4. 5. 6. 7. 8. 9. 10.]
d = np.sqrt(a)     # Извлечение квадратного корня
print(d)           # Output: [0.         1.         1.41421356 ...]

#3 Линейная алгебра
A = np.matrix([[1, 2], [3, 4]])  # Матрица 2x2
B = np.linalg.inv(A)              # Нахождение обратной матрицы
det_A = np.linalg.det(A)          # Нахождение определителя
eig_vals, eig_vecs = np.linalg.eig(A)  # Нахождение собственных значений и векторов

print(B)       # Output: [-2.  1.] [ 1.5 -0.5]
print(det_A)   # Output: -2.0
print(eig_vals)  # Output: [5.37228132 -0.37228132]
print(eig_vecs)  # Собственные вектора


#библиотека Matplotlib
#1 построение простого графика
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)  # Генерация значений X
y = np.sin(x)                     # Функция синус

plt.plot(x, y)                    # Построение графика
plt.xlabel('X')                   # Подпись оси X
plt.ylabel('Sin(X)')              # Подпись оси Y
plt.title('График функции Sinus') # Заголовок графика
plt.grid(True)                    # Отображение сетки
plt.show()                        # Показ графика

#2создание многоосевого и многослойного графика
fig, ax = plt.subplots(nrows=2, ncols=2)  # Создание фигуры с четырьмя осями

ax[0][0].plot(x, np.cos(x))               # График косинуса
ax[0][0].set_title('Cosine')
ax[0][1].scatter(x, np.tan(x))            # Диаграмма рассеяния тангенса
ax[0][1].set_title('Tangent')
ax[1][0].bar(x[:20], np.exp(x[:20]))      # Гистограмма экспоненты
ax[1][0].set_title('Exponential')
ax[1][1].imshow(np.random.randn(50, 50))  # Изображение случайных данных
ax[1][1].set_title('Random Image')
for row in ax:
    for col in row:
        col.set_xlabel('X')
        col.set_ylabel('Y')
fig.suptitle('Multi-plot Example')        # Общий заголовок
fig.tight_layout()                        # Оптимизация расположения графиков
plt.show()

#3 создание интерактивного графика с ползунком
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
# Данные для графика
x = range(10)
y = [i**2 for i in x]
# Создание фигуры и осей
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = ax.plot(x, y, lw=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
# Функция обновления графика при изменении значения ползунка
def update(val):
    order = int(slider.val)
    new_y = [i**order for i in x]
    line.set_ydata(new_y)
    fig.canvas.draw_idle()
# Добавление ползунка для выбора степени
slider_ax = plt.axes([0.15, 0.05, 0.7, 0.03])
slider = Slider(slider_ax, 'Степень', 1, 4, valinit=2, valstep=1)
slider.on_changed(update)
plt.show()