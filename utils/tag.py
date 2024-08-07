import nltk
import json

def get_pos_sequence(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    pos_sequence = [tag[1] for tag in pos_tags]
    return pos_sequence

def process_pos_sequences(directory_path):
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

    with open(directory_path + '/sentences.txt', 'r') as file:
        sentences = file.readlines()

    pos_sequences = []
    for sentence in sentences:
        pos_sequence = get_pos_sequence(sentence)
        pos_sequences.append(pos_sequence)

    with open(directory_path + '/pos_sequences.txt', 'w') as file:
        for pos_sequence in pos_sequences:
            file.write(' '.join(pos_sequence) + '\n')

    pos_frequency = {}
    for pos_sequence in pos_sequences:
        try:
            first_pos = pos_sequence[0]
        except:
            first_pos = "NA"
        
        #print(pos_sequence_str)
        if pos_sequence_str in pos_frequency:
            pos_frequency[pos_sequence_str] += 1
        else:
            pos_frequency[pos_sequence_str] = 1

    total_sequences = len(pos_sequences)
    pos_percentage = {pos: (freq / total_sequences) * 100 for pos, freq in pos_frequency.items()}

    sorted_pos_frequency = dict(sorted(pos_percentage.items(), key=lambda x: x[1], reverse=True))
    with open(directory_path + '/pos_frequency.json', 'w') as file:
        json.dump(sorted_pos_frequency, file)
pos_sequence_str = ' '.join(pos_sequence)
        pos_sequence_str = [str(len(item.split(" "))) for item in pos_sequence_str.split(" , ")]
        pos_sequence_str = [item for item in pos_sequence_str if item != " "]
        #pos_sequence_str = ' '.join(pos_sequence_str)
        pos_sequence_str = first_pos+str(len(pos_sequence_str))
