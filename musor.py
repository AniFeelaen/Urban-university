import re
from typing import Dict, List, Tuple

class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = list(file_names)

    def get_all_words(self) -> Dict[str, List[str]]:
        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                words = file.read().lower().replace('\n', '').replace('.', '').replace(',', '').replace('=', '').replace('!', '').replace('?', '').replace(':', '').replace(';', '').replace(' - ', '')
                words = re.sub(r'\s+', ' ', words).strip().split()
                all_words[filename] = words
        return all_words

    def find(self, word: str) -> Dict[str, int]:
        all_words = self.get_all_words()
        positions = {}
        for filename, words in all_words.items():
            try:
                index = words.index(word)
                positions[filename] = index
            except ValueError:
                pass
        return positions

    def count(self, word: str) -> Dict[str, int]:
        all_words = self.get_all_words()
        counts = {}
        for filename, words in all_words.items():
            count = words.count(word)
            counts[filename] = count
        return counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего