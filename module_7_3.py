class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = list(file_names)
    
    def get_all_words (self):
        all_words = {}
        for file_name in self.file_names:
            with open (file_name, 'r', encoding= 'utf-8') as file:
                file.read().lower().replace([',', '.', '=', '!', '?', ';', ':', ' - '], '')
                
    def 