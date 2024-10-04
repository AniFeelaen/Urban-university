first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [(len(a) - len(b)) for a, b in zip(first, second) if len(a) != len(b)] # если длины элементов неравны, высчитываем длину
second_result = [(len(first[i]) == len(second[i])) for i in range(len(first)) if len(first) == len(second)] #если длина списков равна, то тогда сравниваем элементы

print(list(first_result))
print(list(second_result))