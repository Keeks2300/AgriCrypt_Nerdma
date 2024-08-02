mport os
from flask import Flask, request, jsonify, render_template
import requests
from pyngrok import ngrok
import logging
from roboflow import Roboflow
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import yaml

app = Flask(__name__)
TOKEN = '########'  # Replace with your Telegram bot token
GPT_URL = 'https://www.agenthost.ai/chat/agricrypt'  # Replace with your  endpoint

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Roboflow API key and project details
API_KEY = "YOUR_API_KEY"  # Replace with your Roboflow API key
PROJECT_NAME = "YOUR_PROJECT_NAME"  # Replace with your project name
VERSION_NUMBER = YOUR_VERSION_NUMBER  # Replace with your project version number

# Initialize Roboflow model
rf = Roboflow(api_key=API_KEY)
project = rf.workspace().project(PROJECT_NAME)
model = project.version(VERSION_NUMBER).model

# Load and preprocess data 
def load_and_preprocess_data():
    # Example text data and labels 
    texts = ["Hi?", "What is wrong with my cow ?","How"]
    labels = ["greeting", "Cow", "Question"]

    # Tokenize the text data
    tokenizer = Tokenizer(num_words=10000)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    data = pad_sequences(sequences, maxlen=100)

    # Encode labels
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)

    # Splits the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, tokenizer, label_encoder

# Build and train a simple neural network model
def build_and_train_model(X_train, y_train, X_test, y_test):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Embedding(input_dim=10000, output_dim=64, input_length=100),
        tf.keras.layers.LSTM(64, return_sequences=True),
        tf.keras.layers.LSTM(64),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(len(set(y_train)), activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
    return model

# Predict the intent of a given text
def predict_intent(model, tokenizer, label_encoder, text):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=100)
    prediction = model.predict(padded_sequence)
    predicted_label = label_encoder.inverse_transform([prediction.argmax()])[0]
    return predicted_label

# Load and preprocess data for intent classification
X_train, X_test, y_train, y_test, tokenizer, label_encoder = load_and_preprocess_data()
intent_model = build_and_train_model(X_train, y_train, X_test, y_test)

# Function to send a message via Telegram
def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url, json=payload)
    logging.info(f'Send message response: {r.json()}')
    return r.json()

# Function to get a response from GPT
def get_gpt_response(user_message):
    payload = {
        'prompt': user_message,
        'max_tokens': 50  # Adjust as needed
    }
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(GPT_URL, json=payload, headers=headers)
    logging.info(f'GPT response: {r.json()}')
    return r.json().get('text', 'Sorry, I could not get a response from the GPT.')

# Webhook endpoint for Telegram bot
@app.route('/webhook', methods=['POST'])
def webhook():
    logging.info('Webhook received a request.')
    if request.method == 'POST':
        update = request.json
        logging.info(f'Update received: {update}')
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            text = update['message']['text']
            gpt_response = get_gpt_response(text)
            send_message(chat_id, gpt_response)
        return jsonify(update)

# Endpoint to predict the intent from text
@app.route('/predict_intent', methods=['POST'])
def predict_intent_endpoint():
    data = request.json
    text = data['text']
    predicted_intent = predict_intent(intent_model, tokenizer, label_encoder, text)
    return jsonify({'intent': predicted_intent})

# Endpoint to predict using Roboflow model on a local image
@app.route('/predict_local', methods=['POST'])
def predict_local_image():
    data = request.json
    image_path = data['image_path']  # Path to the local image
    confidence = data.get('confidence', 40)  # Default confidence is set to 40 
    overlap = data.get('overlap', 30)  # Default overlap is set to 30 

    # Perform prediction using the Roboflow model
    prediction = model.predict(image_path, confidence=confidence, overlap=overlap).json()
    return jsonify(prediction)

# Endpoint to predict using Roboflow model on an image
@app.route('/predict_hosted', methods=['POST'])
def predict_hosted_image():
    data = request.json
    image_url = data['image_url']  # URL of the hosted image (telegram)
    confidence = data.get('confidence', 40)  # Default confidence is set to 40 
    overlap = data.get('overlap', 30)  # Default overlap is set to 30 

    # Perform prediction using the Roboflow model
    prediction = model.predict(image_url, hosted=True, confidence=confidence, overlap=overlap).json()
    return jsonify(prediction)

# Render the chatbot UI
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to upload an image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path})

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    # Expose the Flask app via ngrok
    url = ngrok.connect(5000)
    print(f'Public URL: {url}')
    app.run(port=5000)
