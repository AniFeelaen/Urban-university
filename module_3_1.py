calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(string):
    length = len(string)
    up = string.upper()
    low = string.lower()
    count_calls()
    return (length, up, low)

def is_contains (string, list_to_search):
    count_calls()
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