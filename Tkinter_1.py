from tkinter import *

root = Tk()

label_1 = Label(root, text='Name:')
label_2 = Label(root, text='Password:')
label_3 = Checkbutton(root, text='Keep me logged in')
entry_1 = Entry(root)
entry_2 = Entry(root)


label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
label_3.grid(columnspan=2)

button_1 = Button(root, text='Login', fg='black')
button_1.grid(row=3, column=1)

root.mainloop()