def get_lexicon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split()
lexicon = get_lexicon('sv-utf8.txt')
print(lexicon)
