def custom_write(file_name, strings):
    strings_positions = {}
    number_of_string = 1
    byte_of_string = 0
    file = open(file_name, 'w', encoding = 'utf-8')
    for string in strings:
        # current_position = file.tell()
        file.write(string + '\n')
        current_position = file.tell() #запоминаем на чем закончилась строка
        position = (number_of_string, byte_of_string) #сначала записываем 0 байт и 1 строку, а потом уже меняем значение байта и строки
        strings_positions[position] = string #тут записываем словарь с (строка, байт) ("наша строка")
        number_of_string += 1
        byte_of_string = current_position #забисываем байт конца строки в переменную
    
    file.close
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
    