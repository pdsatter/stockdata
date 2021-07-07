import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

import websiteCall

root = tk.Tk()

root.title("Stock Info")
root.geometry("300x200")

fontStyle = tkFont.Font(family="Lucida Grande", size=12)
root.configure(background='gray')

# End of configure
# variables

bool_list = [False]
cButton1Var = tk.BooleanVar()
cButton2Var = tk.BooleanVar()
cButton3Var = tk.BooleanVar()
cButton4Var = tk.BooleanVar()
cButton5Var = tk.BooleanVar()


# end of variables
# Functions

def submit_click():  # updates buttons based on checks then opens websites
    ticker_in_list_format = [str(e.get())]  # puts ticker in a list so it can be used as input
    websiteCall.open_websites(bool_list, ticker_in_list_format)


def isChecked1():
    bool_list[0] = cButton1Var.get()
    print(bool_list[0])


def isChecked2():
    bool_list[1] = cButton2Var.get()
    print(cButton2Var.get())


def isChecked3():
    bool_list[2] = cButton3Var.get()


def isChecked4():
    bool_list[3] = cButton4Var.get()


def isChecked5():
    bool_list[4] = cButton5Var.get()


for i in range(0, websiteCall.web_links_len() - 1):  # initiates bool list for length of links, but already init so -1
    bool_list.append(False)  # Starts all sites as True

# Beginning of Labels and buttons
label = tk.Label(root, text="Ticker", padx=10, pady=10, font=fontStyle, bg='gray').grid(row=0, column=0)  # label

e = tk.Entry(root)  # input entry line
e.configure(bg='white')  # input
e.grid(row=1, column=0)
e.insert(0, "")

cbutton1 = tk.Checkbutton(root, text="Seeking Alpha", onvalue=True, offvalue=False, variable=cButton1Var, bg="gray",
                          command=isChecked1) \
    .grid(row=1, column=1, sticky=W)

cbutton2 = tk.Checkbutton(root, text="openInsider", onvalue=True, offvalue=False, variable=cButton2Var, bg="gray",
                          command=isChecked2) \
    .grid(row=2, column=1, sticky=W)  # adds to grid, sticky sticks to wall of row
# cbutton2.bind("<Button-1>", cButton2Var)  # Binds checking box with the var associated with it

cbutton3 = tk.Checkbutton(root, text="SEC", onvalue=True, offvalue=False, variable=cButton3Var, bg="gray",
                          command=isChecked3) \
    .grid(row=3, column=1, sticky=W)

cbutton4 = tk.Checkbutton(root, text="Whale Wonder", onvalue=True, offvalue=False, variable=cButton4Var, bg="gray",
                          command=isChecked4) \
    .grid(row=4, column=1, sticky=W)

cbutton5 = tk.Checkbutton(root, text="Finra", onvalue=True, offvalue=False, variable=cButton5Var, bg="gray",
                          command=isChecked5) \
    .grid(row=5, column=1, sticky=W)

stockTickerEnterButton = tk.Button(root, text='Submit', padx=10, pady=5, command=submit_click,
                                   fg='white', bg='SpringGreen4').grid(row=2, column=0)

quitButton = Button(root, text='Quit', command=root.quit, bg="salmon", fg="white").grid(row=3, column=0)  # quit button

root.mainloop()
