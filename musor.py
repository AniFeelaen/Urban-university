def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        sum_, incorrect_data = personal_sum(numbers)
        average = sum_ / len(numbers)
        return average
    except ZeroDivisionError:
        print('Количество элементов в коллекции равно нулю. Среднее арифметическое равно 0.')
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных. Среднее арифметическое не может быть рассчитано.')
        return None
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать