data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]



def count_sums(data_structure):
    sum_of_numbers = 0
    sum_of_strings_lengths = 0
    
    
    def recurse(element):
        nonlocal sum_of_numbers, sum_of_strings_lengths
        if isinstance(element, int):
            sum_of_numbers += element
        elif isinstance(element, str):
            sum_of_strings_lengths += len(element)
        else:
            # Рекурсивно проходим через список, словарь или кортеж
            if isinstance(element, list):
                for sub_element in element:
                    recurse(sub_element)
            elif isinstance(element, dict):
                for value in element.values():
                    recurse(value)
            elif isinstance(element, tuple):
                for sub_element in element:
                    recurse(sub_element)
            elif isinstance(element, set):
                for sub_element in element:
                    recurse(sub_element)
    
    recurse(data_structure)
    
    return sum_of_numbers, sum_of_strings_lengths

# Вызов функции с входными данными

sum_of_numbers, sum_of_strings_lengths = count_sums(data_structure)
whole_summ = sum_of_strings_lengths + sum_of_numbers
print(f"Сумма чисел: {sum_of_numbers}")
print(f"Сумма длин строк: {sum_of_strings_lengths}")
print(f"Сумма всех чисел и длин строк : {whole_summ}")