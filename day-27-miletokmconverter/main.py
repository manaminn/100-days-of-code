from tkinter import *

def button_clicked():
    calculated_km = float(num_miles.get()) * 1.61
    rounded = round(calculated_km, 0)
    num_km.config(text=f"{rounded}")


window = Tk()
window.title("Mile to km converter")
window.config(padx=50, pady=50)

#input miles
num_miles = Entry(width=7)
num_miles.insert(END, string="Miles", )
print(num_miles.get())
num_miles.grid(column=1, row=0)
#text miles
text_miles = Label(text="Miles", font={"Arial", 15, "normal"})
text_miles.grid(column=2, row=0)

#text is equal to
text_is_equal_to = Label(text="is equal to", font={"Arial", 15, "normal"})
text_is_equal_to.grid(column=0, row=1)


#num km calculated
num_km = Label(text="0", font={"Arial", 15, "normal"})
num_km.grid(column=1, row=1)

#text km
text_km = Label(text="Km", font={"Arial", 15, "normal"})
text_km.grid(column=2, row=1)

#Button calculate
button_calculate = Button(text="Calculate", command=button_clicked)
button_calculate.grid(column=1, row=2)
window.mainloop()