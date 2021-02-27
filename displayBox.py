from tkinter import *

window = Tk()
window.geometry("500x150")

alist = Listbox(window, selectmode="multiple")

alist.pack(expand=YES, fill="both")

x = ["Organize Animes", "Move Anime", "Add Anime", "Find Anime", "Show lists", "Number of Animes", "Help"]

for each_item in range(len(x)):
    alist.insert(END, x[each_item])

window.mainloop()
