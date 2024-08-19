def single_root_words(root_word, *other_words) :
    same_words = []
    #Приводим к одному регистру сначала корневое слово а потом список
    root_word = root_word.lower()
    other_words  = [item.lower() for item in other_words]
    #Проходим по неизвестному списку и проверяем сначала входимость корневого слова а потом входимость слов списка в корневое
    for item in other_words :
        if root_word in item :
            #.append пополняем список вхождений
            same_words.append(item)
        elif item in root_word:
            same_words.append(item)
    return same_words
    
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)