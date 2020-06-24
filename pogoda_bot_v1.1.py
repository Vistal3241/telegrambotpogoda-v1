from colorama import Fore, Back, Style
import pyowm
import telebot
owm =  pyowm.OWM('8a8ff169b5ef401f1c41473d82d40336', language = "ua")
bot=telebot.TeleBot("1089186238:AAGVgaJ7Lz8Fhtm3DrEBlwZVvTvIz1oKSrM")
print(Back.BLACK)
print(Fore.GREEN)
@bot.message_handler(content_types=['text'])
def send_echo(message):
    name=message.chat.last_name+" "+message.chat.first_name
    print(name+"  "+message.text)
    observ=owm.weather_at_place(message.text)
    w=observ.get_weather()
    temp=w.get_temperature('celsius')["temp"]
    volog=w.get_humidity()
    answer="В "+message.text+" зараз "+w.get_detailed_status()+"\n"
    answer+="Зараз температура "+str(temp)+ "С"+"\n"
    answer+="Вологість зараз - "+str(volog)+"%"+"\n\n"
    if temp<0:
        answer+="На вулиці морозно, вдінся тепло... Бррр..."+"\n"
    elif temp<10:
        answer+="Там холодно, курточку надо)"+"\n"
    elif temp<20:
        answer+="Нууу... куртку надо, но якщо ти машина..."+"\n"
    else:
        answer+="Якраз щоб на турнічки ходити))"+"\n"
    if volog<65:
        answer+="Дощу не буде!"
    elif volog<85:
        answer+="Є шанс на дощ..."
    else:
        answer+="Дощу бути)))"
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True)
