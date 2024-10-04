first = 'Мама мыла раму'
second = 'Рамена мало было'

i = list(map(lambda x,y: x==y, first, second))

print(i)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding= 'utf-8') as f: #открываем файл в русской кодировке и разделяем два элемента списка
            for item in data_set:
                f.write(str(item) + '\n')                  # "эту строчку" и список с элементами 
    return write_everything

write = get_advanced_writer('example.txt')  #но не паонимаю в чем смысл записывания функции в функции
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



from random import choice
class MysticBall:
    def __init__(self, *words):  #помечаем words * так как количество неограниченно
        self.words = words
    
    def __call__(self):              #вызываем функцию чойс из рандома (выбирает наугад один элемент из списка)
        return choice(self.words)
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())