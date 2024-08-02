
# Agricrypt Chatbot
Nerdma Hackathon 

Agricrypt Chatbot is a Flask-based web application integrated with Roboflow for image predictions and Telegram for chat interactions.



## Features

- **Flask Web Application**: Provides endpoints for predictions and serves a chatbot UI.
- **Roboflow Integration**: Uses a trained model for image predictions.
- **Telegram Integration**: Handles incoming messages via a webhook.
- **ngrok**: Exposes the Flask app to the internet for external access.
- **Agricrypt Chatbot Capabilities**:
  - **Generating Summaries**: Provides concise summaries of key findings from video analysis data.
  - **Creating Detailed Reports**: Writes detailed reports based on analysis results, including sections like Introduction, Analysis, Observations, Trends, and Recommendations.
  - **Producing Real-Time Alerts**: Drafts real-time alerts for critical issues identified in video analysis, specifying the issue, affected livestock, and suggested actions.
  - **Responding to Queries**: Answers questions related to livestock behavior, health, and farm security based on provided video data.

## Prerequisites

- Python 3.6 or higher
- Flask
- Roboflow
- TensorFlow
- Requests
- PyYAML
- pyngrok

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2. **Install the Dependencies**

    ```bash
    pip install flask roboflow tensorflow requests pyyaml pyngrok
    ```

## Configuration

1. **Set Up Your API Keys and Tokens**

    - Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual Telegram bot token.
    - Replace `YOUR_API_KEY` with your Roboflow API key.
    - Replace `YOUR_PROJECT_NAME` and `YOUR_VERSION_NUMBER` with your Roboflow project details.
    - Replace `https://chatgpt.com/g/g-xPyvswL5h-agricrypt` with your bot endpoint.

## Running the Application on Google Colab

1. **Install the Necessary Packages**

    In your Colab notebook, run:
    ```python
    !pip install flask roboflow tensorflow requests pyyaml pyngrok
    ```

2. **Upload the Application Code**

    Copy the contents of `app.py` and run it in a cell in your Colab notebook.

3. **Create the HTML Template**

    Create an `index.html` file inside a `templates` directory. Skip this step if you have already saved the `index.html` file.

4. **Run the Application**

    ```python
    !agricrypt app.py
    ```

5. **Access the Application**

    - Follow the ngrok public URL displayed in the Colab output to interact with your chatbot.

## Setting the Telegram Webhook

The script will automatically set the Telegram webhook to the ngrok public URL. Ensure that your Telegram bot token and ngrok URL are correctly configured.

## Endpoints

- `/predict_intent` - Predicts the intent from the provided text.
- `/predict_local` - Predicts using the Roboflow model on a local image.
- `/predict_hosted` - Predicts using the Roboflow model on an image hosted elsewhere.
- `/upload` - Uploads an image.
- `/webhook` - Webhook endpoint for Telegram bot.
- `/` - Serves the chatbot UI.


