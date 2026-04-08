from pathlib import Path

error_path = Path('text_files/error_in_alice.py.txt')

def count_words(path):
    """подсчет приблизительного количества слов в тексте"""
    try:
        contents = path.read_text(encoding='utf-8')
    except(FileNotFoundError):
        error_path.write_text(f'Книга {path} не найдена в файлах.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f"\nФайл {path} содержит {num_words} слов.")

filenames = ['text_files/alice.txt', 'text_files/moby_dick.txt', 
             'text_files/siddartha.txt', 'text_files/little_women.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)
