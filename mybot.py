import telebot
import mysql.connector

import mytoken


from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start'])
    def start(message):
        photo = open('img/rpl2.jpg', 'rb')
        myBot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n-- admin & developer @IrsyaALiffio - SMK Taruna Bhakti -- "+"\n" \
                                "Mungkin kamu harus ketik /help terlebih dahulu untuk mengetahui fitur lainnya"+"\n" \
                        "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['help'])
    def help(message):
        teks = mytoken.SAPA + "\n-- HALLO SAYA WO BOT ASISTEN KAMU SEKARANG -- "+"\n" \
                              "Aku bisa membantu kamu dengan perintah:"+"\n" \
                              "/start : Untuk memulai"+"\n" \
                              "/help : Untuk melihat apa yang bisa bot ini lakukan"+"\n" \
                              "/datasiswa : Untuk melihat data siswa XI RPL 1 dan XI RPL 2"+"\n"
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="\n select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata=''
        if(jmldata>0):
            print(data)
            no=0
            for x in data:
                no += 1
                kumpuldata =kumpuldata+ str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)
