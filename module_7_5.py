import os
import time
# print (os.getcwd())
# os.chdir (r'D:\github Urbanuniversity\Urban-university')
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print (dirs)
# print(file)

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file) # полный путь к файлу
        filetime = os.path.getmtime(filepath) # время файла сырое
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # последнее изменение 
        filesize = os.path.getsize(filepath) #размер
        parent_dir = os.path.dirname(filepath) #в какой папке находится
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Сырое время {filetime}, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
