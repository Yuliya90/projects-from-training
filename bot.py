
import telebot
bot = telebot.TeleBot('7297271282:AAHXYtJe0wBdVMbGN1PGQMvdukYKKACk7xQ')
import pickle
with open('Pickle_RL_Model.pkl', 'rb') as file:
    Pickled_LR_Model = pickle.load(file)
Pickled_LR_Model


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Я бот-помощник по подбору программиста Python. Напиши свой опыт работы подробно.')
bot.polling(none_stop=True)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = Pickled_LR_Model.predict(message.text)
    bot.send_message(response)
bot.polling(none_stop=True)



