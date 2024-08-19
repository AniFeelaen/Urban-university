def single_root_words(root_word, *other_words) :
    same_words = []
    root_word = root_word.lower()
    other_words  = [item.lower() for item in other_words]
    for item in other_words :
        if root_word in item :
            same_words.append(item)
        elif item in root_word:
            same_words.append(item)
    return same_words
    
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)