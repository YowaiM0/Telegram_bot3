#импортируем библиотеку 
import telebot 
#наш токен 
from bote import TOKEN 

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])


def text_message(message):
    lines=message.text.split('\n')
    lines_amount=message.text.count('\n') +1

    if not 3<= lines_amount <= 11:
        return bot.send_message(chat_id = message.chat.id, text ='В Вашем сообщении должно быть от 3 до 11 строк  \U0001F6A8 ')
    
    bot.send_poll(message.chat.id, lines[0], lines[1:])




if __name__ == '__main__' :
    bot.infinity_polling()  
   
