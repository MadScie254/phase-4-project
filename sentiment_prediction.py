import requests

# Define the URL for your Flask application
url = 'http://127.0.0.1:5000/predict'

# Define the text you want to predict sentiment for
data = {'text': 'This is a great product!'}
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    sentiment = result['sentiment']
    print(f"Predicted Sentiment: {sentiment}")
else:
    print(f"Error: {response.text}")
