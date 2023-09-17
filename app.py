from flask import Flask, request, jsonify
import numpy as np
import pickle  # Add this import statement for 'pickle'
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

app = Flask(__name__)

# Load the trained model
model = load_model('sentiment_model.h5')  # Replace with the actual path to your model

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)  # Replace with the actual path to your tokenizer

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.json['text']
        text_sequence = tokenizer.texts_to_sequences([text])
        text_padded = pad_sequences(text_sequence, maxlen=100)
        prediction = model.predict(text_padded)
        sentiment = "Positive" if prediction > 0.5 else "Negative"
        return jsonify({'sentiment': sentiment})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
