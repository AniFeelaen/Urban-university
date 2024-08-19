def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0]) #запоминаем первый элемент
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:])) # умножаем первый элемент на все, кроме первого
    return first

result = get_multiplied_digits(40203)
print(result)   
