import json
import nltk

def get_pos_sequence(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    pos_sequence = [tag[1] for tag in pos_tags]
    return pos_sequence

file_path = '/home/ubuntu/xchange/AI_Total/pos_frequency.json'

with open(file_path, 'r') as file:
    AI_pos = json.load(file)

file_path = '/home/ubuntu/xchange/Human_Total/pos_frequency.json'

with open(file_path, 'r') as file:
    Human_pos = json.load(file)

Sentences = "the authors investigate how licensing influences innovation patterns, industry costs, and market structure."


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

pos_sequence = get_pos_sequence(Sentences)
        
first_pos = pos_sequence[0]
pos_sequence_str = ' '.join(pos_sequence)
pos_sequence_str = [str(len(item.split(" "))) for item in pos_sequence_str.split(" , ")]
pos_sequence_str = [item for item in pos_sequence_str if item != " "]
#pos_sequence_str = ' '.join(pos_sequence_str)
pos_sequence_str = first_pos+str(len(pos_sequence_str))

if pos_sequence_str in AI_pos:
    value_AI = AI_pos[pos_sequence_str]
    print(value_AI)
else:
    print("Key not found in AI_pos")

if pos_sequence_str in Human_pos:
    value_Human = Human_pos[pos_sequence_str]
    print(value_Human)
else:
    print("Key not found in AI_pos")

if value_AI > value_Human*1.5:
    print("AI has higher frequency")
elif value_AI < value_Human*1.5:
    print("Human has higher frequency")
else:
    print("AI and Human have the same frequency")