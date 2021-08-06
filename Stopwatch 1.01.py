import tkinter as tk
import time

win=tk.Tk()
# win.geometry('240x200')
win.title("STOPWATCH")

def start():
    global start1
    start1=time.time()
    but.config(command=stop)
    but.config(text='Stop')

#Follow python.bytes

def stop():
    global stop1
    stop1=time.time()
    global duration
    duration=stop1-start1
    duration=round(duration,2)
    but.config(state='disabled')
    but.config(bg='grey')
    if duration>60:
        if duration%60==0:
            duration=duration/60
            global lab
            lab=tk.Label(win,text=(duration,'min'),font=("times new roman",20),fg='midnightblue')
            lab.pack()
        else:
            duration_in_minutes=int(duration//60)
            duration_in_seconds=int(duration%60)
            # duration_in_seconds=round(duration,0)
            lab=tk.Label(win,text=(duration_in_minutes,'min',duration_in_seconds,'sec'),
                        font=("times new roman",20),fg='midnightblue')
            lab.pack()
    else:
        # global lab
        lab=tk.Label(win,text=(duration,'sec'),font=("times new roman",20),fg='midnightblue')
        lab.pack()
        
follow=tk.Label(win,text='Follow python.bytes',font=("times new roman",20),fg='midnightblue')
follow.pack()
#Follow python.bytes
def reset():
    lab.destroy()
    but.config(state='normal')
    but.config(bg='dodgerblue')
    but.config(text='Start')
    but.config(command=start)

but2=tk.Button(win,text="Reset",command=reset,activebackground='dodgerblue',activeforeground='white',
                fg='white',font=("times new roman",20),bd=3,relief='raised',bg="dodgerblue")
but2.pack(padx=80,pady=10,side='top')

but=tk.Button(win,text='Start',command=start,fg='white',activebackground='dodgerblue',
            activeforeground='white',font=("times new roman",20),bd=3,relief='raised',bg="dodgerblue")
but.pack(padx=80,pady=10,side='bottom')
win.mainloop()
