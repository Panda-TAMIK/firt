from cgitb import text
from ctypes import resize
from email.errors import InvalidBase64LengthDefect
from turtle import back
import telebot


from telebot import types
Bot = telebot.TeleBot('5763576199:AAGpuYhMu1h4PxLaYjUVOOA826RbTvbWTtc',parse_mode = None)


@Bot.message_handler(commands=['start'])
def start_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton ('Прайс лист')
    item2 = types.KeyboardButton ('Оплата Курса')
    #item3 = types.KeyboardButton ('Доступ к оплаченному курсу ')
    item4 = types.KeyboardButton ('Помощь')

    markup.add(item1,item2,item4)
     #markup.add(item1,item2,item3,item4)

    Bot.send_message(message.chat.id,'Привет,{0.first_name}!Рады видеть тебя🤩Наша команда создала Бота для помощи в подготовке к ЕГЭ! Мы не преподаватели из твоей школы, мы сами сдавали экзамены в течении последних лет и как никто можем помочь тебе справиться с этим этапом. ❤Используй кнопки ниже, для навигации по нашим возможностям😉'.format(message.from_user),reply_markup = markup)

@Bot.message_handler(content_types=['text'])
def bot_message(message):
 if message.chat.type == 'private':



  if message.text == 'Оплата Курса':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    #item1 = types.KeyboardButton('.выбрать нужный кейс')
    #item2 = types.KeyboardButton('Олатить его')
    #item3 = types.KeyboardButton('мы пришлём вам ссылку и ваш личный код для получения доступа к курсу ')
    #item4 = types.KeyboardButton('зайти на курс и тщательно его изучить')
    #item5 = types.KeyboardButton('.забыть про волнение, со спокойной душой и знаниями пойти на экзамен ')
    back = types.KeyboardButton('Назад')
    #markup.add(item1,item2,item3,item4,item5,back)
    markup.add(back)
    Bot.send_message(message.chat.id,'Мы рады, что вас заинтересовал наш продукт🥳Сейчас вам необходимо написать менеджеру')
    Bot.send_message(message.chat.id,'@Bot_pt',reply_markup=markup)

  #elif message.text == 'Доступ к оплаченному курсу':
  #       markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
  #       item1 = types.KeyboardButton('проверить оплату')
  #       item2 = types.KeyboardButton('Перейти к оплаченому курсу')
  #       back = types.KeyboardButton('Назад')
  #       markup.add(item1,item2,back)
  #       Bot.send_message(message.chat.id,'Проверьте оплату после чего мы вышлим вам курс',reply_markup=markup)

  elif message.text == 'Помощь':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    Bot.send_message(message.chat.id, text='Если у вас появились какие-то проблемы или же вопросы, то мы будем рады ответить вам в личных сообщениях с нашим менеджером')
    Bot.send_message(message.chat.id,'@Bot_pt',reply_markup=markup)

  elif message.text == 'Напишите нам':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Назад')
    markup.add(item1) 
    Bot.send_message(message.chat.id,'@Bot_pt',reply_markup=markup)


  elif message.text == 'Назад':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton ('Прайс Лист')
    item2 = types.KeyboardButton ('Оплата Курса')
    #item3 = types.KeyboardButton ('Доступ к оплаченному курсу')
    item4 = types.KeyboardButton ('Помощь')

    markup.add(item1,item2,item4)
#markup.add(item1,item2,item3,item4)
    Bot.send_message(message.chat.id,'Выберите пункт в меню',reply_markup=markup)

  elif message.text == 'Прайс Лист':

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    callback_button = types.InlineKeyboardButton(text="Русский язык", callback_data="test1")
    callback_button1 = types.InlineKeyboardButton(text="Литература", callback_data="test2")
    callback_button2 = types.InlineKeyboardButton(text="Математика (база/проф)", callback_data="test3")
    callback_button3 = types.InlineKeyboardButton(text="Обществознание", callback_data="test4")
    callback_button4 = types.InlineKeyboardButton(text="Английский язык", callback_data="test5")
    callback_button5 = types.InlineKeyboardButton(text="Биология", callback_data="test6")
    callback_button6 = types.InlineKeyboardButton(text="Химия", callback_data="test7")
    callback_button7 = types.InlineKeyboardButton(text="Физика", callback_data="test8")
    callback_button8 = types.InlineKeyboardButton(text="Информатика", callback_data="test9")
    callback_button9 = types.InlineKeyboardButton(text="История", callback_data="test10")


    keyboard.add(callback_button,callback_button1,callback_button2,callback_button3,callback_button9,callback_button4,callback_button5,callback_button6,callback_button7,callback_button8)

    Bot.send_message(message.from_user.id, "Выберите предмет",reply_markup=keyboard)

@Bot.callback_query_handler(func=lambda call:True)
def callback(call):
      if call.data == 'test1':
        Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Русский язык')
        Bot.send_message(call.message.chat.id, text='1. Поможем полностью подготовится к предмету ')
        Bot.send_message(call.message.chat.id, text='2. Подготовка к сочинению и тестовой части')
        Bot.send_message(call.message.chat.id, text='3. Подготовка к тестовой части ')

      elif call.data == 'test2':
         Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Литература')
         Bot.send_message(call.message.chat.id, text=' 1. Поможемм полностью подготовится к предмету ')
         Bot.send_message(call.message.chat.id, text=' 2. Вся необходимая информация, для повторения перед экзаменом + лайфхаки ')
      elif call.data == 'test3':
               Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Математика')
               Bot.send_message(call.message.chat.id, text='1.1. Поможем полностью подготовиться к БАЗОВОЙ МАТЕМАТИКЕ')
               Bot.send_message(call.message.chat.id, text='1.2. Поможем полностью подготовиться к ПРОФИЛЬНОЙ МАТЕМАТИКЕ')
               Bot.send_message(call.message.chat.id, text='2. Краткая информация по ПРОФИЛЬНОЙ МАТЕМАТИКЕ')
               Bot.send_message(call.message.chat.id, text='3.1. Вся необходимая информация, для повторения перед экзаменом + лайфхаки (БАЗОВАЯ МАТЕМАТИКА)')
               Bot.send_message(call.message.chat.id, text='3.2. Вся необходимая информация, для повторения перед экзаменом + лайфхаки (ПРОФИЛЬНАЯ МАТЕМАТИКА)')

      elif call.data == 'test4':
               Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Обществознание')
               Bot.send_message(call.message.chat.id, text='1. Поможем полностью подготовится к предмету ')
               Bot.send_message(call.message.chat.id, text='2. Краткая информация по подготовки к предмету')
               Bot.send_message(call.message.chat.id, text='3. Вся необходимая информация, для повторения перед экзаменом + лайфхаки ')

      elif call.data == 'test5':
               Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Английский язык')
               Bot.send_message(call.message.chat.id, text='1. Поможем полностью подготовится к предмету')
               Bot.send_message(call.message.chat.id, text='2. Краткая информация по подготовки к предмету ')
               Bot.send_message(call.message.chat.id, text='3. Вся необходимая информация, для повторения перед экзаменом + лайфхаки' )

      elif call.data == 'test6':
         Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Биология')
         Bot.send_message(call.message.chat.id, text='1. Поможем полностью подготовится к предмету ')
         Bot.send_message(call.message.chat.id, text='2. Краткая информация по подготовки к предмету ')
         Bot.send_message(call.message.chat.id, text='3. Вся необходимая информация, для повторения перед экзаменом + лайфхаки ')

      elif call.data == 'test7':
         Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Химия')
         Bot.send_message(call.message.chat.id, text='1. Поможем полностью подготовится к предмету ')
         Bot.send_message(call.message.chat.id, text='2. Краткая информация по подготовки к предмету ')
         Bot.send_message(call.message.chat.id, text='3. Вся необходимая информация, для повторения перед экзаменом + лайфхаки ')

      elif call.data == 'test8':
         Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Физика')
         Bot.send_message(call.message.chat.id, text='1. Поможем полностью подготовится к предмету ')
         Bot.send_message(call.message.chat.id, text='2. Краткая информация по подготовки к предмету ')
         Bot.send_message(call.message.chat.id, text='3. Вся необходимая информация, для повторения перед экзаменом + лайфхаки ')
      elif call.data == 'test9':
         Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Инорматика')
         Bot.send_message(call.message.chat.id, text='1. Поможем полностью подготовится к предмету ')
         Bot.send_message(call.message.chat.id, text='2. Краткая информация по подготовки к предмету ')
         Bot.send_message(call.message.chat.id, text='3. Вся необходимая информация, для повторения перед экзаменом + лайфхаки ')
         Bot.send_message(call.message.chat.id, text='')
      elif call.data == 'test10':
         Bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'История')
         Bot.send_message(call.message.chat.id, text='1. Поможем полностью подготовится к предмету ')
         Bot.send_message(call.message.chat.id, text='2. Краткая информация по подготовки к предмету ')
         Bot.send_message(call.message.chat.id, text='3. Вся необходимая информация, для повторения перед экзаменом + лайфхаки ')

Bot.polling(none_stop=True)