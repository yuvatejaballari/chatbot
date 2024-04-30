pip install chatterbot

# Create a new instance of a ChatBot
bot = ChatBot(
    'MyChatBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the English corpus
trainer.train("chatterbot.corpus.english")

print("Hello! I am your chatbot. How can I assist you today?")

while True:
    user_input = input("You: ")

    # Get the bot's response to the user input
    bot_response = bot.get_response(user_input)

    print("Bot:", bot_response)
