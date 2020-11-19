from tkinter import *

window = Tk()
window.title("ATM")
window.resizable(width="true", height="true")

equation = StringVar()

expression = ""

def pressButton(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clearAll():
    global expression
    expression = ""
    equation.set("")

def clearOne():
    global expression
    expression = expression[:-1]
    equation.set(expression)

input_frame = LabelFrame(window,pady=20)
input_frame.grid(columnspan=5,ipadx=50,ipady=50)

first_label = Label(input_frame, text="ATM ID")
first_label.grid(row=0)

input_field = Entry(input_frame, textvariable = equation)
input_field.grid(row=0,column=1, columnspan=5, ipadx=10 ,ipady=5, padx=5,pady=5)

second_label = Label(input_frame, text="PIN")
second_label.grid(row=1)

second_input_field = Entry(input_frame, textvariable = equation)
second_input_field.grid(row=1, column=1,columnspan=5, ipadx=10 ,ipady=5, padx=5,pady=5)


button1 = Button(window, text='1', fg='black', bg='red',
                 command=lambda: pressButton(1), height=2, width=5)
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = Button(window, text='2', fg='black', bg='green',
                 command=lambda: pressButton(2), height=2, width=5)
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = Button(window, text='3', fg='black', bg='blue',
                 command=lambda: pressButton(3), height=2, width=5)
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = Button(window, text='4', fg='black', bg='yellow',
                 command=lambda: pressButton(4), height=2, width=5)
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = Button(window, text='5', fg='black', bg='pink',
                 command=lambda: pressButton(5), height=2, width=5)
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = Button(window, text='6', fg='black', bg='orange',
                 command=lambda: pressButton(6), height=2, width=5)
button6.grid(row=2, column=2, padx=5, pady=5)

button7 = Button(window, text='7', fg='black', bg='purple',
                 command=lambda: pressButton(7), height=2, width=5)
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = Button(window, text='8', fg='black', bg='grey',
                 command=lambda: pressButton(8), height=2, width=5)
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = Button(window, text='9', fg='black', bg='magenta',
                 command=lambda: pressButton(9), height=2, width=5)
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = Button(window, text='0', fg='black', bg='light green',
                 command=lambda: pressButton(0), height=2, width=5)
button0.grid(row=4, column=1, padx=5, pady=5)

backspace = Button(window, text='BACKSPACE', fg='black',
                   bg='light grey', command=clearOne, height=2, width=8)
backspace.grid(row=1, column=4, padx=5, pady=5)

clear = Button(window, text='CLEAR', fg='black', bg='light grey',
               command=clearAll, height=2, width=8)
clear.grid(row=2, column=4, padx=5, pady=5)

enter = Button(window, text='ENTER', fg='black',
               bg='light grey', height=2, width=8)
enter.grid(row=3, column=4, padx=5, pady=5)

window.mainloop()
