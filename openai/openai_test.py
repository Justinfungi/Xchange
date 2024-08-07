from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
from datetime import datetime
import time 

def format_test(row):
    formatted_message = [{"role": "user", "content": row['Support Query']}]
    return formatted_message

def predict(test_messages, fine_tuned_model_id):
    response = client.chat.completions.create(
        model=fine_tuned_model_id, messages=test_messages, temperature=0, max_tokens=50
    )
    return response.choices[0].message.content

def store_predictions(test_df, fine_tuned_model_id):
    test_df['Prediction'] = None
    for index, row in test_df.iterrows():
        test_message = format_test(row)
        prediction_result = predict(test_message, fine_tuned_model_id)
        test_df.at[index, 'Prediction'] = prediction_result

    test_df.to_csv("predictions.csv")

def format_test_v2(system_content, user_content):
    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ]
    return messages

def predict_v2(test_messages, fine_tuned_model_id, client):
    response = client.chat.completions.create(
        model=fine_tuned_model_id, 
        messages=test_messages, 
        temperature=0, 
        max_tokens=50
    )
    return response.choices[0].message.content


def store_predictions_v2(test_df, fine_tuned_model_id, res_df, client):
    test_df['Prediction'] = None
    for index, row in test_df.iterrows():
        if index >100:
            continue

        test_message = format_test_v2(row[0][0]["content"],row[0][1]["content"])
        #print(test_message)
        prediction_result = predict_v2(test_message, fine_tuned_model_id, client)

        new_row_data = [row[0][1]["content"], prediction_result, row[0][2]["content"]]
        res_df.loc[len(res_df)] = new_row_data
        

    res_df.to_csv(f"{fine_tuned_model_id}_predictions.csv")
    accuracy_percentage = get_accuracy(res_df)
    print(accuracy_percentage)

def get_accuracy(df):
    correct_predictions = df[df['Prediction'] == df['GT']]
    accuracy_percentage = (len(correct_predictions) / len(df)) * 100
    return accuracy_percentage

def store_predictions_v3(test_df, fine_tuned_model_id, res_df, client):
    test_df['Prediction'] = None
    for index, row in test_df.iterrows():
        """if index >1:
            continue"""

        try:
            test_message = format_test_v2("You are a AI detection assistant for Machine Learning. You should help the user to detect whether the writing is created by AI according to the wording and writting habit of AI.",
                                            row[0])
            #print(test_message)
            prediction_result = predict_v2(test_message, fine_tuned_model_id, client)

            new_row_data = [row[0], prediction_result, row[1], row[2]]
            res_df.loc[len(res_df)] = new_row_data
        except:
            new_row_data = [row[0], row[1], row[2]]
            print(new_row_data)
            time.sleep(1)

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{fine_tuned_model_id}_{dt_string}_predictions.csv"
    res_df.to_csv(filename)
    accuracy_percentage = get_accuracy(res_df)
    print(accuracy_percentage)
