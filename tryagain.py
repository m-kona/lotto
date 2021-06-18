from tkinter import *
import random

from random_numbers import lotteryNumbers

space = Tk()
space.geometry("200x200")
space.title("Random")

def play():
    lotteryNumbers = []

    for i in range(0, 6):
        number = random.randint(1, 50)
        # Check if this number has already been picked and ...
        while number in lotteryNumbers:
            # ... if it has, pick a new number instead
            number = random.randint(1, 50)

        # Now that we have a unique number, let's append it to our list.
        lotteryNumbers.append(number)

    # Sort the list in ascending order
    lotteryNumbers.sort()


heading_label = Label(space, text="Numbers")
heading_label.place(x=20,y=20)

results_label = Label(space, text="")
results_label.place(x=20,y=40)

enter_number = Entry(space)
enter_number.place(x=20,y=70)

play_btn = Button(space, text="Play", command=play)
play_btn.place(x=20,y=100)

space.mainloop()