import nltk
import random
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

nltk.download('punkt')


def generate_sentences(text, n):
    tokens = word_tokenize(text)
    bigrams = list(ngrams(tokens, 2))
    trigrams = list(ngrams(tokens, 3))

    generated_sentences = []

    for _ in range(3):
        if n == 2:
            current_gram = random.choice(bigrams)
        elif n == 3:
            current_gram = random.choice(trigrams)

        sentence = list(current_gram)
        while len(sentence) < 15:
            next_words = [gram for gram in (bigrams if n == 2 else trigrams) if
                          gram[:n - 1] == tuple(sentence[-(n - 1):])]
            if not next_words:
                break
            next_word = random.choice(next_words)[-1]
            sentence.append(next_word)

        generated_sentences.append(' '.join(sentence))

    return generated_sentences


# Example usage
file_path = 'idiot.txt'  
with open(file_path, 'r',encoding='utf-8') as file:
    text = file.read()

bigram_sentences = generate_sentences(text, 2)
trigram_sentences = generate_sentences(text, 3)

print("Bigram sentences:")
for sentence in bigram_sentences:
    print(sentence)

print("\nTrigram sentences:")
for sentence in trigram_sentences:
    print(sentence)
