from colorama import Fore, Back, Style #library color terminal
import pyowm #library pogoda 2.5.0
import telebot #library telegram bot 3.7.2
import time
from random import randint
from telebot import types
import version
ver=version.version
prover=version.proversion


owm =  pyowm.OWM('8a8ff169b5ef401f1c41473d82d40336', language = 'ua') #API keys pogoda
bot=telebot.TeleBot("1089186238:AAGVgaJ7Lz8Fhtm3DrEBlwZVvTvIz1oKSrM") #Api keys telegram bot pogoda
bot1=telebot.TeleBot("1127913180:AAHzMKApIvFp6QCUxSQ7iJyfEX3Ht_EbNHw")

sssr1=1
sssr2=['P6vaD8zmrfg','yL4eIUTovLM','Dboi1bja6M8','QwdbFNGCkLw']
sssr=sssr1+len(sssr2)-1

@bot.message_handler(commands=['start','menu'])
def menu(message):
    markup=telebot.types.ReplyKeyboardMarkup(True, True)
    if message.chat.id==873414523:
        markup.row('info','version')
        markup.row('pro version')
    else:
        markup.row('info','version')
    bot.send_message(message.from_user.id, 'Меню: ', reply_markup=markup)


@bot.message_handler(content_types=['text']) #bot send text 
def send_echo(message): #function
    try: #if dont error
        print(Back.WHITE)#color terminal background // when error
        print(Fore.GREEN)#color terminal front // when error
        answer='ᅠ'
        observ=owm.weather_at_place(message.text) #dostayem pogodu
        w=observ.get_weather() #pereroblyem pogodu
        temp=w.get_temperature('celsius')["temp"] #distayem temperature 
        volog=w.get_humidity() #distayem vologict
        viter=w.get_wind()['speed']
        smail=''
        if w.get_detailed_status()=="рвані хмари":
            smail='🌤'
        elif w.get_detailed_status()=="легкий дощ":
            smail='🌧'
        elif w.get_detailed_status()=='хмарно':
            smail='☁'
        elif w.get_detailed_status()=='чисте небо':
            smail='☀'
        elif w.get_detailed_status()=="кілька хмар":
            smail='⛅'
        elif w.get_detailed_status()=="гроза":
            smail=' 🌩'
        else:
            smail='⭐'
        ('''if w.get_detailed_status()=="рвані хмари":
           answer="__________________$\n"
           answer+="____________$_____$_______$\n"
           answer+="______$_____$$___$$_____$$\n"
           answer+="_______$$___$$$_$$$___$$$\n"
           answer+="_$______$$$$$$$$$$$$$$$$\n"
           answer+="___$$$__$$$_______$$$$\n"
           answer+="____$$$$$___________$$\n"
           answer+="_______$____________$$$$$\n"
           answer+="____$$$$____________$$$$$$$\n"
           answer+="$$$$$$$$$___________$$$$$$$$$\n"
           answer+="_______$$$___$$$$$$$_______$$$$\n"
           answer+="______$$$$$$$$_____$________$$$\n"
           answer+="____$_____$$$$_______________$$$$$\n"
           answer+="__$______$$__$___________________$$\n"
           answer+="$_____$$$__________$___________$$$\n"
           answer+="_______$$$$$$$$$___$$$$$______$$$$\n"
           answer+="__________$$$__$$$$$__$$$$$$$$$$\n"
           

        else:
            answer="__________¶____¶_________________________________\n"
            answer+="__________¶¶__¶¶___¶_____________________________\n"
            answer+="______¶¶__¶¶¶_¶¶__¶¶___¶¶________________________\n"
            answer+="______¶¶¶¶_¶¶¶¶¶¶¶¶¶_¶¶¶_________________________\n"
            answer+="___¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________________________\n"
            answer+="___¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶____________________\n"
            answer+="_____¶¶¶¶_______¶¶¶¶¶¶¶__¶¶¶¶¶¶¶_________________\n"
            answer+="_¶¶¶¶¶¶¶_______¶¶¶____________¶¶¶________________\n"
            answer+="__¶¶¶¶¶¶______¶¶________________¶¶¶¶¶¶___________\n"
            answer+="_____¶¶______¶¶__________________¶¶¶¶¶¶¶_________\n"
            answer+="_¶¶¶¶¶¶______¶¶_______________________¶¶¶________\n"
            answer+="_¶¶¶¶¶¶¶__¶¶¶¶_________________________¶¶________\n"
            answer+="_____¶¶¶¶¶¶¶¶¶_________________________¶¶________\n"
            answer+="___¶¶¶¶¶_______________________________¶¶¶¶______\n"
            answer+="__¶¶¶¶___________________________________¶¶¶¶____\n"
            answer+="___¶¶_______________________________________¶¶___\n"
            answer+="___¶________________________________________¶¶___\n"
            answer+="__¶¶_________________________________________¶¶__\n"
            answer+="___¶¶_______________________________________¶¶___\n"
            answer+="___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___\n"
            answer+="_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____\n"
            answer+="_________________________________________________\n"
            print(w.get_detailed_status())''')
        a="В "+message.text+" зараз "+w.get_detailed_status()+' '+smail+'\n'
        b="Зараз температура "+str(temp)+ "°С"
        c="Вологість зараз - "+str(volog)+"%"+"\n" #vidpovid bota
        d="Швидкість вітру зараз "+str(viter)+"m/s"+'\n'
        a2=len(a)
        b2=len(b)
        c2=len(c)
        d2=len(d)
        if a2>b2:
            a3=a2
        else:
            a3=b2
        if c2>d2:
            b3=c2
        else:
            b3=d2
        if a3>b3:
            a3+=0
        else:
            a3=b3

        a1=int((a3)/1.25)*'--'+'\n'
        f=int(((len(a1)-len(a))/2))*' '
        f1=int(((len(a1)-len(b))/2)+2)*' '
        f2=int(((len(a1)-len(c))/2)+2)*' '
        f3=int(((len(a1)-len(d))/2)+2)*' '
        answer+=f+a+a1+f1+b+'  🌡'+'\n'+a1+f2+c+a1+f3+d+a1
        answer=answer.upper()
        ('''if temp<0: # if po temperature
            answer+="На вулиці морозно, вдінся тепло... Бррр..."+"\n"
        elif temp<10:
            answer+="Там холодно, курточку надо)"+"\n"
        elif temp<20:
            answer+="Нууу... куртку надо, но якщо ти машина..."+"\n"
        else:
            answer+="Якраз щоб на турнічки ходити))"+"\n"
        if volog<65: #if po vologict
            answer+="Дощу не буде!"
        elif volog<85:
            answer+="Є шанс на дощ..."
        else:
            answer+="Дощу бути)))"''')
        bot.send_message(message.chat.id, answer) #bot vidpravlyae
        print(Back.BLACK) #color terminal background // dont error // info
        print(Fore.GREEN) #color terminal front // dont error // info
        if isinstance(message.chat.first_name,str)==True and isinstance(message.chat.last_name,str)==True and isinstance(message.chat.username,str)==True:
            name=message.chat.last_name+" "+message.chat.first_name+"\n"+str(message.chat.id)+" \n@"+message.chat.username
        elif isinstance(message.chat.first_name,str)==True and isinstance(message.chat.last_name,str)==True:
            name=message.chat.last_name+" "+message.chat.first_name+"\n"+str(message.chat.id)
        else:
            name=str(message.chat.id)
        namem=name+"  "+message.text+"  "+time.asctime()
        namem1=name+"  "+message.text
        namem2=name+"\n"+message.text+'\n'+smail+" *"+w.get_detailed_status()+'*\n'+time.asctime()
        bot1.send_message(873414523, namem2, parse_mode= "Markdown")
        namems=namem+'\n' #slegka
        my_file = open('basadanih.txt','a') #file slegki
        my_file.write(namems)
        my_file.close()
        print(namem1)
    except: # if do error
        global sssr
        if message.text=='info':
            answer="Я - телеграм бот погоди!🌤\n"
            answer+="Напиши мені назву країни, міста, села\n"
            answer+="І я надішлю погоду на даний момент🕖"
            bot.send_message(message.chat.id, answer)
        elif message.text=='version':
            bot.send_message(message.chat.id, ver)
        elif message.text=='pro version':
            bot.send_message(message.chat.id, prover)
        elif message.text.lower()=='ricardo milos' or message.text.lower()=='рікардо мілос' or message.text.lower()=='рикардо милос' or message.text.lower()=='рікардо милос':
            photo = open('ricardo.gif', 'rb')
            bot.send_video_note(message.chat.id, photo)
        elif message.text.lower()=='ссср':
            random=randint(1,sssr)
            if random<=sssr1:
                jpg=str(random)+'ссср.jpg'
                photo = open(jpg, 'rb')
                bot.send_photo(message.chat.id, photo)
            else:
                sssr3=random-sssr1
                bot.send_message(message.chat.id, "www.youtube.com/watch?v="+sssr2[sssr3])
        elif message.text=='пасхалки':
            markup1=telebot.types.ReplyKeyboardMarkup(True, True)
            markup1.row('ricardo milos')
            markup1.row('ссср')
            #markup1.row('')
            bot.send_message(message.from_user.id, 'Пасхалки: ', reply_markup=markup1)
        else:
            bot.send_message(message.chat.id, "error: try again")
            if isinstance(message.chat.first_name,str)==True and isinstance(message.chat.last_name,str)==True and isinstance(message.chat.username,str)==True:
                name=message.chat.last_name+" "+message.chat.first_name+"  "+str(message.chat.id)+" @"+message.chat.username
            elif isinstance(message.chat.first_name,str)==True and isinstance(message.chat.last_name,str)==True:
                name=message.chat.last_name+" "+message.chat.first_name+"  "+str(message.chat.id)
            else:
                name=str(message.chat.id)
            namem=name+"  "+message.text+"  "+time.asctime()
            namem1=name+"  "+message.text
            namem2=name+"\n"+message.text+"\n"+time.asctime()
            bot1.send_message(873414523, namem2)
            namems=namem+'\n' #slegka
            my_file = open('basadanih.txt','a') #file slegki
            my_file.write(namems)
            my_file.close()
            print(namem1)
            print("error")
bot.infinity_polling(True) #povtoryuvati zavgdi
