
def add_everything_up(a, b):
    try: 
       return round(a + b, 3)  #выполняем сложение чисел если все окей + округляем
    except TypeError as exc:
       return str(a) + str(b)  # если есть несочетание типов между собой то выполняем сложение строк
        # return f'{a}{b}'
        
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))