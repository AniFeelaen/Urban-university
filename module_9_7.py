def is_prime(func):
    def wrapper(*args):
        result_dec = func(*args)
        if result_dec % 2 != 0:
            print("Простое") 
        else:
            print("Составное")
        print(result_dec)
    return wrapper

@is_prime
def sum_three(a,b,c):
    result_three = a + b + c
    # print (result_three)
    return result_three


result = sum_three(2, 3, 6)
# print(result)