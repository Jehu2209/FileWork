from tkinter import *
import os

tk = Tk()

# entry
v = StringVar()
e = Entry(tk, textvariable=v)
v.set('input folder path')
e.pack()

warnlabel = Label(tk, text='not path', fg='red')
goodlabel = Label(tk, text='is path', fg='green')
def subcheck():
    if os.path.isdir(v.get()):
        goodlabel.place(x=100, y=50)
    else:
        warnlabel.place(x=100, y=50)

submit_btn = Button(tk, text='submit', fg='blue', command=lambda: print(subcheck()))
submit_btn.place(x=100, y=100)
# entry end



# close
close_btn = Button(tk, text='close', fg='blue', command=lambda: tk.destroy()) # TODO : add try loop
close_btn.place(x=100, y=120)
# close end

tk.title('SimCheck')
tk.geometry("300x200+10+20")

tk.mainloop()
