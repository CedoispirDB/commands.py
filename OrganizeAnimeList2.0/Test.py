# import hashlib
#
# x = [".png", ".jpeg", ".mp4", ".rtf", ".pdf", ".txt"]
# for n in x:
#     ex = hashlib.sha1(n.encode()).hexdigest()
#     print(n + ": " + ex)

# import tkinter
#
# root = tkinter.Tk()
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
#
# print(width, height)

from pynput import keyboard

def on_press(key):
    try:
        print(str(key)[1:2])
    except AttributeError:
        print(key)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# listener = keyboard.Listener(on_press=on_press)
# listener.start()
