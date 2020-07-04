from tkinter import *
from keyboard import *

def find(sv):
    for l in lines:
        if len(sv.get())==2: return 
        if(l.split("@")[0].strip().lower() == sv.get().lower()):
            root.clipboard_clear()
            root.clipboard_append(l.split("@")[1].strip())
            answer.set(l.split("@")[1].strip())
            break

buff = "" 
def callback(e):
    global buff
    if e.name == 'esc':
        buff = ''
        sv.set(buff)
    elif e.name == 'backspace':
        buff  = buff[:-1]
        sv.set(buff)
    elif e.name in 'qwertyuiopasdfghjklzxcvbnm':
        buff += e.name
        sv.set(buff) #triggers the find callback since SV variable is being traced

on_press(callback)

root = Tk()
lines = []

with open("C:\\Users\\pc\\Desktop\\Eng.txt", encoding='utf-8', mode='r') as f:
    lines = f.readlines()

canvas1 = Canvas(root, width = 200, height = 200)
canvas1.pack()

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: find(sv))
entry1 = Entry (root,validate="focusout", textvariable=sv)
canvas1.create_window(100, 100, window=entry1)

button1 = Button(text='Find', command=find)
canvas1.create_window(100, 140, window=button1)

answer = StringVar()
label = Label(root, textvariable=answer)
canvas1.create_window(100, 50, window=label)


root.mainloop()