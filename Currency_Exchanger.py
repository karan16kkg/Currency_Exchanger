import tkinter as tk
from tkinter import *
import tkinter.messagebox

root = tk.Tk()
root.attributes("-fullscreen",True)
root.title("Currency Exchanger")

Tops = Frame(root, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 70, 'bold'), text='Currency Exchanger',bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("currency")
variable2.set("currency")

def RealTimeCurrencyConversion():
	from forex_python.converter import CurrencyRates
	c = CurrencyRates()

	from_currency = variable1.get()
	to_currency = variable2.get()

	if (Amount1_field.get() == ""):
		tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

	elif (from_currency == "currency" or to_currency == "currency"):
		tkinter.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")

	else:
		new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
		new_amount = float("{:.4f}".format(new_amt))
		Amount2_field.insert(0, str(new_amount))

def clear_all():
	Amount1_field.delete(0, tk.END)
	Amount2_field.delete(0, tk.END)

CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "EUR"]

root.configure(background='#e6e5e5')
root.geometry("700x400")

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Amount : ", bg="#e6e5e5", fg="black")
label1.place(x=80,y=200)

label2 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t From Currency : ", bg="#e6e5e5", fg="black")
label2.place(x=80,y=300)

label3 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t To Currency : ", bg="#e6e5e5", fg="black")
label3.place(x=80,y=400)

label4 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t Converted Amount : ", bg="#e6e5e5", fg="black")
label4.place(x=80,y=550)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

FromCurrency_option.place(x=400,y=300)
ToCurrency_option.place(x=400,y=400)

Amount1_field = tk.Entry(root)
Amount1_field.place(x=400,y=200)

Amount2_field = tk.Entry(root)
Amount2_field.place(x=400,y=550)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Convert ", padx=2, pady=2, bg="lightblue", fg="white",command=RealTimeCurrencyConversion)
Label_9.place(x=550,y=450)

Label_9 = Button(root, font=('arial', 15, 'bold'), text=" Clear All ", padx=2, pady=2, bg="lightblue", fg="white",command=clear_all)
Label_9.place(x=550,y=600)

Label_10=Button(root,text="EXIT",bg="red",fg="black",font=("Cascadia Code SemiBold",45,"bold"),command=root.destroy)
Label_10.place(x=1300,y=700)

root.mainloop()