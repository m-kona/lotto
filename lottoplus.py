from tkinter import *
from tkinter import messagebox

myspace = Tk()
myspace.title("Lotto Machine")
myspace.geometry("700x500")

label_name = Label(myspace, text="Name")
label_name.place(x=10,y=200)
enter_name = Entry(myspace)
enter_name.place(x=10,y=220)

label_name = Label(myspace, text="Email")
label_name.place(x=10,y=250)
enter_name = Entry(myspace)
enter_name.place(x=10,y=270)

label_name = Label(myspace, text="Address")
label_name.place(x=10,y=300)
enter_name = Entry(myspace)
enter_name.place(x=10,y=320)

label_name = Label(myspace, text="Identity (ID)")
label_name.place(x=10,y=350)
enter_name = Entry(myspace)
enter_name.place(x=10,y=370)

button_enter = Button(myspace, text="Enter")
button_enter.place(x=60,y=410)

# Side 2
label_one_set = Label(myspace, text="Set 1")
label_one_set.place(x=350,y=220)
set_one_one = Entry(myspace, width=3)
set_one_one.place(x=250,y=250)
set_one_two = Entry(myspace, width=3)
set_one_two.place(x=290,y=250)
set_one_three = Entry(myspace, width=3)
set_one_three.place(x=330,y=250)
set_one_four = Entry(myspace, width=3)
set_one_four.place(x=370,y=250)
set_one_five = Entry(myspace, width=3)
set_one_five.place(x=410,y=250)
set_one_six = Entry(myspace, width=3)
set_one_six.place(x=450,y=250)

label_two_set = Label(myspace, text="Set 2")
label_two_set.place(x=350,y=280)
set_two_one = Entry(myspace, width=3)
set_two_one.place(x=250,y=310)
set_two_two = Entry(myspace, width=3)
set_two_two.place(x=290,y=310)
set_two_three = Entry(myspace, width=3)
set_two_three.place(x=330,y=310)
set_two_four = Entry(myspace, width=3)
set_two_four.place(x=370,y=310)
set_two_five = Entry(myspace, width=3)
set_two_five.place(x=410,y=310)
set_two_six = Entry(myspace, width=3)
set_two_six.place(x=450,y=310)

label_three_set = Label(myspace, text="Set 3")
label_three_set.place(x=350,y=340)
set_three_one = Entry(myspace, width=3)
set_three_one.place(x=250,y=370)
set_three_two = Entry(myspace, width=3)
set_three_two.place(x=290,y=370)
set_three_three = Entry(myspace, width=3)
set_three_three.place(x=330,y=370)
set_three_four = Entry(myspace, width=3)
set_three_four.place(x=370,y=370)
set_three_five = Entry(myspace, width=3)
set_three_five.place(x=410,y=370)
set_two_six = Entry(myspace, width=3)
set_two_six.place(x=450,y=370)

button_play = Button(myspace, text="Play")
button_play.place(x=340,y=410)

# Side 3
button_replay = Button(myspace, text="Replay")
button_replay.place(x=550,y=280)
button_replay = Button(myspace, text="Exit")
button_replay.place(x=550,y=330)
button_replay = Button(myspace, text="Your Prize")
button_replay.place(x=550,y=380)

myspace.mainloop()