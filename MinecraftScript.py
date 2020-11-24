import pyautogui as pyautogui
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import random
import tkinter as tk
import time
import keyboard

time.sleep(5)

# window = tk.Tk()
# mouse = Controller()
# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()
# mouse.position = (width / 2, height / 2)

while True:
    pos = pyautogui.position()
    pyautogui.click(pos)
    time.sleep(1.5)

# MID Point(x=1238, y=414)
