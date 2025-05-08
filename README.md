# Rasa Language Learning Chatbot: English-Russian Vocabulary Practice

This bot is designed to help you practice translating English to Russian. Whether you're just starting out or want to refresh your skills, the chatbot makes learning fun and interactive.

The way it works is simple: you’ll be given an English word to translate into Russian. If you get it right, awesome! If not, no worries—the bot will gently correct you and keep things moving so you can learn at your own pace. It’s all about making language practice more engaging and less intimidating.

## What It Does

    Interactive Learning: The bot will give you English words to translate into Russian and give feedback based on your answers.

    Real-Time Feedback: If you make a mistake, the bot will kindly correct you and move on to the next word so you can keep learning.

    Flexible: Right now, it’s set up for English to Russian, but you can easily switch it to Russian to English or any other language you want.


## What You Need:

Make sure you have:

    Python (version 3.6 or later)

    Rasa Open Source (You can find the installation guide on the Rasa website).

## Setup Instructions:

    Clone the repo:

git clone https://github.com/thecognicode/Rasa-EN-RU-bot.git

cd Rasa-chatbot

## Install required packages:

First, create a virtual environment (depends on OS you use).


## Download language models:

If you're working with more languages, grab the language models from the Rasa website.

### Run the following command to train the model using the data:

rasa train

### Run the bot:

rasa run actions (run this in one terminal)

Then open another terminal and type:
rasa shell (don't forget to activate your virtual environment before running this command/it applies for rasa run actions too if you opened it in a separate terminal)

##  Et voilà! Now you can start learning a few new words each day by chatting with the bot💛
