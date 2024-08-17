calls = 0
#добавляем счетчик и возвращаем его значение при обращении
def count_calls():
    global calls
    calls = calls + 1
    return calls
#вызываем строку, прибавляем счетчик, считаем длину, и регистры верхний и нижний
def string_info(string):
    count_calls()
    length = len(string)
    up = string.upper()
    low = string.lower()
    return (length, up, low)
# считаем счетчик вызовов функций и смотрим есть ли первое значение в списке
def is_contains (string, list_to_search):
    count_calls() 
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    for item in list_to_search:
        if item in string:
            return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)