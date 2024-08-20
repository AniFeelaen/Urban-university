def f(*args):
    for element in args:
        if isinstance(element, list):
            return f + len(element)
        if isinstance(element, dict):
            return
            
f(data_structure)            