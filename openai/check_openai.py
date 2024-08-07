from openai import OpenAI
import time
import signal
import datetime


def signal_handler(sig, frame):
    status = client.fine_tuning.jobs.retrieve(job_id).status
    print(f"Stream interrupted. Job is still {status}.")
    return

client = OpenAI(api_key="sk-roYuDSVuTABXZKbAM0dM_qrmqJpVwv1gYvcrBH6wxYT3BlbkFJrZWkOsRhO_DtGHgp_LK25lbIQA9Al22CPtNCYRnW8A")
result = client.fine_tuning.jobs.list()

job_id = "ftjob-Vcc7mJGwfRrYcbSElpjyG2n7"
print(job_id)

# Monitor Progress

"""while True:
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

print(f"Streaming events for the fine-tuning job: {job_id}")


signal.signal(signal.SIGINT, signal_handler)
events = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id)
try:
    with open("training_log.txt", "a") as file:
        for event in events:
            print(
                f'{datetime.datetime.fromtimestamp(event.created_at)} {event.message}'
            )
            log_entry = f'{datetime.datetime.fromtimestamp(event.created_at)} {event.message}\n'
            file.write(log_entry)
except Exception:
    print("Stream interrupted (client disconnected).")
"""

result = client.fine_tuning.jobs.list()
fine_tuned_model = result.data[0].fine_tuned_model
new_prompt = """
When you mention that "audit needs to outlast using AWS to audit stock analysis," the term "outlast" in this context likely means that the audit process needs to continue or remain effective beyond the period when you are actively using AWS for auditing stock analysis.

Here are a few interpretations of what "outlast" could mean in this context:

Persistence: The audit should persist even after the AWS tools are no longer being actively used for stock analysis. This could imply that the audit process needs to be durable and ongoing, regardless of changes in tools or systems.
Longevity: The audit process should have a long-lasting impact or relevance, extending beyond the immediate use of AWS for stock analysis. It suggests that the audit's effects and benefits should be felt well into the future.
Endurance: The audit should be robust and able to withstand changes or challenges that may arise, ensuring the integrity and accuracy of stock analysis data even after the AWS tools are no longer in use.
In essence, stating that the audit needs to "outlast using AWS to audit stock analysis" implies that the audit process should endure, continue to be effective, and maintain its integrity beyond the specific period during which AWS tools are utilized for auditing stock analysis.
​"""

messages = [
    {"role": "system", "content": "You are a AI detection assistant for Machine Learning. You should help the user to detect whether the writing is created by AI according to the wording and writting habit of AI."},
    {"role": "user", "content": new_prompt}
]

answer = client.chat.completions.create(
    model=fine_tuned_model,
    messages=messages,
    temperature=0,
    max_tokens=50
)

with open("output.txt", "a") as file:
    file.write("New Prompt:\n")
    file.write(new_prompt + "\n\n")
    file.write("Content from Answer:\n")
    file.write(answer.choices[0].message.content)
    
    
print(new_prompt)
print(answer.choices[0].message.content)