class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    
    def get_all_words (self):
        all_words = {}
        for file_name in self.file_names:
            with open (file_name, 'r', encoding= 'utf-8') as file:
                # words = file.read().lower().replace([',', '.', '=', '!', '?', ';', ':', ' - '], '') список использовать нельзя, в конце не забываем. split. чтобы каждое слово вошло в словарь
                words = file.read().lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace(' - ', '').split()
                all_words[file_name] = words
        return all_words
    
    def find(self, word: str):
        all_words = self.get_all_words()
        positions = {}
        word = word.lower() #обязательно преобразуем искомое слово в нижний регистр чтобы им (регистром) пренебречь.
        counter = 0
        for file_name, words in all_words.items():
            for index in (words):
                if index == word:
                    position = counter  # считаем слова в списке используя счетчик (первое слово текст = 3 проходам цикла фор )
                # = words.index(word)   # не используем index - определяет индекс первого встреченного
                    positions[file_name] = position
                    counter += 1
        return positions

    def count(self, word: str):
        all_words = self.get_all_words()
        counts = {}
        word = word.lower()  #обязательно преобразуем искомое слово в нижний регистр чтобы им (регистром) пренебречь.
        for file_name, words in all_words.items():
            count = words.count(word) # используем count - считаем сколько всего слов
            counts[file_name] = count
        return counts
    
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего