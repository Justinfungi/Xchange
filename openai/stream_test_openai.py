from openai import OpenAI
import pandas as pd
import time
import signal
import datetime
from openai_test import format_test, predict_v2, store_predictions_v2

def signal_handler(sig, frame):
    status = client.fine_tuning.jobs.retrieve(job_id).status
    print(f"Stream interrupted. Job is still {status}.")
    return

client = OpenAI(api_key="sk-roYuDSVuTABXZKbAM0dM_qrmqJpVwv1gYvcrBH6wxYT3BlbkFJrZWkOsRhO_DtGHgp_LK25lbIQA9Al22CPtNCYRnW8A")
result = client.fine_tuning.jobs.list()

job_id = "ftjob-Vcc7mJGwfRrYcbSElpjyG2n7"
print(job_id)


result = client.fine_tuning.jobs.list()
fine_tuned_model = result.data[0].fine_tuned_model

test_df = pd.read_json('/home/ubuntu/xchange/openai/train_test.jsonl', lines=True)
res_df = pd.DataFrame(columns=["Text", "Prediction", "GT"])
store_predictions_v2(test_df, fine_tuned_model, res_df, client)

