from tkinter import *
import time

root = Tk()
root.geometry('280x350+400+150')
root.title('Adure Calculator')
root.config(bg='sky blue')

calc = StringVar()
text_input = StringVar()
operator = ""

def exit1():
    exit()

def btn_click(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def btn_clear():
    global operator
    operator = ""
    text_input.set("")

label1 = Label(root, text="SIMPLE CALCULATOR", font=('arial', 12, 'bold'), bg='sky blue',
               fg='dark blue').pack()
entry1 = Entry(root, font=('arial', 14, 'bold'), fg='blue', bg='white', textvariable=text_input,
               bd=4, width=18, justify='right').place(x=35, y=30)
btn7 = Button(root, text='7', font=('arial', 14, 'bold'), width=3, bd=5, command=lambda: btn_click(7)).place(x=35, y=70)
btn8 = Button(root, text='8', font=('arial', 14, 'bold'), width=3, bd=5, command=lambda: btn_click(8)).place(x=89, y=70)
btn9 = Button(root, text='9', font=('arial', 14, 'bold'), width=3, bd=5).place(x=143, y=70)
btnmult = Button(root, text='*', font=('arial', 14, 'bold'), width=3, bd=5).place(x=197, y=70)

btn4 = Button(root, text='4', font=('arial', 14, 'bold'), width=3, bd=5).place(x=35, y=120)
btn5 = Button(root, text='5', font=('arial', 14, 'bold'), width=3, bd=5).place(x=89, y=120)
btn6 = Button(root, text='6', font=('arial', 14, 'bold'), width=3, bd=5).place(x=143, y=120)
btnsubtr = Button(root, text='-', font=('arial', 14, 'bold'), width=3, bd=5).place(x=197, y=120)

btn1 = Button(root, text='1', font=('arial', 14, 'bold'), width=3, bd=5).place(x=35, y=170)
btn2 = Button(root, text='2', font=('arial', 14, 'bold'), width=3, bd=5).place(x=89, y=170)
btn3 = Button(root, text='3', font=('arial', 14, 'bold'), width=3, bd=5).place(x=143, y=170)
btnadd = Button(root, text='+', font=('arial', 14, 'bold'), width=3, bd=5).place(x=197, y=170)

btnC = Button(root, text='C', font=('arial', 14, 'bold'), width=3, bd=5, command=btn_clear).place(x=35, y=220)
btn0 = Button(root, text='0', font=('arial', 14, 'bold'), width=3, bd=5).place(x=89, y=220)
btndot = Button(root, text='.', font=('arial', 14, 'bold'), width=3, bd=5).place(x=143, y=220)
btnequ = Button(root, text='=', font=('arial', 14, 'bold'), width=3, bd=5).place(x=197, y=220)

btnexit = Button(root, text='Exit', font=('arial', 14, 'bold'), bd=5, command=exit1).place(x=100, y=280)

root.mainloop()