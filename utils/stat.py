import re
import os
import json
from collections import Counter
import matplotlib.pyplot as plt

def plot_length_frequency(length_frequency, name):
        lengths = list(length_frequency.keys())
        frequencies = list(length_frequency.values())

        plt.bar(lengths, frequencies)
        plt.xlabel('Sentence Length')
        plt.ylabel('Frequency (%)')
        plt.title(f'{name} Sentence Length Frequency')
        plt.savefig(f'{name}/sentence_length_frequency.png')
        plt.close()

def length_stat(text, name):
    sentences = re.split(r'[.!?]', text)  # Split text into sentences using regular expression
    os.makedirs(name, exist_ok=True)
    with open(f'{name}/sentences.txt', 'w') as file:
        for sentence in sentences:
            file.write(sentence.strip() + '\n')
    sentence_lengths = [len(sentence.split()) for sentence in sentences]  # Calculate sentence lengths

    length_counts = Counter(sentence_lengths)  # Count the frequency of sentence lengths

    total_sentences = len(sentences)

    length_frequency_dict = {}
    for length, count in length_counts.items():
        frequency_percentage = (count / total_sentences) * 100
        length_frequency_dict[length] = frequency_percentage

    sorted_length_frequency = dict(sorted(length_frequency_dict.items(), key=lambda x: x[0]))

    os.makedirs(name, exist_ok=True)
    with open(f'{name}/sentence_length_frequency.json', 'w') as json_file:
        json.dump(sorted_length_frequency, json_file)

    length_frequency = sorted_length_frequency 
    plot_length_frequency(length_frequency, name)

def word_stat(text, name):
    words = text.split()
    word_counts = Counter(words)

    total_words = len(words)

    word_frequency_dict = {}
    for word, count in word_counts.items():
        frequency_percentage = (count / total_words) * 100
        word_frequency_dict[word] = frequency_percentage

    sorted_word_frequency = dict(sorted(word_frequency_dict.items(), key=lambda x: x[1], reverse=True))

    with open(f'{name}/word_frequency.json', 'w') as json_file:
        json.dump(sorted_word_frequency, json_file)
