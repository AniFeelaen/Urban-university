import random

#выбираем случайное число из списка от 3 до 20
def select():
    spisok = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    first_number = random.choice(spisok)
    return first_number
#считаем пары где происходит деление первого числа на сумму этих пар
def count(first_number):
    result = []
    for i in range(1, first_number):
        for j in range(i+1, first_number): #используем i+1 чтобы не было дубляжей пар
            if first_number % (i + j) == 0:
                result.append(i)
                result.append(j)
    return result

first_number = select()
print(first_number)
result = count(first_number)
print(result)
#умучался


# import random
# result = []
# def select():
#     spisok = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     first_number = random.choice(spisok)
#     return first_number

# first_number = select()
# print (first_number)

# def count(first_number, i):
#     global result
#     for i in range (1, first_number):
#         for j in range (i, first_number):
#             if first_number % (i+ j) == 0:
#                 result.append(i)
#                 result.append(j)
#     return result
# a = count(5,5)
# print(a)
        
# def shifr(x, y):
#     summashifra = []
#     x = random.choice(spisok)
#     for y in range(x):
#         if  x % (y + (y+1)) == 0:
#             summashifra.append([y, y+1])
#     return summashifra

# print(shifr(18, 15))
# # result = shifr(6,y)
# # print (result)