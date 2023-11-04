import datetime
import time
import json
from back import keep_alive

#This bot was created by @SWQTR. If you have any suggestions and ideas for optimizing and improving the bot, please contact me through Telegram." 

with open('config.json', 'r') as config_file:
  config_data = json.load(config_file)

# Отримайте доступ до окремих полів конфігурації
telegram_token = config_data['TOKEN']
path = config_data['path']
time_c = config_data['time']

TIME = int(time_c)

bot = telebot.TeleBot(telegram_token)

time_now = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

print("Start...")


@bot.message_handler(commands=['lessons']) #блок з посиланнями на пару
def get_user_text(message):
  try: 
    bot.send_message(
        message.chat.id,
        '<b>Дискретка: </b> <a href = ""> Перейти </a> \n'
        '\n'
        '<b>Крипта (лекція):</b> <a href = ""> Перейти </a> \n'
        '\n'
        '<b>Крипта (практика): </b> <a href = ""> Перейти </a> \n'
        '\n'
        '<b>Бізнес інформатика: </b> <a href = ""> Перейти </a> \n'
        '\n'
        '<b>Лютий: </b> <a href = ""> Перейти </a> \n'
        '\n'
        '<b>Алгоритми: </b> <a href = ""> Перейти </a> \n'
        '\n'
        '<b>Хмара: </b> <a href = ""> Перейти </a> \n'
        '\n'
        '<b>Труш:</b> <a href = ""> Перейти </a> \n'
        '\n'
        '<b>ТМС: </b> <a href = ""> Перейти </a>',
        parse_mode='html')

  except Exception as e:
    print("Error 1: ", e)


@bot.message_handler(commands=['emails']) #блок з поштами викладачів
def emails(message):
  try:
    bot.send_message(message.chat.id,
                     '<b>ФІЗРА ПЛАВАННЯ</b> -  \n'
                     '\n'
                     '<b>ФІЗРА ФІТНЕС</b> -  \n'
                     '\n'
                     '<b>ФІЗРА БАСКЕТ</b> -  \n'
                     '\n'
                     '<b>ФІЗРА ФУТБОЛ</b> -  \n'
                     '\n'
                     '<b>КІБЕРБЕЗПЕКА</b> -  \n'
                     '\n'
                     '<b>ЗМІЄВУСТ</b> - \n'
                     '\n'
                     '<b>КРИПТА</b> -  \n'
                     '\n'
                     '<b>ХМАРА</b> -  \n',
                     parse_mode='html')
  except Exception as e:
    print("Error 2: ", e)


@bot.message_handler(commands=['timetable']) #Блок з розкладом
def emails(message):
  week_number = datetime.datetime.today().isocalendar()[1]
  week_day = datetime.datetime.today().weekday()
  hour_str = time.strftime('%H', time.localtime())
  hour = int(hour_str)
  if week_number % 2 == 0:  #Нижняя
    if week_day == 0 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПонедельникНижний.png', 'rb'),
                     caption='<b>Понеділок (Нижній)</b>',
                     parse_mode='html')
    elif week_day == 0 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ВторникНижний.png', 'rb'),
                     caption='<b>Вівторок (Нижній)</b>',
                     parse_mode='html')
    elif week_day == 1 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ВторникНижний.png', 'rb'),
                     caption='<b>Вівторок (Нижній)</b>',
                     parse_mode='html')
    elif week_day == 1 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}СредаНижний.png', 'rb'),
                     caption="<b>Середа (Нижній)</b>",
                     parse_mode='html')
    elif week_day == 2 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}СредаНижний.png', 'rb'),
                     caption="<b>Середа (Нижній)</b>",
                     parse_mode='html')
    elif week_day == 2 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ЧетвергНижний.png', 'rb'),
                     caption='<b>Четвер (Нижній)</b>',
                     parse_mode='html')
    elif week_day == 3 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ЧетвергНижний.png', 'rb'),
                     caption='<b>Четвер (Нижній)</b>',
                     parse_mode='html')
    elif week_day == 3 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПятницаНижний.png', 'rb'),
                     caption="<b>П'ятниця (Нижній)</b>",
                     parse_mode='html')
    elif week_day == 4 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПятницаНижний.png', 'rb'),
                     caption="<b>П'ятниця (Нижній)</b>",
                     parse_mode='html')
    elif week_day == 4 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПонедельникВерхний.png', 'rb'),
                     caption='<b>Понеділок (Верхній)</b>',
                     parse_mode='html')
    elif (week_day == 5 or week_day == 6) and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПонедельникВерхний.png', 'rb'),
                     caption='<b>Понеділок (Верхній)</b>',
                     parse_mode='html')
    elif (week_day == 5 or week_day == 6) and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПонедельникВерхний.png', 'rb'),
                     caption='<b>Понеділок (Верхній)</b>',
                     parse_mode='html')
  elif week_number % 2 != 0:  #Верхняя
    if week_day == 0 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПонедельникВерхний.png', 'rb'),
                     caption='<b>Понеділок (Верхній)</b>',
                     parse_mode='html')
    elif week_day == 0 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ВторникВерхний.png', 'rb'),
                     caption='<b>Вівторок (Верхній)</b>',
                     parse_mode='html')
    elif week_day == 1 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ВторникВерхний.png', 'rb'),
                     caption='<b>Вівторок (Верхній)</b>',
                     parse_mode='html')
    elif week_day == 1 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}СредаВерхний.png', 'rb'),
                     caption="<b>Середа (Нижній)</b>",
                     parse_mode='html')
    elif week_day == 2 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}СредаВерхний.png', 'rb'),
                     caption="<b>Середа (Нижній)</b>",
                     parse_mode='html')
    elif week_day == 2 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ЧетвергВерхний.png', 'rb'),
                     caption='<b>Четвер (Верхній)</b>',
                     parse_mode='html')
    elif week_day == 3 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ЧетвергВерхний.png', 'rb'),
                     caption='<b>Четвер (Верхній)</b>',
                     parse_mode='html')
    elif week_day == 3 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПятницаВерхний.png', 'rb'),
                     caption="<b>П'ятниця (Верхній)</b>",
                     parse_mode='html')
    elif week_day == 4 and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПятницаВерхний.png', 'rb'),
                     caption="<b>П'ятниця (Верхній)</b>",
                     parse_mode='html')
    elif week_day == 4 and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПонедельникНижний.png', 'rb'),
                     caption='<b>Понеділок (Нижній)</b>',
                     parse_mode='html')
    elif (week_day == 5 or week_day == 6) and hour < TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПонедельникНижний.png', 'rb'),
                     caption='<b>Понеділок (Нижній)</b>',
                     parse_mode='html')
    elif (week_day == 5 or week_day == 6) and hour >= TIME:
      bot.send_photo(message.chat.id,
                     open(f'{path}ПонедельникНижний.png', 'rb'),
                     caption='<b>Понеділок (Нижній)</b>',
                     parse_mode='html')

keep_alive()
bot.infinity_polling(timeout=10, long_polling_timeout=5)