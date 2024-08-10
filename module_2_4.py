numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

#формируем цикл фор и сразу после него записываем проверку на простоту
for i in numbers:
    is_prime = True
    #внутренний цикл фор в диапазоне до последнего числа не включительно
    for divisor in range (2, i-1):
        if i % divisor == 0:
            is_prime = False
            break
    #добавление простых и не простых чисел в списки, исключаем 1 по условию задачи        
    if is_prime and i != 1:
        primes.append(i)
    elif is_prime == False and i!= 1:
        not_primes.append(i)    
print ('Простые числа', primes, "Не простые числа", not_primes)
