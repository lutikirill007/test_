from tkinter import *
def click():
    res = ' Привет {}'.format(ent.get())
    lab.configure(text=res)

    pass

window = Tk()

window.title("окно")
window.geometry('700x400')


lab = Label(window, text="введите своё имя")
lab.grid(column=0, row=0)


ent=Entry(window,width=10)
ent.grid(column=1, row=0)

button= Button(window, text="Click" ,command=click)
button.grid(column=2,row=0)

window.mainloop()


