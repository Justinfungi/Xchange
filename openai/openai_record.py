from openai import OpenAI
import time


client = OpenAI(api_key="sk-roYuDSVuTABXZKbAM0dM_qrmqJpVwv1gYvcrBH6wxYT3BlbkFJrZWkOsRhO_DtGHgp_LK25lbIQA9Al22CPtNCYRnW8A")
result = client.fine_tuning.jobs.list()
print(f"Found {len(result.data)} finetune jobs.")

#print(result.data[0])
items_list = []

for attr, value in result.data[0].__dict__.items():
    items_list.append((attr, value))

print(items_list)