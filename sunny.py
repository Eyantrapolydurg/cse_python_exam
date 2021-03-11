import time
from tkinter import Tk,Label
win = Tk()
win.title("time")
win.geometry("350x150")
win.resizable(0,0)
win.configure(background="black")
#win.overrideredirect(1)
def start():
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(200,start)
    
label = Label(win,font=("ds-digital",50,"bold"),bg="black",fg="red",bd=50)
label.grid(row=0,column=1)
start()
win.mainloop()
