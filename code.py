from tkinter import *
import random

window = Tk()
window.title("ATM")

# Field keys
atmIdFieldKey = StringVar()
pinFieldKey = StringVar()

# Variables for fields
atmIdText = ""
pinText = ""

# To keep track of the SCREENS
screenNumber = 0

# Number list
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
newlist = numlist

# For creating number table
class Table:
    def __init__(self, page):

        if screenNumber == 2:
            random.shuffle(newlist)

        # take the data
        lst = [('Red', newlist[0]),
               ('Dark Green', newlist[1]),
               ('Blue', newlist[2]),
               ('Yellow', newlist[3]),
               ('Light Pink', newlist[4]),
               ('Orange', newlist[5]),
               ('purple', newlist[6]),
               ('Grey', newlist[7]),
               ('Pink', newlist[8]),
               ('Light Green', newlist[9])]

        newFrame = LabelFrame(page)
        newFrame.grid(columnspan=5)

        for i in range(2):
            bgColor = ""
            for j in range(10):
                bgColor = lst[j][0]
                e = Entry(newFrame, width=10, fg='black', bg=bgColor, font=('Arial', 10))
                e.grid(row=i, column=j)
                e.insert(END, lst[j][i])

# For INTEGER buttons
def pressButton(num):
    global atmIdText, pinText
    if screenNumber == 1:
        atmIdText = atmIdText + str(num)
        atmIdFieldKey.set(atmIdText)
    elif screenNumber == 2:
        pinText = pinText + str(num)
        pinFieldKey.set(pinText)

# For CLEAR button
def clearAll():
    global atmIdText, pinText
    if screenNumber == 1:
        atmIdText = ""
        atmIdFieldKey.set(atmIdText)
    elif screenNumber == 2:
        pinText = ""
        pinFieldKey.set(pinText)

# For BACKSPACE button
def clearOne():
    global atmIdText, pinText
    if screenNumber == 1:
        atmIdText = atmIdText[:-1]
        atmIdFieldKey.set(atmIdText)
    elif screenNumber == 2:
        pinText = pinText[:-1]
        pinFieldKey.set(pinText)

# Page 1
def goToPage1():
    page0.destroy()

    global screenNumber
    screenNumber = 1

    page1 = LabelFrame(mainFrame)
    page1.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)

    atmId = Label(page1, text="ATM ID")
    atmId.place(relx=0.2, rely=0.4, anchor="center")

    atmIdField = Entry(page1, textvariable=atmIdFieldKey)
    atmIdField.place(relx=0.6, rely=0.4, anchor="center")

    atmIdSubmit = Button(page1, text='Next', bg='white', height=2, width=10, command=lambda: goToPage2())
    atmIdSubmit.place(relx=0.5, rely=0.7, anchor="center")

    p1 = Table(page1)

    # Page 2
    def goToPage2():
        page1.destroy()

        global screenNumber
        screenNumber = 2

        page2 = LabelFrame(mainFrame)
        page2.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)

        pin = Label(page2, text="PIN")
        pin.place(relx=0.2, rely=0.4, anchor="center")

        pinField = Entry(page2, textvariable=pinFieldKey)
        pinField.place(relx=0.6, rely=0.4, anchor="center")

        pinSubmit = Button(page2, text='Submit', bg='white', height=2, width=10, command=lambda: goToPage3())
        pinSubmit.place(relx=0.5, rely=0.7, anchor="center")

        p2 = Table(page2)

        # Page 3
        def goToPage3():
            page2.destroy()

            page3 = LabelFrame(mainFrame)
            page3.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)

            successText = Label(page3, text='Thank You')
            successText.place(relx=0.5, rely=0.5, anchor="center")


# Main frame
mainFrame = LabelFrame(window, pady=20)
mainFrame.grid(columnspan=5,)

# Page 0
page0 = LabelFrame(mainFrame, pady=20)
page0.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)

welcomeText = Label(page0, text='WELCOME TO XYZ BANK ATM')
welcomeText.place(relx=0.5, rely=0.3, anchor="center")

nextbutton = Button(page0, text='Next', bg='white', height=2, width=10, command=lambda: goToPage1())
nextbutton.place(relx=0.5, rely=0.7, anchor="center")

# All buttons
button1 = Button(window, fg='black', bg='red', command=lambda: pressButton(newlist[0]), height=2, width=5)
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = Button(window, fg='black', bg='green', command=lambda: pressButton(newlist[1]), height=2, width=5)
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = Button(window, fg='black', bg='blue', command=lambda: pressButton(newlist[2]), height=2, width=5)
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = Button(window, fg='black', bg='yellow', command=lambda: pressButton(newlist[3]), height=2, width=5)
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = Button(window, fg='black', bg='pink', command=lambda: pressButton(newlist[4]), height=2, width=5)
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = Button(window, fg='black', bg='orange', command=lambda: pressButton(newlist[5]), height=2, width=5)
button6.grid(row=2, column=2, padx=5, pady=5)

button7 = Button(window, fg='black', bg='purple', command=lambda: pressButton(newlist[6]), height=2, width=5)
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = Button(window, fg='black', bg='grey', command=lambda: pressButton(newlist[7]), height=2, width=5)
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = Button(window, fg='black', bg='magenta', command=lambda: pressButton(newlist[8]), height=2, width=5)
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = Button(window, fg='black', bg='light green', command=lambda: pressButton(newlist[9]), height=2, width=5)
button0.grid(row=4, column=1, padx=5, pady=5)

backspace = Button(window, text='BACKSPACE', fg='black', bg='light grey', command=lambda: clearOne(), height=2, width=10)
backspace.grid(row=1, column=4, padx=5, pady=5)

clear = Button(window, text='CLEAR', fg='black', bg='light grey', command=lambda: clearAll(), height=2, width=10)
clear.grid(row=2, column=4, padx=5, pady=5)

enter = Button(window, text='ENTER', fg='black', command=lambda: clearAll(), bg='light grey', height=2, width=10)
enter.grid(row=3, column=4, padx=5, pady=5)

window.mainloop()
