import csv
import json
from collections import Counter
import os
import re
import matplotlib.pyplot as plt
from utils.sentences import split_sentences
from utils.tag import process_pos_sequences
from utils.plot_pos import plot_json_data


""" idx = 1 is AI. 0 is Human"""
def get_data(idx):
    with open('testing500.csv', 'r') as file:
        reader = csv.reader(file)
        column1_values = []
        for i, row in enumerate(reader):
            if i >0:
                column1_values.append(row[idx])
            if i == 2:
                print(row[idx], "\n\n")

    combined_text = ' '.join(column1_values)
    lowercase_text = combined_text.lower() 
    return  lowercase_text

def plot_length_frequency(length_frequency, name):
        length_frequency = {length: frequency for length, frequency in length_frequency.items() if frequency != 0}
        lengths = list(length_frequency.keys())
        frequencies = list(length_frequency.values())

        plt.bar(lengths, frequencies)
        plt.xlabel('Sentence Length')
        plt.ylabel('Frequency (%)')
        plt.title(f'{name} Sentence Length Frequency')
        plt.savefig(f'{name}/sentence_length_frequency.png')
        plt.close()

def length_stat(text, name):
    sentences = split_sentences(text)  # Split text into sentences using regular expression
    os.makedirs(name, exist_ok=True)
    with open(f'{name}/sentences.txt', 'w') as file:
        for sentence in sentences:
            if len(sentence.split(" ")) > 5:
                file.write(sentence.strip() + '\n')
    sentence_lengths = [len(sentence.split()) for sentence in sentences]  # Calculate sentence lengths

    length_counts = Counter(sentence_lengths)  # Count the frequency of sentence lengths

    total_sentences = len(sentences)

    length_frequency_dict = {}
    for length, count in length_counts.items():
        frequency_percentage = (count / total_sentences) * 100
        length_frequency_dict[length] = round(frequency_percentage, 2)

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
        word_frequency_dict[word] = round(frequency_percentage, 2)

    sorted_word_frequency = dict(sorted(word_frequency_dict.items(), key=lambda x: x[1], reverse=True))

    with open(f'{name}/word_frequency.json', 'w') as json_file:
        json.dump(sorted_word_frequency, json_file)


lowercase_text = get_data(0)
length_stat(lowercase_text, "Human_Total")
word_stat(lowercase_text, "Human_Total")
process_pos_sequences("Human_Total")
plot_json_data("Human_Total", "/home/ubuntu/xchange/Human_Total/pos_frequency.json")


lowercase_text = get_data(1)
length_stat(lowercase_text, "AI_Total")
word_stat(lowercase_text, "AI_Total")
process_pos_sequences("AI_Total")
plot_json_data("AI_Total", "/home/ubuntu/xchange/AI_Total/pos_frequency.json")
