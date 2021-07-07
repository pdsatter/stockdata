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

bool_list = []


# Functions!

def submit_click(bool_list1):  # updates buttons based on checks then opens websites
    ticker_list_format = [e.get()]  # puts ticker in a list so it can be used as input
    websiteCall.open_websites(bool_list1, ticker_list_format)

    # FIX this call breaks buttons to all be false


# Beginning of Labels
label = tk.Label(root, text="Ticker", padx=10, pady=10, font=fontStyle, bg='gray').grid(row=0, column=0)  # label

#  label.configure(fg='white')

e = tk.Entry(root)  # input entry line
e.configure(bg='white')  # input
e.grid(row=1, column=0)
e.insert(0, "")

stockTickerEnterButton = tk.Button(root, text='Submit', padx=10, pady=5,  # Adds enter button that searches stocks
                                   command=lambda: submit_click(bool_list), fg='white', bg='SpringGreen4') \
    .grid(row=2, column=0)

cButton1Var = tk.BooleanVar(value=websiteCall.sa_is_true())  # Booleans related to checkboxes
cButton2Var = tk.BooleanVar(value=websiteCall.oi_is_true())  # Initiated as settings for corresponding website vars
cButton3Var = tk.BooleanVar(value=websiteCall.sec_is_true())
cButton4Var = tk.BooleanVar(value=websiteCall.ww_is_true())
cButton5Var = tk.BooleanVar(value=websiteCall.fin_is_true())

bool_list.append(cButton1Var)  # adds buttons to bool_list, true if checked, false if unchecked
bool_list.append(cButton2Var)
bool_list.append(cButton3Var)
bool_list.append(cButton4Var)
bool_list.append(cButton5Var)

cbutton1 = tk.Checkbutton(root, text="Seeking Alpha", variable=cButton1Var, bg="gray") \
    .grid(row=1, column=1, sticky=W)
# cbutton1.bind("<Button-1>", cButton1Var)

cbutton2 = tk.Checkbutton(root, text="openInsider", variable=cButton2Var, bg="gray") \
    .grid(row=2, column=1, sticky=W)  # adds to grid, sticky sticks to wall of row
# cbutton2.bind("<Button-1>", cButton2Var)  # Binds checking box with the var associated with it

cbutton3 = tk.Checkbutton(root, text="SEC", variable=cButton3Var, bg="gray") \
    .grid(row=3, column=1, sticky=W)
# cbutton3.bind("<Button-1>", cButton3Var)

cbutton4 = tk.Checkbutton(root, text="Whale Wonder", variable=cButton4Var, bg="gray") \
    .grid(row=4, column=1, sticky=W)
# cbutton4.bind("<Button-1>", cButton4Var)

cbutton5 = tk.Checkbutton(root, text="Finra", variable=cButton5Var, bg="gray") \
    .grid(row=5, column=1, sticky=W)
# cbutton5.bind("<Button-1>", cButton5Var)

quitButton = Button(root, text='Quit', command=root.quit, bg="salmon", fg="white").grid(row=3, column=0)  # quit button

root.mainloop()
