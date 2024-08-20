def f(*args):
    sum = 0
    for element in args:
        if isinstance(element, list):
            for i in element :
                if i == int :
                  sum += i  
                if i == str :
                    sum+= len(i)
            return sum
        if isinstance(element, dict):
            sum.keys()
            return
            
f(data_structure)          
set
 