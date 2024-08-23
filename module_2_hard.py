summashifra = []
def shifr(x, y):
    global summashifra
    x = x.random(3, 20)
    for y in range(x) :
        if y+1 + y+2 % x :
            return summashifra.append(y+1, y+2)
        else :
            print ("пар нет")
    return shifr
result = summashifra
print (result)