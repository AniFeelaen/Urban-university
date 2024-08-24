data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = 0
def calculate_structure_sum(*args):
  result = 0
  for element in args:
    print(element)
    if isinstance(element, list):
      result += calculate_structure_sum(*element)
    elif isinstance(element, int):
      result += element
    elif isinstance(element, str):
      result += len(element)
    elif isinstance(element, tuple):
      result += element
    elif isinstance(element, dict):
      result += len(element.keys())
      result += element.values()

    elif isinstance(element, set):
      result += element
      
  return result
  
summa = calculate_structure_sum(data_structure)
print(summa)