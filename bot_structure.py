import config
from DBhandle import DBhandle
import telebot
import datetime
import os


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def autorization(message):
    bot.reply_to(message, 'Верификация: введи свой тг в текстовое поле (login):' )
    
    username = user.first_name  #message.from_user.first_name + ' ' + str(message.chat.id)
    user_id = '-just start-'
    mtext = message.text
    
    data = [(username, message.chat.id, mtext)]
    dbinit = DBhandle().simpleRecording(data)
    
    

@bot.message_handler(func=lambda message: message.text == 'my_username' or message.text =='users_username')  # wat
def doshit(message):
    bot.send_message(message.chat.id, 'Привет. С днем рождения!')
    
    username = message.from_user.first_name  # + ' ' + str(message.chat.id)
    user_id = user.id
    mtext = message.text
    
    data = [(username, message.chat.id, user_id, mtext)]
    
    dbinit = DBhandle().recording(data)
    #dbinit.recording(data)

    
    # Первое сообщение отправленое после старт, содержит переменную логин, которую необходимо отправить на проверку
    # Атрибуты, которые нужно извлечь для работы над этой переменной: chat_id / message_id  OR
    # Записать значения в базу данных (возможно, файл \ лог). Сделать вывод лога доступный по команде. Переменные: текст и время
    # ЗАПОМНИТЬ ПОЛЬЗОВАТЕЛЯ (айди контакт)
    
    # УСЛОВИЕ: Если пользователь не авторизирован, он не имеет возможности получать сообщения. 
    # Вариант 1. Зацикленная проверка. 
    # Вариант 2. Привилегии.
    
    # Сделать возможным отложенную отправку (представление рассылки, возможно) в назначенное время, назначенного дня. 
    # Пока день(!) не наступил, составить ответ на входящие сообщения
    
# commands for output 
@bot.message_handler(commands=['cttt'])
def checkout(message):
    dbinit = DBhandle().get_user_info()
    bot.send_message(message.chat.id, dbinit)
    
    
    
# отправить сообщение по юзер айди, отправить сообщение по чат айди,
@bot.message_handler(commands=['dothissomething'])  # send message work only with message.chat_id
def send_the_text(message):
    bot.send_message(message.chat.id, text='text some message')
    


@bot.message_handler(func=lambda message: True)
def repeat(message):
    msg='|'+message.text+'|'+message.chat.id+'|'+message.from_user.first_name
    bot.send_message(my_chat_id, text=msg)


if __name__ == '__main__':
    
    dbinit = DBhandle().setup()
    
    bot.polling(none_stop=False, interval=0, timeout=20)

# if she say: how can i find out, what commands this RoBoT contains