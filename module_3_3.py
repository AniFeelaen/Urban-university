
def append_to_list(item, list_my = [None]):
    if list_my is None:
        list_my = []
    list_my.append(item)



def print_params(a = 1, b = 'строка', c = True):
    print (print_params)
print_params(a = 5, b = 10, c = False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['true', True, 5]

values_dict = {a: 5, b: 5, c: False}