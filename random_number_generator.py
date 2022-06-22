import random
from tkinter import *

PickedNumber = []
NumList = []

for i in range(90): # Define range of the List
    NumList.append(i + 1)

window = Tk()


def pick(): # Get the number randomly and delete from the list to prevent dublicate
    x = random.choice(NumList)
    winnerLabel.config(text=x)
    NumList.remove(x)
    x = str(x)
    PickedNumber.append(x + "|")
    l2.config(text=PickedNumber)
    window.config(bg='#146B3A')

    if not NumList:
        winnerLabel.config(text='GAME FINISHED') #For extra text, try the codes which is at the below
        # finishLabel = Label(window, text='GAME FINISHED', font=("Helvetica 60 bold"),bg="#165B33",fg="White")
        # finishLabel.pack(pady=20)
    return


window.title('Random Number Generator')# app title
window.geometry('800x800')

winnerLabel = Label(window, text='Start', font=("Helvetica 30 bold"), bg="#BB2528", fg="White")# main Title
winnerLabel.pack(pady=20)

winButton = Button(window, text="Choose The Lucky Number", font=('Verdana 22'), bg="#F8B229", fg="White", command=pick)# button to get number
winButton.pack(pady=20)

l2 = Label(bg="#EA4630", font=("Arial", 22), text="", wraplengt=600, justify="center")#Numbers
l2.place(x=80, y=200)

window.mainloop()