from tkinter import *
from tkinter import messagebox
import random

from random_numbers import lotteryNumbers

my_next_space = Tk()
my_next_space.title("Pick and Play")
my_next_space.geometry("600x400")

# Winner
label_win_set = Label(my_next_space, text="Winning Numbers")
label_win_set.place(x=250,y=15)
set_win_one = Entry(my_next_space, width=3)
set_win_one.place(x=190,y=40)
set_win_two = Entry(my_next_space, width=3)
set_win_two.place(x=230,y=40)
set_win_three = Entry(my_next_space, width=3)
set_win_three.place(x=270,y=40)
set_win_four = Entry(my_next_space, width=3)
set_win_four.place(x=310,y=40)
set_win_five = Entry(my_next_space, width=3)
set_win_five.place(x=350,y=40)
set_win_six = Entry(my_next_space, width=3)
set_win_six.place(x=390,y=40)

# Set 1
label_one_set = Label(my_next_space, text="Set 1")
label_one_set.place(x=290,y=130)
set_one_one = Entry(my_next_space, width=3)
set_one_one.place(x=190,y=150)
set_one_two = Entry(my_next_space, width=3)
set_one_two.place(x=230,y=150)
set_one_three = Entry(my_next_space, width=3)
set_one_three.place(x=270,y=150)
set_one_four = Entry(my_next_space, width=3)
set_one_four.place(x=310,y=150)
set_one_five = Entry(my_next_space, width=3)
set_one_five.place(x=350,y=150)
set_one_six = Entry(my_next_space, width=3)
set_one_six.place(x=390,y=150)

# set 2

label_one_set = Label(my_next_space, text="Set 2")
label_one_set.place(x=290,y=200)
set_one_one = Entry(my_next_space, width=3)
set_one_one.place(x=190,y=220)
set_one_two = Entry(my_next_space, width=3)
set_one_two.place(x=230,y=220)
set_one_three = Entry(my_next_space, width=3)
set_one_three.place(x=270,y=220)
set_one_four = Entry(my_next_space, width=3)
set_one_four.place(x=310,y=220)
set_one_five = Entry(my_next_space, width=3)
set_one_five.place(x=350,y=220)
set_one_six = Entry(my_next_space, width=3)
set_one_six.place(x=390,y=220)

# set 3

label_one_set = Label(my_next_space, text="Set 3")
label_one_set.place(x=290,y=270)
set_one_one = Entry(my_next_space, width=3)
set_one_one.place(x=190,y=290)
set_one_two = Entry(my_next_space, width=3)
set_one_two.place(x=230,y=290)
set_one_three = Entry(my_next_space, width=3)
set_one_three.place(x=270,y=290)
set_one_four = Entry(my_next_space, width=3)
set_one_four.place(x=310,y=290)
set_one_five = Entry(my_next_space, width=3)
set_one_five.place(x=350,y=290)
set_one_six = Entry(my_next_space, width=3)
set_one_six.place(x=390,y=290)

# functions
def lotto():
    # Initialise an empty list that will be used to store the 6 lucky numbers!
    lotteryNumbers = []

    for i in range(0, 6):
        number = random.randint(1, 49)
        # Check if this number has already been picked and ...
        while number in lotteryNumbers:
            # ... if it has, pick a new number instead
            number = random.randint(1, 49)

        # Now that we have a unique number, let's append it to our list.
        lotteryNumbers.append(number)

    # Sort the list in ascending order
    lotteryNumbers.sort()

    # Display the list on screen:

# Buttons
replay_button = Button(my_next_space, text="Replay")
replay_button.place(x=170,y=350)
prize_button = Button(my_next_space, text="Claim Prize")
prize_button.place(x=260,y=350)
exit_button = Button(my_next_space, text="Exit")
exit_button.place(x=380,y=350)
play_button = Button(my_next_space, text="Play", command=lotto)
play_button.place(x=275,y=80)



my_next_space.mainloop()