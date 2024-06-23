import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

# Загрузка необходимых ресурсов NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Загрузка текста из файла
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Предобработка текста
def preprocess_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('russian'))
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word not in stop_words]
    return words, sentences

# Построение распределения частот
def plot_word_frequencies(common_words):
    df = pd.DataFrame(common_words, columns=['Word', 'Frequency'])
    df.plot(kind='bar', x='Word', y='Frequency', legend=False)
    plt.title('Top N Most Common Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()

# Поиск предложений, содержащих больше 4 наиболее часто встречающихся слов
def find_sentences_with_common_words(sentences, common_words_set):
    result = []
    lemmatizer = WordNetLemmatizer()
    for sentence in sentences:
        words_in_sentence = [lemmatizer.lemmatize(word) for word in word_tokenize(sentence.lower()) if word.isalnum()]
        common_word_count = sum(1 for word in words_in_sentence if word in common_words_set)
        if common_word_count > 4:
            result.append((sentence, common_word_count))
    return result

# Основной код
file_path = 'text1.txt'  # Укажите путь к вашему текстовому файлу
text = load_text(file_path)
words, sentences = preprocess_text(text)

# Подсчет частоты слов
N = 15
word_freq = Counter(words)
common_words = word_freq.most_common(N)
common_words_set = {word for word, _ in common_words}

# Построение распределения частот
plot_word_frequencies(common_words)

# Найти и отобразить предложения
sentences_with_common_words = find_sentences_with_common_words(sentences, common_words_set)
for sentence, count in sentences_with_common_words:
    print(f'Sentence: {sentence}\nCommon words count: {count}\n')
