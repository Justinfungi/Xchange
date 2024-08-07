from utils.stat import word_stat, length_stat
import csv

def get_data(row_list, col, default_msg=None):
    print(default_msg)
    if default_msg:
        return open('/home/ubuntu/xchange/docs/a.txt').read()
    with open('testing500.csv', 'r') as file:
        reader = csv.reader(file)
        column1_values = []
        for i, row in enumerate(reader):
            if i >0:
                if i in row_list:
                    column1_values.append(row[col])

    combined_text = ' '.join(column1_values)
    lowercase_text = combined_text.lower() 
    return  lowercase_text

def test_data(row_list, col, default_msg):
    data = get_data(row_list, col, default_msg)
    print(data)
    length_stat(data, 'test')

