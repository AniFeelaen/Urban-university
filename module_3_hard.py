data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = 0
def calculate_structure_sum(*args): # знак * распаковывает содержимое
  result = 0
  for element in args:
    print(element)
    if isinstance(element, list):
      result += calculate_structure_sum(*element) #используем рекурсию чтобы приплюсовать все элементы списка
    
    elif isinstance(element, int): # рекурсию при простых числах делать не нужно, так как элемент 1
      result += element
    elif isinstance(element, str):
      result += len(element)
    elif isinstance(element, set): #используем рекурсию чтобы приплюсовать все элементы множества
      result += calculate_structure_sum(*element)        
    elif isinstance(element, tuple): #используем рекурсию чтобы приплюсовать все элементы кортежа
      result += calculate_structure_sum(*element)
      
    elif isinstance(element, dict): #со словарем нужно использовать оба его аргумента для рекурсии
      result += calculate_structure_sum(*element.keys()) #не используем len потому что выше уже есть приплюсовывание строки
      result += calculate_structure_sum(*element.values())
  return result
  
summa = calculate_structure_sum(data_structure) #присваиваем результат функции, переменной, чтобы сохранить глобально результат
print(summa)