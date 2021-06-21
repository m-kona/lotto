#  Masibulele Kona
from tkinter import *
from tkinter import messagebox
import random

my_next_space = Tk()
my_next_space.title('Pick and Play')
my_next_space.geometry('600x500')
my_next_space.config(bg="#28a00a")

img = PhotoImage(file="lotto.png")
canvas = Canvas(my_next_space, width = 400, height = 160)
canvas.create_image(20, 20, anchor=NW, image=img)
canvas.place(x=95,y=20)


class Lotto:
    results = StringVar()
    set_onevar = StringVar()
    set_twovar = StringVar()
    set_threevar = StringVar()

    # lotto sets
    set_one = []
    set_two = []
    set_three = []

    def __init__(self, master):
        # labels
        self.winning_label = Label(master, text="Lotto Nmbers", bg="#28a00a").place(x=250, y=370)
        self.winning_results = Label(master, text='', textvariable=self.results, bg="#28a00a").place(x=250, y=400)

        self.set_one_label = Label(master, text="", textvariable=self.set_onevar, bg="#28a00a").place(x=250, y=225)
        self.set_one_show = Label(master, text="First Set", bg="#28a00a").place(x=250,y=200)
        self.set_two_label = Label(master, text="", textvariable=self.set_twovar, bg="#28a00a").place(x=250, y=280)
        self.set_two_show = Label(master, text="Second Set", bg="#28a00a").place(x=250,y=260)
        self.set_three_label = Label(master, text="", textvariable=self.set_threevar, bg="#28a00a").place(x=250, y=340)
        self.set_three_show = Label(master, text="Third Set", bg="#28a00a").place(x=250,y=320)

        # Buttons
        self.num1 = Button(master, text='1', width=1, command=lambda: self.lottery(1), bg="#b4d308").place(x=10, y=200)
        self.num2 = Button(master, text='2', width=1, command=lambda: self.lottery(2), bg="red").place(x=45, y=200)
        self.num3 = Button(master, text='3', width=1, command=lambda: self.lottery(3), bg="#b4d308").place(x=80, y=200)
        self.num4 = Button(master, text='4', width=1, command=lambda: self.lottery(4), bg="#b4d308").place(x=115, y=200)
        self.num5 = Button(master, text='5', width=1, command=lambda: self.lottery(5), bg="red").place(x=150, y=200)
        self.num6 = Button(master, text='6', width=1, command=lambda: self.lottery(6), bg="#b4d308").place(x=185, y=200)
        self.num7 = Button(master, text='7', width=1, command=lambda: self.lottery(7), bg="orange").place(x=10, y=232)
        self.num8 = Button(master, text='8', width=1, command=lambda: self.lottery(8), bg="#b4d308").place(x=45, y=232)
        self.num9 = Button(master, text='9', width=1, command=lambda: self.lottery(9), bg="red").place(x=80, y=232)
        self.num10 = Button(master, text='10', width=1, command=lambda: self.lottery(10), bg="red").place(x=115, y=232)
        self.num11 = Button(master, text='11', width=1, command=lambda: self.lottery(11), bg="#b4d308").place(x=150, y=232)
        self.num12 = Button(master, text='12', width=1, command=lambda: self.lottery(12), bg="orange").place(x=185, y=232)
        self.num13 = Button(master, text='13', width=1, command=lambda: self.lottery(13), bg="#b4d308").place(x=10, y=264)
        self.num14 = Button(master, text='14', width=1, command=lambda: self.lottery(14), bg="red").place(x=45, y=264)
        self.num15 = Button(master, text='15', width=1, command=lambda: self.lottery(15), bg="#b4d308").place(x=80, y=264)
        self.num16 = Button(master, text='16', width=1, command=lambda: self.lottery(16), bg="#b4d308").place(x=115, y=264)
        self.num17 = Button(master, text='17', width=1, command=lambda: self.lottery(17), bg="red").place(x=150, y=264)
        self.num18 = Button(master, text='18', width=1, command=lambda: self.lottery(18), bg="#b4d308").place(x=185, y=264)
        self.num19 = Button(master, text='19', width=1, command=lambda: self.lottery(19), bg="orange").place(x=10, y=296)
        self.num20 = Button(master, text='20', width=1, command=lambda: self.lottery(20), bg="#b4d308").place(x=45, y=296)
        self.num21 = Button(master, text='21', width=1, command=lambda: self.lottery(21), bg="red").place(x=80, y=296)
        self.num22 = Button(master, text='22', width=1, command=lambda: self.lottery(22), bg="red").place(x=115, y=296)
        self.num23 = Button(master, text='23', width=1, command=lambda: self.lottery(23), bg="#b4d308").place(x=150, y=296)
        self.num24 = Button(master, text='24', width=1, command=lambda: self.lottery(24), bg="orange").place(x=185, y=296)
        self.num25 = Button(master, text='25', width=1, command=lambda: self.lottery(25), bg="#b4d308").place(x=10, y=328)
        self.num26 = Button(master, text='26', width=1, command=lambda: self.lottery(26), bg="red").place(x=45, y=328)
        self.num27 = Button(master, text='27', width=1, command=lambda: self.lottery(27), bg="#b4d308").place(x=80, y=328)
        self.num28 = Button(master, text='28', width=1, command=lambda: self.lottery(28), bg="#b4d308").place(x=115, y=328)
        self.num29 = Button(master, text='29', width=1, command=lambda: self.lottery(29), bg="red").place(x=150, y=328)
        self.num30 = Button(master, text='30', width=1, command=lambda: self.lottery(30), bg="#b4d308").place(x=185, y=328)
        self.num31 = Button(master, text='31', width=1, command=lambda: self.lottery(31), bg="orange").place(x=10, y=360)
        self.num32 = Button(master, text='32', width=1, command=lambda: self.lottery(32), bg="#b4d308").place(x=45, y=360)
        self.num33 = Button(master, text='33', width=1, command=lambda: self.lottery(33), bg="red").place(x=80, y=360)
        self.num34 = Button(master, text='34', width=1, command=lambda: self.lottery(34), bg="red").place(x=115, y=360)
        self.num35 = Button(master, text='35', width=1, command=lambda: self.lottery(35), bg="#b4d308").place(x=150, y=360)
        self.num36 = Button(master, text='36', width=1, command=lambda: self.lottery(36), bg="orange").place(x=185, y=360)
        self.num37 = Button(master, text='37', width=1, command=lambda: self.lottery(37), bg="#b4d308").place(x=10, y=392)
        self.num38 = Button(master, text='38', width=1, command=lambda: self.lottery(38), bg="red").place(x=45, y=392)
        self.num39 = Button(master, text='39', width=1, command=lambda: self.lottery(39), bg="#b4d308").place(x=80, y=392)
        self.num40 = Button(master, text='40', width=1, command=lambda: self.lottery(40), bg="#b4d308").place(x=115, y=392)
        self.num41 = Button(master, text='41', width=1, command=lambda: self.lottery(41), bg="red").place(x=150, y=392)
        self.num42 = Button(master, text='42', width=1, command=lambda: self.lottery(42), bg="#b4d308").place(x=185, y=392)
        self.num43 = Button(master, text='43', width=1, command=lambda: self.lottery(43), bg="orange").place(x=10, y=424)
        self.num44 = Button(master, text='44', width=1, command=lambda: self.lottery(44), bg="#b4d308").place(x=45, y=424)
        self.num45 = Button(master, text='45', width=1, command=lambda: self.lottery(45), bg="red").place(x=80, y=424)
        self.num46 = Button(master, text='46', width=1, command=lambda: self.lottery(46), bg="red").place(x=115, y=424)
        self.num47 = Button(master, text='47', width=1, command=lambda: self.lottery(47), bg="#b4d308").place(x=150, y=424)
        self.num48 = Button(master, text='48', width=1, command=lambda: self.lottery(48), bg="orange").place(x=185, y=424)
        self.num49 = Button(master, text='49', width=1, command=lambda: self.lottery(49), bg="#b4d308").place(x=10, y=456)

        # buttons
        self.play_btn = Button(my_next_space, text='Play',
                                   command=self.play, bg="#b4d308").place(x=450, y=220)
        self.clear_btn = Button(my_next_space, text='Clear',
                                command=self.clear, bg="#b4d308").place(x=450, y=280)
        self.exit_btn = Button(my_next_space, text='Exit',
                               command=self.switch_off, bg="#b4d308").place(x=450, y=340)
        self.claim_btn = Button(my_next_space, text='Claim Prize',
                                command=self.claim, bg="#b4d308").place(x=450, y=400)

    def play(self):
        x = 0
        list_one = []
        while x < 6:
            r = random.randint(1, 49)
            if r not in list_one:
                list_one.append(r)
                x = x + 1
        else:
            x = x - 1
        list_one.sort()
        self.results.set(list_one)

    def lottery(self, num):
        if len(self.set_one) < 6 and num not in self.set_one:
            self.set_one.append(num)
            self.set_onevar.set(self.set_one)

        elif len(self.set_one) == 6 and len(self.set_two) < 6 and num not in self.set_two:
            self.set_two.append(num)
            self.set_twovar.set(self.set_two)

        elif len(self.set_two) == 6 and len(self.set_three) < 6 and num not in self.set_three:
            self.set_three.append(num)
            self.set_threevar.set(self.set_three)

    def lotto_play(self):
        global win
        y = 0
        list_one = []
        while y < 6:
            r = random.randint(1, 49)
            if r not in list_one:
                list_one.append(r)
                x = y + 1
        else:
            x = y - 1
        list_one.sort()
        self.results.set(list_one)
        if self.set_one[x] == list_one[x]:
            y += 1
        if y == 6:
            win = 10000000
        elif y == 5:
            win = 8584
        elif y == 4:
            win = 2384
        elif y == 3:
            win = 100.50
        elif y == 2:
            win = 20
        elif y < 2:
            win = 0
        messagebox.showinfo("Status", "Set had: " + str(y))
        messagebox.showinfo("Lotto", "Numbers are: " + str(list_one))
        messagebox.showinfo("Winnings", "You have won R" + str(win))

    def switch_off(self):
        my_next_space.destroy()

    def clear(self):
        self.results.set("")
        self.set_onevar.set("")
        self.set_twovar.set("")
        self.set_threevar.set("")

    def claim(self):
        import bank_details


a = Lotto(my_next_space)
my_next_space.mainloop()