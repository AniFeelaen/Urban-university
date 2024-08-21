data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = 0
def f(*args):
  result = 0
  for element in args:
      if isinstance(element, list):
          return f(args)
  
result = f(data_structure)
print(result)