def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1 
            print(f'Некорректный тип данных для подсчёта суммы - {number}') #каждый раз если строка а не число, получим пример неправильного типа данных
    return result, incorrect_data          
    
def calculate_average(numbers):
    try:
        summa, incorrect_data = personal_sum(numbers) # в кортеже из суммы и некорректных данных используем только сумму
        average = summa / (len(numbers) - incorrect_data)
        return average
    except ZeroDivisionError:
        print('Количество элементов в коллекции равно нулю')
        return 0
    except TypeError:
        print ('В numbers записан некорректный тип данных')
        return None
        
    
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать    
print(f'Результат 5: {calculate_average([])}')# передаем пустую коллекцию
