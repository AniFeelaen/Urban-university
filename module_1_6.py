my_dict = {alex : 2000, dmitry : 1990, anton : 1980}
print(my_dict)
print("печатаем одно значение", my_dict[alex])
Print("не существующее значение", my_dict.get[alexander])

my_dict.update ({kostya : 2001, masha : 2002})
a = my_dict.pop[kostya] #выбираем лишний элемент из словаря
print (my_dict[masha])
print("измененный словарь", my_dict)

my_set = {1, "odin", 1.5, 1, "odin"}
print (my_set)
my_set.add(2, "dva")
my_set.discard (1) #убираем элемент из множества
print("новое множество", my_set)
