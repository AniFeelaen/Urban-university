grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # множество
sorted_students = sorted(list(students)) #преобразуем множество в упорядоченный список в алфавитном порядке
new_dict = {} # создаем пустой словарь

average1 = sum(grades[0])/len(grades[0]) # вычисляем средние оценки в списке grades
average2 = sum(grades[1])/len(grades[1])
average3 = sum(grades[2])/len(grades[2])
average4 = sum(grades[3])/len(grades[3])
average5 = sum(grades[4])/len(grades[4])


new_grades = (average1, average2, average3, average4, average5) #добавляем оценки в новый список
new_dict.update({sorted_students[0]: new_grades[0], sorted_students[1]: new_grades[1], sorted_students[2]: new_grades[2], sorted_students[3]: new_grades[3], 
               sorted_students[4]: new_grades[4]}) #добавляем студентов и оценки в словарь по парам


print (new_dict)
