from tkinter import *

window = Tk()
window.title("ATM")

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


def nextPage():
    page1.destroy()

    page2 = LabelFrame(mainFrame)
    page2.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)

    atmId = Label(page2, text="ATM ID")
    atmId.place(relx=0.2,rely=0.4,anchor="center")

    atmIdField = Entry(page2, textvariable=equation)
    atmIdField.place(relx=0.6, rely=0.4, anchor="center")
    
    atmIdSubmit = Button(page2, text='Next', bg='white', height=2, width=10, command=lambda: pinIdPage())
    atmIdSubmit.place(relx=0.5, rely=0.7, anchor="center")
    
    def pinIdPage():
        page2.destroy()
        page3 = LabelFrame(mainFrame)
        page3.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)
        
        pinInput = StringVar()
        pin = Label(page3, text="PIN")
        pin.place(relx=0.2, rely=0.5,anchor="center")

        pinField = Entry(page3, textvariable = equation)
        pinField.place(relx=0.6, rely=0.5, anchor="center")
        
        def checkPin():
            global expression
            if expression =="1234":
                result="SUCCESS!!"
            else:
                result="WRONG PIN!! /nTRY AGAIN"
                expression=""
                equation.set("")
            resultLabel = Label(page3,textvariable=result)
            resultLabel.place(relx=0.5, rely=0.8,anchor="center")
    
        

mainFrame = LabelFrame(window, pady=20)
mainFrame.grid(columnspan=5,)

page1 = LabelFrame(mainFrame, pady=20)
page1.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)

welcomeText = Label(page1, text='WELCOME TO XYZ BANK ATM')
welcomeText.place(relx=0.5, rely=0.2, anchor="center")

nextbtn = Button(page1, text='Next', bg='white', height=2, width=10, command=lambda: nextPage())
nextbtn.place(relx=0.5, rely=0.7, anchor="center")


button1 = Button(window, text='1', fg='black', bg='red', command=lambda: pressButton(1), height=2, width=5)
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = Button(window, text='2', fg='black', bg='green', command=lambda: pressButton(2), height=2, width=5)
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = Button(window, text='3', fg='black', bg='blue', command=lambda: pressButton(3), height=2, width=5)
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = Button(window, text='4', fg='black', bg='yellow', command=lambda: pressButton(4), height=2, width=5)
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = Button(window, text='5', fg='black', bg='pink', command=lambda: pressButton(5), height=2, width=5)
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = Button(window, text='6', fg='black', bg='orange', command=lambda: pressButton(6), height=2, width=5)
button6.grid(row=2, column=2, padx=5, pady=5)

button7 = Button(window, text='7', fg='black', bg='purple', command=lambda: pressButton(7), height=2, width=5)
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = Button(window, text='8', fg='black', bg='grey', command=lambda: pressButton(8), height=2, width=5)
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = Button(window, text='9', fg='black', bg='magenta', command=lambda: pressButton(9), height=2, width=5)
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = Button(window, text='0', fg='black', bg='light green', command=lambda: pressButton(0), height=2, width=5)
button0.grid(row=4, column=1, padx=5, pady=5)

backspace = Button(window, text='BACKSPACE', fg='black', bg='light grey', command=clearOne(), height=2, width=10)
backspace.grid(row=1, column=4, padx=5, pady=5)

clear = Button(window, text='CLEAR', fg='black', bg='light grey', command=clearAll(), height=2, width=10)
clear.grid(row=2, column=4, padx=5, pady=5)

enter = Button(window, text='ENTER', fg='black', bg='light grey',command=lambda:checkPin(), height=2, width=10)
enter.grid(row=3, column=4, padx=5, pady=5)

window.mainloop()
