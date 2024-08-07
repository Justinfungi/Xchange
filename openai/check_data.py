from collections import defaultdict
import json

# Initialize a dictionary to store format errors
format_errors = defaultdict(int)

# Load the data from the JSONL files
def load_data_from_jsonl(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

# Paths to the JSONL files
training_file_name = '/home/ubuntu/xchange/openai/train_train.jsonl'
validation_file_name = '/home/ubuntu/xchange/openai/train_validate.jsonl'

# Load data from the JSONL files
training_data = load_data_from_jsonl(training_file_name)
validation_data = load_data_from_jsonl(validation_file_name)

# Check format errors in the loaded data
for dataset in [training_data, validation_data]:
    for ex in dataset:
        if not isinstance(ex, dict):
            format_errors["data_type"] += 1
            continue

        messages = ex.get("messages", None)
        if not messages:
            format_errors["missing_messages_list"] += 1
            continue

        for message in messages:
            if "role" not in message or "content" not in message:
                format_errors["message_missing_key"] += 1

            if any(k not in ("role", "content", "name") for k in message):
                format_errors["message_unrecognized_key"] += 1

            if message.get("role", None) not in ("system", "user", "assistant"):
                format_errors["unrecognized_role"] += 1

            content = message.get("content", None)
            if not content or not isinstance(content, str):
                format_errors["missing_content"] += 1

        if not any(message.get("role", None) == "assistant" for message in messages):
            format_errors["example_missing_assistant_message"] += 1

# Display the format errors
if format_errors:
    print("Found errors:")
    for k, v in format_errors.items():
        print(f"{k}: {v}")
else:
    print("No errors found")