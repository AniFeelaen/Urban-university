def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list) # можно использовать перечисление через ИФ чтобы определять имя функций и тогда нужное-вычислять
        #     if func == min:
        #     results['min'] = min(int_list)
        # elif func == max:
        #     results['max'] = max(int_list)
        # elif func == len:
        #     results['len'] = len(int_list)
        # elif func == sum:
        #     results['sum'] = sum(int_list)
        # elif func == sorted:
        #     results['sorted'] = sorted(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))