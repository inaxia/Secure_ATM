from tkinter import *

window = Tk()
window.title("ATM")
window.resizable(width="false", height="true")

equation = StringVar()

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

input_field = Entry(window, textvariable = equation)
input_field.grid(columnspan=5, ipadx=50 ,ipady=10, padx=5,pady=5)

button1 = Button(window, text='1', fg='black', bg='red', command=lambda:press(1), height=2, width=5)
button1.grid(row=1,column=0,padx=5, pady=5)

button2 = Button(window, text='2', fg='black', bg='green', command=lambda:press(2), height=2, width=5)
button2.grid(row=1,column=1,padx=5, pady=5)

button3 = Button(window, text='3', fg='black', bg='blue', command=lambda:press(3), height=2, width=5)
button3.grid(row=1,column=2,padx=5, pady=5)

button4 = Button(window, text='4', fg='black', bg='yellow', command=lambda:press(4), height=2, width=5)
button4.grid(row=2,column=0,padx=5, pady=5)

button5 = Button(window, text='5', fg='black', bg='pink', command=lambda:press(5), height=2, width=5)
button5.grid(row=2,column=1,padx=5, pady=5)

button6 = Button(window, text='6', fg='black', bg='orange', command=lambda:press(6), height=2, width=5)
button6.grid(row=2,column=2,padx=5, pady=5)

button7 = Button(window, text='7', fg='black', bg='purple', command=lambda:press(7), height=2, width=5)
button7.grid(row=3,column=0,padx=5, pady=5)

button8 = Button(window, text='8', fg='black', bg='grey', command=lambda:press(8), height=2, width=5)
button8.grid(row=3,column=1,padx=5, pady=5)

button9 = Button(window, text='9', fg='black', bg='magenta', command=lambda:press(9), height=2, width=5)
button9.grid(row=3,column=2,padx=5, pady=5)

button10 = Button(window, text='', fg='black', bg='white', height=2, width=5)
button10.grid(row=4,column=0,padx=5, pady=5)

button11 = Button(window, text='0', fg='black', bg='light green', command=lambda:press(0), height=2, width=5)
button11.grid(row=4,column=1,padx=5, pady=5)

button12 = Button(window, text='', fg='black', bg='white', height=2, width=5)
button12.grid(row=4,column=2,padx=5, pady=5)

button13 = Button(window, text='CANCEL', fg='black', bg='white', height=2, width=8)
button13.grid(row=1,column=4,padx=5, pady=5)

button14 = Button(window, text='ENTER', fg='black', bg='white', height=2, width=8)
button14.grid(row=2,column=4,padx=5, pady=5)

button15 = Button(window, text='CUT', fg='black', bg='white', height=2, width=8)
button15.grid(row=3,column=4,padx=5, pady=5)

button16 = Button(window, text=' ', fg='black', bg='white', height=2, width=8)
button16.grid(row=4,column=4,padx=5, pady=5)
window.mainloop()
