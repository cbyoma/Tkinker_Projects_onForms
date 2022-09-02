import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import time
from PIL import Image, ImageTk

root = Tk()
root.geometry('500x650+300+40')
root.title('Charles Registration Form')

form_image = Image.open('C:/Users/CByoma/Desktop/SE Learning/Python Projects/Online Image download/download1.jpg')
foto = ImageTk.PhotoImage(form_image)

lab = Label(image=foto)
lab.pack()

first_name = StringVar()
last_name = StringVar()
DoB = StringVar()
listdrop = StringVar()
msgbox_java = "Java"
msgbox_python = "Python"
gender_select = StringVar()

def printt():
    f_name = first_name.get()
    l_name = last_name.get()
    DoBirth = DoB.get()
    l_drop = listdrop.get()
    gender = gender_select.get()
    msgbox_pro = msgbox_java
    msgbox_pro = msgbox_python

    print(f'First Name: {f_name}')
    print(f'Last Name: {l_name}')
    print(f'Date of Birth: {DoBirth}')
    print(f'Country: {l_drop}')
    print(f'Gender: {gender}')
    print(f'Programming Laguage: {msgbox_pro}')
    tkinter.messagebox.showinfo('Welcome', 'You successfully signed Up !')

def exit1():
    exit()

#------------------------------------- Main name -----------------------------------------------
label1 = Label(root, text='Registration Form', font=('arial', 20, 'bold'), relief='solid', width=20,
               fg='dark blue').place(x=80, y=180)

#------------------------------------- Form details and entries --------------------------------
label2 = Label(root, text='First Name:', font=('arial', 15, 'bold'), fg='blue'
               ).place(x=70, y=250)
entry_label2 = Entry(root, font=('arial', 15, 'bold'), bd=4, width=16,
                     textvariable=first_name).place(x=200, y=250)
label3 = Label(root, text='Last Name:', font=('arial', 15, 'bold'), fg='blue'
               ).place(x=70, y=300)
entry_label3 = Entry(root, font=('arial', 15, 'bold'), bd=4, width=16,
                     textvariable=last_name).place(x=200, y=300)
label4 = Label(root, text='DoB:', font=('arial', 15, 'bold'), fg='blue'
               ).place(x=70, y=350)
entry_label4 = Entry(root, font=('arial', 15, 'bold'), bd=4, width=16,
                     textvariable=DoB).place(x=200, y=350)
label5 = Label(root, text='Country', font=('arial', 15, 'bold'), fg='blue'
               ).place(x=70, y=400)

label6 = Label(root,text='Gender:', font=('arial', 15, 'bold'), fg='blue'
               ).place(x=70, y=450)
label7 = Label(root,text='Prog Lang.:', font=('arial', 15, 'bold'), fg='blue'
               ).place(x=70, y=500)

RM_gender = Radiobutton(root, text='Male', variable=gender_select, value='Male').place(x=200, y=450)
RF_gender = Radiobutton(root, text='Female', variable=gender_select, value='Female').place(x=300, y=450)

check_box1 = Checkbutton(root, text='Java', variable=msgbox_java,
                         bd=4, font=('arial', 10, 'bold')).place(x=200, y=500)
check_box2 = Checkbutton(root, text='Python', variable=msgbox_python,
                         bd=4, font=('arial', 10, 'bold')).place(x=270, y=500)

list = ['Nigeria', 'Ghana', 'Togo', 'Senegal', 'DR Congo']
drop_list = OptionMenu(root, listdrop, *list)
listdrop.set('Select Country')
drop_list.config(width=15, bd=4, font=('arial', 10, 'bold'))
drop_list.place(x=200, y=400)

btn1 = Button(root, text='Signup', font=('arial', 14, 'bold'), bd=6, fg='white',
              bg='blue', command=printt).place(x=140, y=580)
btn2 = Button(root, text='Exit', font=('arial', 14, 'bold'), bd=6, width=6, fg='white',
              bg='blue', command=exit1).place(x=270, y=580)

root.mainloop()