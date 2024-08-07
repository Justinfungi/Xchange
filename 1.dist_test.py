import numpy as np
from scipy.stats import anderson_ksamp
import json
from utils.test import test_data

def perform_anderson_darling_test(json_file1, json_file2):
    # Read data from JSON files
    with open(json_file1) as f:
        data1 = json.load(f)

    with open(json_file2) as f:
        data2 = json.load(f)

    # Convert dictionaries to NumPy arrays
    data1 = np.array([k for k, v in sorted(dict(data1).items()) for _ in range(int(np.round(100 * v)))])
    data2 = np.array([k for k, v in sorted(data2.items()) for _ in range(int(np.round(100 * v)))])
    
    # Perform Anderson-Darling test
    statistic, p_value, _ = anderson_ksamp([data1, data2])
    
    # Return the test results
    return statistic, p_value

test_data(list(range(1,20)), 1, 1)
# Example usage
json_file1 = '/home/ubuntu/xchange/AI_Total/sentence_length_frequency.json'
json_file2 = '/home/ubuntu/xchange/test/sentence_length_frequency.json'
statistic_AI, p_value = perform_anderson_darling_test(json_file1, json_file2)
print(f"AI Anderson-Darling statistic: {statistic_AI}")
print(f"p-value: {p_value}")

# Example usage
json_file1 = '/home/ubuntu/xchange/Human_Total/sentence_length_frequency.json'
json_file2 = '/home/ubuntu/xchange/test/sentence_length_frequency.json'
statistic_human, p_value = perform_anderson_darling_test(json_file1, json_file2)
print(f"Human Anderson-Darling statistic: {statistic_human}")
print(f"p-value: {p_value}")

if statistic_human <= statistic_AI:
    print("Human sentences are more similar to the test sentences.")
else:
    print("AI sentences are more similar to the test sentences.")