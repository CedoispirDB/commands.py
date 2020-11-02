from tkinter import Button
from pynput.mouse import Button, Controller
import random
import tkinter as tk
import webbrowser

sure = input("Are you sure? ")
sure = sure.lower()
if sure == "n":
    exit()

window = tk.Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

mouse = Controller()

while True:
    webbrowser.open("https: // mail.google.com/mail/u/0 /  # inbox")
    mouse.position = (random.randint(-width,width), random.randint(-height,height))
