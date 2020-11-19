import tkinter as tk
import random

# --- functions ---


def code(value):

    # inform function to use external/global variable
    global pin

    if value == '*':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e.delete('0', 'end')
        e.insert('end', pin)

    elif value == '#':
        # check pin

        if pin == "1234":
            print("PIN OK")
        else:
            print("PIN ERROR!", pin)
            # clear `pin`
            pin = ''
            # clear `entry`
            e.delete('0', 'end')

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e.insert('end', value)

    print("Current:", pin)

# --- main ---


keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    [' ', '9', ' '],
]

# create global variable for pin
pin = ''  # empty string

root = tk.Tk()

# place to display pin
e = tk.Entry(root)
e.grid(row=0, column=0, columnspan=3, ipady=5)


# for key in keys:
#     random.shuffle(key)
    #optionally we can also shuffle the keys list
    # random.shuffle(keys)

# create buttons using `keys`
for y, row in enumerate(keys, 1):
    for x, key in enumerate(row):
        # `lambda` inside `for` has to use `val=key:code(val)`
        # instead of direct `code(key)`
        b = tk.Button(root, text=key, command=lambda val=key: code(val))
        b.grid(row=y, column=x, ipadx=10, ipady=10)

root.mainloop()
