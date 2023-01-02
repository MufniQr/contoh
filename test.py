import pyautogui as spam
import time

limit = input("masukkan nomor message")
msg = input("masukkan pesan")

i = 0
time.sleep(5)

while i<int(limit):

    spam.typewrite(msg)
    spam.press('Enter')

    i+=1
