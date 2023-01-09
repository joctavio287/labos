import telegram
def notify_ending(message):
    token = '5448153732:AAGhKraJQquEqMfpD3cb4rnTcrKB6U1ViMA'
    chat_id = '1034347542'
    bot = telegram.Bot(token = token)
    bot.sendMessage(chat_id = chat_id, text = message)