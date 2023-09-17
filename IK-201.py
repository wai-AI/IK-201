import telebot
import datetime
import time

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

time_now = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

print("Start...")

@bot.message_handler(commands=['lessons'])
def get_user_text(message):
    try:
        bot.send_message(message.chat.id,'<b>Дискретка: </b> <a href = "https://us02web.zoom.us/j/6757933043?pwd=UlpuOGRzVTRUdkRoTnNMMG9CRWhwZz09"> Перейти </a> \n'
                                        '\n'
                                        '<b>Крипта (лекція):</b> <a href = "https://us05web.zoom.us/j/86246664838?pwd=v0YCXlXK4eQgbPK0HubQkA9lbBkSBv.1"> Перейти </a> \n'
                                        '\n'
                                        '<b>Крипта (практика): </b> <a href = "https://us05web.zoom.us/j/87832280496?pwd=V9F7yWbGOf1Kreo5bRHqjborrlKCYo.1"> Перейти </a> \n'
                                        '\n'
                                        '<b>Алгоритми: </b> <a href = "https://us04web.zoom.us/j/76854073083?pwd=Rb4o7hdj5Rd7mX1zz5ebxzklgIdjVh.1"> Перейти </a> \n'
                                        '\n'
                                        '<b>Труш:</b> <a href = "https://us04web.zoom.us/j/74898611963?pwd=ajFtS1Y3dlVZVGhqRDV1djZTMXN6dz09"> Перейти </a> \n'
                                        '\n'
                                        '<b>ТМС: </b> <a href = "https://us02web.zoom.us/j/83810477083?pwd=NTBKNWxBajk2WFFDSG04aFhFNitsZz09"> Перейти </a>', parse_mode='html')

    except Exception as e:
        print("Error 1: ", e)

@bot.message_handler(commands=['emails'])
def emails(message):
    try:
        bot.send_message(message.chat.id,'<b>ФІЗРА ПЛАВАННЯ</b> - yanishevskiy62@ukr.net \n'
                                        '\n'
                                        '<b>ФІЗРА ФІТНЕС</b> - dorika2@ukr.net \n'
                                        '\n'
                                        '<b>ФІЗРА БАСКЕТ</b> - Marysia_rachok@icloud.com \n'
                                        '\n'
                                        '<b>ФІЗРА ФУТБОЛ</b> - ssobotiuk@gmail.com \n'
                                         '\n'
                                        '<b>КРИПТА</b> - naghirnaalla@ukr.net \n'
                                        '\n'
                                        '<b>ХМАРА</b> - olkam@kneu.edu.ua \n', parse_mode='html')
    except Exception as e:
        print("Error 2: ", e)

@bot.message_handler(commands=['timetable'])
def emails(message):
    week_number = datetime.datetime.today().isocalendar()[1]
    week_day = datetime.datetime.today().weekday()
    hour_str = time.strftime('%H', time.localtime())
    hour = int(hour_str)
    if week_number % 2 == 0: #Нижняя
        if week_day == 0 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПонедельникНижний.png', 'rb'), caption = '<b>Понеділок (Нижній)</b>', parse_mode = 'html')
        elif week_day == 0 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ВторникНижний.png', 'rb'), caption = '<b>Вівторок (Нижній)</b>', parse_mode = 'html')
        elif week_day == 1 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ВторникНижний.png', 'rb'), caption = '<b>Вівторок (Нижній)</b>', parse_mode = 'html')
        elif week_day == 1 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/СредаНижний.png', 'rb'), caption = "<b>Середа (Нижній)</b>", parse_mode = 'html')
        elif week_day == 2 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/СредаНижний.png', 'rb'), caption = "<b>Середа (Нижній)</b>", parse_mode = 'html')
        elif week_day == 2 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ЧетвергНижний.png', 'rb'), caption = '<b>Четвер (Нижній)</b>', parse_mode = 'html')
        elif week_day == 3 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ЧетвергНижний.png', 'rb'), caption = '<b>Четвер (Нижній)</b>', parse_mode = 'html')
        elif week_day == 3 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПятницаНижний.png', 'rb'), caption = "<b>П'ятниця (Нижній)</b>", parse_mode = 'html')
        elif week_day == 4 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПятницаНижний.png', 'rb'), caption = "<b>П'ятниця (Нижній)</b>", parse_mode = 'html')
        elif week_day == 4 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПонедельникВерхний.png', 'rb'), caption = '<b>Понеділок (Верхній)</b>', parse_mode = 'html')
        elif (week_day == 5 or week_day == 6) and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПонедельникВерхний.png', 'rb'), caption = '<b>Понеділок (Верхній)</b>', parse_mode = 'html')
        elif (week_day == 5 or week_day == 6) and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПонедельникВерхний.png', 'rb'), caption = '<b>Понеділок (Верхній)</b>', parse_mode = 'html')
    elif week_number % 2 != 0: #Верхняя
        if week_day == 0 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПонедельникВерхний.png', 'rb'), caption = '<b>Понеділок (Верхній)</b>', parse_mode = 'html')
        elif week_day == 0 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ВторникВерхний.png', 'rb'), caption = '<b>Вівторок (Верхній)</b>', parse_mode = 'html')
        elif week_day == 1 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ВторникВерхний.png', 'rb'), caption = '<b>Вівторок (Верхній)</b>', parse_mode = 'html')
        elif week_day == 1 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/СредаВерхний.png', 'rb'), caption = "<b>Середа (Нижній)</b>", parse_mode = 'html')
        elif week_day == 2 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/СредаВерхний.png', 'rb'), caption = "<b>Середа (Нижній)</b>", parse_mode = 'html')
        elif week_day == 2 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ЧетвергВерхний.png', 'rb'), caption = '<b>Четвер (Верхній)</b>', parse_mode = 'html')
        elif week_day == 3 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ЧетвергВерхний.png', 'rb'), caption = '<b>Четвер (Верхній)</b>', parse_mode = 'html')
        elif week_day == 3 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПятницаВерхний.png', 'rb'), caption = "<b>П'ятниця (Верхній)</b>", parse_mode = 'html')
        elif week_day == 4 and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПятницаВерхний.png', 'rb'), caption = "<b>П'ятниця (Верхній)</b>", parse_mode = 'html')
        elif week_day == 4 and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПонедельникНижний.png', 'rb'), caption = '<b>Понеділок (Нижній)</b>', parse_mode = 'html')
        elif (week_day == 5 or week_day == 6) and hour<11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПонедельникНижний.png', 'rb'), caption = '<b>Понеділок (Нижній)</b>', parse_mode = 'html')
        elif (week_day == 5 or week_day == 6) and hour>=11:
            bot.send_photo(message.chat.id, open(r'/data/data/com.termux/files/home/projects/IK-201/ПонедельникНижний.png', 'rb'), caption = '<b>Понеділок (Нижній)</b>', parse_mode = 'html')

@bot.message_handler(commands=['test'])
def message_to_group(message):
    if message.from_user.username == "Zakhiel":
        mess = bot.send_message(message.chat.id, "Введите сообщение:")
        bot.register_next_step_handler(mess, send_message_to_group)
    else:
        bot.send_message(message.from_user.id, "В доступе отказано!")

def send_message_to_group(message):
    if message.text != "/end":
        mess = message.text
        #IK101
        id = -1001386447243
        #Test
        #id = -1001888106740
        bot.send_message(id, mess)
        message_to_group(message)
    else:
        bot.send_message(message.chat.id, "Вы завершили сессию.")

bot.infinity_polling(timeout=10, long_polling_timeout = 5)
