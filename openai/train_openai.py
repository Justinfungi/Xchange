from openai import OpenAI
import signal
import datetime
import time

client = OpenAI(api_key="sk-roYuDSVuTABXZKbAM0dM_qrmqJpVwv1gYvcrBH6wxYT3BlbkFJrZWkOsRhO_DtGHgp_LK25lbIQA9Al22CPtNCYRnW8A")

training_file_name = '/home/ubuntu/xchange/openai/train_train.jsonl'
validation_file_name = '/home/ubuntu/xchange/openai/train_validate.jsonl'

training_file = client.files.create(
    file=open(training_file_name, "rb"), purpose="fine-tune"
)
validation_file = client.files.create(
    file=open(validation_file_name, "rb"), purpose="fine-tune"
)

hyperparameters={
    "n_epochs": 15,
    "batch_size": 3,
    "learning_rate_multiplier": 0.3
}

# Create Fine-Tuning Job
suffix_name = "Xchange"
response = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    validation_file=validation_file.id,
    model="gpt-3.5-turbo",
    suffix=suffix_name
)

job_id = response.id

print(job_id)
print(f"Streaming events for the fine-tuning job: {job_id}")

while True:
    job_status = client.fine_tuning.jobs.retrieve(job_id).status
    if job_status == "succeeded":
        break
    elif job_status == "failed":
        print("Fine-tuning job failed.")
        break
    else:
        print(f"Job status: {job_status}")
        # Add any additional monitoring logic here
        time.sleep(60)  # Check job status every 30 seconds

