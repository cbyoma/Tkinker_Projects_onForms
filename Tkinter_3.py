from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('1350x700+0+0')
root.title('Charles Adure Application')
root.config(bg='sky blue')

name1 = StringVar()
name2 = StringVar()

def printt():
    f_name = name1.get()
    l_name = name2.get()
    print("The is done by %s" % f_name)
    print("The is done by %s" % l_name)

def exit1():
    exit()

label1 = Label(root, text='Registration Application', font=('arial', 40, 'bold'), fg='dark blue',
               bg='sky blue', relief='solid', width=25, bd=4).pack()
label2 = Label(root, text='First Name:', font=('arial', 25, 'bold'), fg='brown', bg='sky blue'
               ).place(x=350, y=150)
entry_label2 = Entry(root, font=('arial', 25, 'bold'), fg='brown', bg='white', width=15,
               justify='left', bd=10, textvariable=name1).place(x=600, y=150)
label3 = Label(root, text='Last Name:', font=('arial', 25, 'bold'), fg='brown', bg='sky blue'
               ).place(x=350, y=250)
entry_label3 = Entry(root, font=('arial', 25, 'bold'), fg='brown', bg='white', width=15,
               justify='left', bd=10, textvariable=name2).place(x=600, y=250)

btn1 = Button(root, font=('arial', 20, 'bold'), text='Login', fg='white', bg='blue', bd=10, width=8,
              command=printt)
btn1.place(x=450, y=350)
btn2 = Button(root, font=('arial', 20, 'bold'), text='Exit', fg='white', bg='blue', bd=10, width=8,
              command=exit1)
btn2.place(x=650, y=350)


root.mainloop()