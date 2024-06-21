import re

def analyze_poem(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        poem = file.read()
    
    # Подсчёт количества строк
    lines = poem.strip().split('\n')
    num_lines = len(lines)
    
    # Подсчёт количества предложений
    sentences = re.split(r'[.!?]', poem)
    num_sentences = len([s for s in sentences if s.strip() != ''])
    
    # Подсчёт количества вопросительных предложений
    question_sentences = re.findall(r'\?', poem)
    num_question_sentences = len(question_sentences)
    
    return num_lines, num_sentences, num_question_sentences

# Пример использования
file_path = 'poem.txt'  # Укажите путь к файлу со стихотворением
num_lines, num_sentences, num_question_sentences = analyze_poem(file_path)

print(f"Количество строк: {num_lines}")
print(f"Количество предложений: {num_sentences}")
print(f"Количество вопросительных предложений: {num_question_sentences}")
