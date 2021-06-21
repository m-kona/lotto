#  Masibulele Kona
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk



class realtime_currency_converter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

            # limiting the precision to 2 decimal places
        amount = round(amount * self.currencies[to_currency], 2)
        return amount


class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        self.configure(background ="#28a00a")
        self.geometry("500x500")

        # Label
        clicked = StringVar()

        acc_name_label = Label(self, text="Account Holder Name", bg="#28a00a").place(x=190, y=30)
        enter_acc_name = Entry(self).place(x=190, y=60)
        acc_number = Label(self, text="Account Number", bg="#28a00a").place(x=190, y=90)
        enter_acc_number = Entry(self).place(x=190, y=120)

        bank_menu_label = Label(self, text="Select your Bank", bg="#28a00a").place(x=190, y=150)
        bank_menu = OptionMenu(self, clicked, "Capitec", "Nedbank", "FNB", "ABSA").place(x=190, y=190)

        proceed_btn = Button(self, text="Proceed").place(x=260, y=190)

        self.intro_label = Label(self, text='Convert your Winnings to your currency',
                                 fg='black', relief=tk.RAISED,borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))

        self.date_label = Label(self,
                                text=f"1 South African Rand equals = {self.currency_converter.convert('ZAR', 'USD', 1)} USD \n "
                                     f""f"Date : {self.currency_converter.data['date']}",relief=tk.GROOVE, borderwidth=5)

        self.intro_label.place(x=20, y=260)
        self.date_label.place(x=110, y=300)

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, borderwidth=3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("ZAR")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")  # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.currencies.keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)

        # placing
        self.from_currency_dropdown.place(x=40, y=400)
        self.amount_field.place(x=20, y=370)
        self.to_currency_dropdown.place(x=340, y=400)
        self.converted_amount_field_label.place(x=335, y=370)

        # Convert button
        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=220, y=380)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = realtime_currency_converter(url)

    App(converter)
    mainloop()