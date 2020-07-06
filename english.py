from tkinter import *
from keyboard import *

def find(sv):
    if len(sv.get())==2: return 
    root.clipboard_clear()
    try:
        root.clipboard_append(words[sv.get().lower()])
        answer.set(words[sv.get().lower()])
    except:
        pass    

buff = "" 
def callback(e):
    global buff
    if e.name == 'esc' or e.name == 'enter':
        buff = ''
        sv.set(buff)
        answer.set(buff)
    elif e.name == 'backspace':
        buff  = buff[:-1]
        sv.set(buff)
    elif e.name == '.':
        send('ctrl+a')
        for i in range(15):
            send(14);
        write(words[sv.get().lower()]+'\n')
        buff = ''
        answer.set(buff)
    elif e.name == ',':
        send('ctrl+a')
        write(words[sv.get().lower()])       
        buff = ''
        answer.set(buff)
    elif e.name in 'qwertyuiopasdfghjklzxcvbnm':
        buff += e.name
        sv.set(buff) #triggers the find callback since SV variable is being traced

on_press(callback)

root = Tk()
lines = []

with open("C:\\Users\\pc\\Desktop\\Eng.txt", encoding='utf-8', mode='r') as f:
    lines = f.readlines()
    words = {m.strip():n.strip() for m,n in [z.split("@") for z  in lines]}

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