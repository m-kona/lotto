# Masibulele Kona
from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
import re
import rsaidnumber
from PIL import Image

myspace = Tk()
myspace.geometry('500x500')
myspace.title('Age Validation')
myspace.config(bg="#28a00a")

img = PhotoImage(file="lotto.png")
canvas = Canvas(myspace, width = 400, height = 150)
canvas.create_image(20, 20, anchor=NW, image=img)
canvas.place(x=45,y=320)

# StringVar
result = StringVar()


class Check_Age:

    def __init__(self, master):

        self.name_label = Label(master, text="Name", bg="#28a00a")
        self.name_label.place(x=230, y=10)
        self.enter_name = Entry(master)
        self.enter_name.place(x=170, y=35)

        self.email_label = Label(master, text="Email", bg="#28a00a")
        self.email_label.place(x=230, y=75)
        self.enter_email = Entry(master)
        self.enter_email.place(x=170, y=100)

        self.id_label = Label(master, text="ID Number", bg="#28a00a")
        self.id_label.place(x=215, y=135)
        self.enter_id = Entry(master)
        self.enter_id.place(x=170, y=160)

        self.enter_btn = Button(master, text="Enter", bg="#b4d308", command=self.id_info)
        self.enter_btn.place(x=110, y=250)
        self.exit_btn = Button(master, text="Exit", bg="#b4d308")
        self.exit_btn.place(x=220, y=250)
        self.clear_btn = Button(master, text="Clear", bg="#b4d308", command=self.clear)
        self.clear_btn.place(x=320, y=250)

    def email_info(self):
        expr = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        for i in range(len(self.enter_email.get())):
            if re.search(expr, self.enter_email.get()):
                with open("players_info.txt", "w+") as f:
                    f.write(self.enter_name.get())
                    f.write('\n')
                    f.write(self.enter_email.get())
                    f.write('\n')
                    f.write(self.enter_id.get())
                    f.write('\n')

            else:
                messagebox.showerror("Error", "Invalid Email")
                myspace.destroy()

    def id_info(self):
        self.email_info()
        id_number = rsaidnumber.parse(self.enter_id.get())
        dob = id_number.date_of_birth
        age = (datetime.today() - dob) // timedelta(365.245)

        try:
            if age >= 18:
                messagebox.showinfo('Status', "Let's Play!")
                myspace.destroy()
                import lotto_p_two

            elif len(self.enter_id.get()) != 13:
                messagebox.showerror("Error", "Not a valid ID number")
                myspace.destroy()

            else:
                messagebox.showinfo('Error', "Underage,")
                myspace.destroy()

        except ValueError:
            if self.enter_id.get() != int:
                messagebox.showerror("Error", "Only Numbers")

    def exit(self):
        myspace.destroy()

    def clear(self):
        self.enter_name.delete(0,END)
        self.enter_email.delete(0,END)
        self.enter_id.delete(0,END)


log_win = Check_Age(myspace)

myspace.mainloop()