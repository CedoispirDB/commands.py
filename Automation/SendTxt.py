import random
import pyautogui as p
import time as t
import os
import webbrowser
from os import listdir
from os.path import isfile, join
from datetime import datetime

global currentFile

def sendFile():
    w, h = p.size()
    print(w, h)
    # p.click((101 / 288) * w, (8/9) * h)
    p.click((101 / 288) * w, (8/9) * h)
    p.click((101 / 288) * w, (747 / 900) * h)
    t.sleep(1)
    p.click((509 / 1440) * w, (224 / 900) * h)
    t.sleep(1)
    p.click((1068 / 1440) * w, (534 / 900) * h)
    t.sleep(1)
    p.press("enter")


def copyFile():
    path = "/Users/marcobarreirinhas1/Desktop/iFun"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    currentFile = files[random.randint(0, len(files))]
    os.system("cp /Users/marcobarreirinhas1/Desktop/iFun/" + currentFile + " /Users/marcobarreirinhas1/Downloads/")
    os.system("mv /Users/marcobarreirinhas1/Downloads/" + currentFile + " /Users/marcobarreirinhas1/Downloads/a.jpg")

def clean():
    os.system("rm /Users/marcobarreirinhas1/Downloads/a.jpg")

def openBrowser():
    webbrowser.open("https://web.whatsapp.com/")
    t.sleep(5)
    p.click((221, 338))

def getPos():
    xi = -1

    yi = -1

    while True:
        point = p.position()
        x = point.x
        y = point.y

        if x != xi or y != yi:
            print("x: " + str(x) + " y: " + str(y))
            xi = x
            yi = y

def timer():
    now = datetime.now()

    # dd/mm/YY H:M:S
    h = int(now.strftime("%H"))
    m = int(now.strftime("%M"))

    print(h, m)

    return h == 10 and m == 30


def run():

    if timer():
        copyFile()
        t.sleep(1)
        openBrowser()
        t.sleep(2)
        sendFile()
        t.sleep(1)
        clean()
        t.sleep(0.5)
        run()
    else:
        t.sleep(10)
        run()

if __name__ == '__main__':
    run()

