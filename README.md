
# Agricrypt Chatbot
Nerdma Hackathon 

Agricrypt Chatbot assists farmers in understanding livestock issues faster by providing AI-driven insights through a simple, online interface. Integrated with Roboflow's trained models, it offers precise analysis of livestock health and behavior, ensuring farmers can identify potential problems quickly. Accessible via Telegram, Agricrypt Chatbot delivers instant alerts and actionable recommendations, making it easy to stay on top of farm management. Designed for simplicity and efficiency, it empowers farmers with cutting-edge technology without the need for complex setups.

**Disclaimer: Agricrypt Chatbot does not replace veterinary care; always consult a vet for professional health advice.**

## Table of Contents
- [Quick Start Guide](https://github.com/Keeks2300/AgriCrypt_Nerdma/blob/main/Quick%20Start%20Guide.md)
- [Links to Demos](#links-to-demos)
- [Chatbot](#chatbot)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application on Google Colab](#running-the-application-on-google-colab)
- [Setting the Telegram Webhook](#setting-the-telegram-webhook)
- [Endpoints](#endpoints)
- [License](#license)

## Quick Start Guide

This is a guide to effectively test Agricrypt Chatbot. For a quick setup and usage guide, refer to the [Quick Start Guide](https://github.com/Keeks2300/AgriCrypt_Nerdma/blob/main/Quick%20Start%20Guide.md)).

## Links to Demos 
- [Demo of trained dataset](https://drive.google.com/file/d/1RPXrhBWUlfLmpZlhXYaB4ZVHMyudQ7Z2/view?usp=sharing)
- [Demo of AI Chat in action](https://drive.google.com/file/d/1NFIEPhK8vmRtLdhW1DvNEW5OXX7bOXSx/view?usp=sharing)
- [Demo of Multi-language Chat](https://drive.google.com/file/d/1rQa9OQEfUvS9IOZyzXkdjMn6-qPpEb3r/view?usp=sharing)

**Please note the project is split in two parts: (1) a chatbot that applies the trained dataset and AI, and (2) A camera simulation see [Quick Start Guide](#quick-start-guide) for more information**

## Chatbot

![QRCode](https://github.com/user-attachments/assets/bacff3ea-de7f-46b6-b82a-77d10c802977)

**To test the chat, click on [TRY ME](https://www.agenthost.ai/chat/agricrypt) and to test it on your mobile device, scan the QR code.**

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
    - Replace `YOUR_PROJECT_NAME` with `Y2024-08-01 5:33pm v1` .
    - Replace `https://chatgpt.com/g/g-xPyvswL5h-agricrypt` with your bot endpoint.

2. **Obtain a Telegram API Token**
    - Go to the [Telegram BotFather](https://telegram.me/botfather).
    - Start a chat with BotFather and use the `/newbot` command to create a new bot.
    - Follow the instructions to name your bot and create a username for it.
    - Once created, you will receive a token. Use this token as your `YOUR_TELEGRAM_BOT_TOKEN`.

3. **Obtain a Roboflow API Key**
    - Go to the [Agricrypy on roboflow](https://app.roboflow.com/agricrypt/agricrypt/1).
    - Sign up for a new account or log in if you already have an account.
    - Navigate to the project settings and find the API key section.
    - Copy the API key and use it as your `YOUR_API_KEY`.

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
    !python app.py
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


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


