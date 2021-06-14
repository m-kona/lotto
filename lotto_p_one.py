from tkinter import *
from tkinter import messagebox

myspace = Tk()
myspace.title("Authority Check")
myspace.geometry("600x400")

label_name = Label(myspace, text="Name")
label_name.place(x=280,y=30)
enter_name = Entry(myspace, width=30)
enter_name.place(x=180,y=50)

label_email = Label(myspace, text="Email")
label_email.place(x=280,y=100)
enter_email = Entry(myspace, width=30)
enter_email.place(x=180,y=120)

label_address = Label(myspace, text="Address")
label_address.place(x=275,y=170)
enter_address = Entry(myspace, width=30)
enter_address.place(x=180,y=190)

label_identity = Label(myspace, text="Identity (ID)")
label_identity.place(x=265,y=240)
enter_identity = Entry(myspace, width=30)
enter_identity.place(x=180,y=260)

def check():
    name = ["Joyce","Velaphi","BraDakie"]
    address = ["no1 shukushukuma","no2 shukushukuma","no3 shukushukuma"]
    email = ["joyce@gmail.com","velaphi@gmail.com","bradakie@gmail.com"]
    identity = ["10111","11111","12111"]
    found = False

    for x in range(len(name)):
        if enter_name.get() == name[x] and enter_address.get() == address[x]:
            found = True
            if found == True:
                messagebox.showinfo("ALERT","Access Granted")
                myspace.destroy()
                import lotto_p_two
        else:
                messagebox.showinfo("ERROR","Access denied")

button_enter = Button(myspace, text="Enter", bg="skyblue", command=check)
button_enter.place(x=270,y=300)

myspace.mainloop()