class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    
    def get_all_words (self):
        all_words = {}
        for file_name in self.file_names:
            with open (file_name, 'r', encoding= 'utf-8') as file:
                # words = file.read().lower().replace([',', '.', '=', '!', '?', ';', ':', ' - '], '')
                words = file.read().lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace(' - ', '')
                all_words[file_name] = words
        return all_words
    def find(self, word: str):
        all_words = self.get_all_words()
        positions = {}
        for file_name, words in all_words.items():
            try:
                index = words.index(word)
                positions[file_name] = index
            except ValueError:
                pass
        return positions

    def count(self, word: str):
        all_words = self.get_all_words()
        counts = {}
        for file_name, words in all_words.items():
            count = words.count(word)
            counts[file_name] = count
        return counts
    
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего