# -*- coding: utf-8 -*-
import config
import telebot as tb
import requests
# import numpy as np
# import cv2
import video_processing
import  sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb')

bot = tb.TeleBot(config.token)
# TODO play with tg bot
# TODO try parallel handling images
@bot.message_handler(content_types=["photo"])
def repeat_all_messages(message):
  photo_id = message.photo[2].file_id # index specifies size of an image
  # download_file and save it
  file_info = bot.get_file(photo_id)
  downloaded_file = bot.download_file(file_info.file_path)
  print('-------------------------------------------------------------------')
  print( file_info.file_path.split('.')[-1]  )
  print(file_info.file_path.split('.')[0])
  extension = file_info.file_path.split('.')[-1]
  filename = '/' + file_info.file_path.split('.')[0] + '.' + extension
  with open(filename,'wb') as new_file:
    new_file.write(downloaded_file)

  if new_file:
    video_processing.handle_image(filename)
    video = open('output.mp4', 'rb')
    bot.send_video_note(message.chat.id, video)
# opencv work
# face_cascade = cv2.CascadeClassifier('/home/edwinna/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
# bot.send_photo(chat_id=message.chat.id, photo=open('detected_faces/new_file.png', 'rb'))

if __name__ == '__main__':
 #  while True:
    # try:
  bot.polling(none_stop=True)
    # except Exception as ex:
    #   print('')
