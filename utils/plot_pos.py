import json
import json
import plotly.graph_objects as go

def plot_json_data(p, json_path):
    # Read the JSON data from the file
    with open(json_path) as file:
        jsonData = json.load(file)

    labels = list(jsonData.keys())
    values = list(jsonData.values())

    # Create the bar chart
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    fig.update_layout(
        xaxis=dict(title='Labels'),
        yaxis=dict(title='Number'),
        title='Vertical Bar Chart'
    )

    # Save the chart as an HTML file
    output_path = f"{p}/pos_frequency.html"
    fig.write_html(output_path)
    print(f"Bar chart saved at {output_path}")

    return output_path