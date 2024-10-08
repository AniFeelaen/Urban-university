def all_variants(text):
    for i in range(len(text)): #проходимся по списку после нашего элемента и записываем
        for j in range(i,len(text)): 
            yield text[i:j+1]  


a = all_variants("abcdg")
for i in a:
    print(i)