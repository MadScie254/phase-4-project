import requests

url = 'http://127.0.0.1:5000/predict'
data = {'text': 'This is a positive tweet!'}  # Replace with your text
response = requests.post(url, json=data)

print(response.json())  # This will print the model's prediction
