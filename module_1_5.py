immutable_var = tuple(1,"string", True, 2)
print(immutable_var)
immutable_var [1] = "list" #выдаст ошибку, так как нельзя в кортеже менять неизменяемые элементы

mutable_list = [1,"string", True, 2]
mutable_list[1] = "list" #список можно менять и string заменится на list
print(mutable_list)
