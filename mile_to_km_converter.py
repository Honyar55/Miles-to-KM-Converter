from tkinter import *

window = Tk()
window.minsize(300, 300)
window.title("Mile To KM")
window.config(padx=20, pady=20)

def calculate():
    mile = input.get()
    km = round(float(mile) * 1.609344, 3)
    label3.config(text=km)    

input = Entry(width=20, background="light blue")
input.grid(column=1, row=0)

label1 = Label(text="Miles", font=("Times New Roman", 16))
label1.grid(column=2, row=0)
label1.config(padx=10, pady=10)

label2 = Label(text="Is Equal To", font=("Times New Roman", 16))
label2.grid(column=0, row=1)
label2.config(padx=10, pady=10)

label3 = Label(text="0", font=("Times New Roman", 16), foreground="red")
label3.grid(column=1, row=1)
label3.config(padx=10, pady=10)

label4 = Label(text="KM", font=("Times New Roman", 16))
label4.grid(column=2, row=1)
label4.config(padx=10, pady=10)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10, pady=10)

window.mainloop()