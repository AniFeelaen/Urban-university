#создаем функцию с н строками и м количеством элементов в каждой и значениями валуе, пустую матрицу
def get_matrix (n, m, value):
    matrix = []
    #внутренний и внешний цикл фор чтобы добавлять изначально  пустые строки в матрицу, заполняя их значениями валуе
    for i in range (n) :
        line = []
        for j in range (m) :
            #добавляем в строку значения values m раз
            line.append (value)
        #добавляем в матрицу строку line  n раз
        matrix.append (line)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
