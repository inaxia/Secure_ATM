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

# Correct id and pin
correctAtmId = '2020'
correctPin = '6344'

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
               ('Brown', newlist[4]),
               ('Orange', newlist[5]),
               ('Purple', newlist[6]),
               ('Grey', newlist[7]),
               ('Pink', newlist[8]),
               ('Light Green', newlist[9])]

        newFrame = LabelFrame(page)
        newFrame.grid(columnspan=5)

        for i in range(2):
            bgColor = ""
            for j in range(10):
                bgColor = lst[j][0]
                if(i==0):
                    e = Text(newFrame, height=3, width=6, bg=bgColor)
                    e.grid(row=i, column=j)
                else:
                    e = Text(newFrame, height=2, width=5, fg='Black', font=('Arial', 10), padx=8, pady=4)
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
    page1.grid(columnspan=5, ipady=60, padx=10, pady=10)

    atmId = Label(page1, text="ATM ID")
    atmId.place(relx=0.4, rely=0.6, anchor="center")

    atmIdField = Entry(page1, textvariable=atmIdFieldKey)
    atmIdField.place(relx=0.6, rely=0.6, anchor="center")

    atmIdSubmit = Button(page1, text='Next', bg='White', height=2, width=10, command=lambda: goToPage2())
    atmIdSubmit.place(relx=0.5, rely=0.85, anchor="center")

    p1 = Table(page1)

    # Page 2
    def goToPage2():
        page1.destroy()

        global screenNumber
        screenNumber = 2

        page2 = LabelFrame(mainFrame)
        page2.grid(columnspan=5, ipady=60, padx=10, pady=10)

        pin = Label(page2, text="PIN")
        pin.place(relx=0.4, rely=0.6, anchor="center")

        pinField = Entry(page2, textvariable=pinFieldKey)
        pinField.place(relx=0.6, rely=0.6, anchor="center")

        pinSubmit = Button(page2, text='Submit', bg='White', height=2, width=10, command=lambda: goToPage3())
        pinSubmit.place(relx=0.5, rely=0.85, anchor="center")

        p2 = Table(page2)

        # Page 3
        def goToPage3():
            page2.destroy()

            finalText = ''

            if ((atmIdText == correctAtmId) and (pinText == correctPin)):
                finalText = 'Thank You'
            else:
                finalText = 'Failed'

            page3 = LabelFrame(mainFrame)
            page3.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)
            
            finalText = Label(page3, text=finalText)
            finalText.place(relx=0.5, rely=0.5, anchor="center")


# Main frame
mainFrame = LabelFrame(window)
mainFrame.grid(columnspan=5)

# Page 0
page0 = LabelFrame(mainFrame)
page0.grid(columnspan=5, ipadx=140, ipady=90, padx=10, pady=10)

welcomeText = Label(page0, text='WELCOME TO XYZ BANK ATM')
welcomeText.place(relx=0.5, rely=0.3, anchor="center")

nextbutton = Button(page0, text='Next', bg='White', height=2, width=10, command=lambda: goToPage1())
nextbutton.place(relx=0.5, rely=0.7, anchor="center")

# All buttons
button1 = Button(window, fg='Black', bg='Red', command=lambda: pressButton(newlist[0]), height=2, width=5)
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = Button(window, fg='Black', bg='Dark Green', command=lambda: pressButton(newlist[1]), height=2, width=5)
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = Button(window, fg='Black', bg='Blue', command=lambda: pressButton(newlist[2]), height=2, width=5)
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = Button(window, fg='Black', bg='Yellow', command=lambda: pressButton(newlist[3]), height=2, width=5)
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = Button(window, fg='Black', bg='Brown', command=lambda: pressButton(newlist[4]), height=2, width=5)
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = Button(window, fg='Black', bg='Orange', command=lambda: pressButton(newlist[5]), height=2, width=5)
button6.grid(row=2, column=2, padx=5, pady=5)

button7 = Button(window, fg='Black', bg='Purple', command=lambda: pressButton(newlist[6]), height=2, width=5)
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = Button(window, fg='Black', bg='Grey', command=lambda: pressButton(newlist[7]), height=2, width=5)
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = Button(window, fg='Black', bg='Pink', command=lambda: pressButton(newlist[8]), height=2, width=5)
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = Button(window, fg='Black', bg='Light Green', command=lambda: pressButton(newlist[9]), height=2, width=5)
button0.grid(row=4, column=1, padx=5, pady=5)

backspace = Button(window, text='BACKSPACE', fg='Black', bg='Light Grey', command=lambda: clearOne(), height=2, width=10)
backspace.grid(row=1, column=4, padx=5, pady=5)

clear = Button(window, text='CLEAR', fg='Black', bg='Light Grey', command=lambda: clearAll(), height=2, width=10)
clear.grid(row=2, column=4, padx=5, pady=5)

enter = Button(window, text='ENTER', fg='Black', bg='Light Grey', height=2, width=10)
enter.grid(row=3, column=4, padx=5, pady=5)

window.mainloop()
