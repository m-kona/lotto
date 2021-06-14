from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("500x300")
root.config(bg="skyblue")

input_label1 = Label(root, text="Please enter username")
input_label1.place(x=5, y=5)
user_entry = Entry(root)
user_entry.place(x=200, y=5)

input_label2 = Label(root, text="Please enter password")
input_label2.place(x=5, y=50)
pass_entry = Entry(root, show="-")
pass_entry.place(x=200, y=50)

def check():
    username = ["Joyce","Velaphi","Nombi","BraDakie"]
    password = ["10111","11111","12111","13111"]
    found = False

    for x1 in range(len(username)):
        if user_entry.get() == username[x1] and pass_entry.get() == password[x1]:
            found = True
            if found == True:
                messagebox.showinfo("ALERT","Access Granted")
                root.destroy()
                import login_two
        else:
                messagebox.showinfo("ERROR","Access denied")

def clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)

def exit():
    root.destroy()

log_btn = Button(root, text="Login", borderwidth="10", bg="Aqua", font=("Consolas 15 bold"), command=check)
log_btn.place(x=125, y=100)
clear_btn = Button(root, text="Clear", borderwidth="10", bg="Aqua", font=("Consolas 15 bold"), command=clear)
clear_btn.place(x=250, y=100)
exit_btn = Button(root, text="Exit",borderwidth="10", bg="Aqua", font=("Consolas 15 bold"), command=exit)
exit_btn.place(x=375, y=100)

root.mainloop()
