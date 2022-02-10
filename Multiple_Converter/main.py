from tkinter import *

window = Tk()
window.title("Multiple Converters")
#window.minsize(width=270, height=250)
window.config(padx=20, pady=20)
MY_FONT = ("Comic Sans MS", 16, "bold")

class LittleWindow:
    def __init__(self, to_be_converted, converted, c=0, r=0):
        self.equal_label = Label(text="=", font=MY_FONT)
        self.equal_label.grid(column=c+0, row=r+1, padx=(20, 0))
        self.user_input = Entry(width=10, font=MY_FONT)
        self.user_input.grid(column=c+1, row=r+0)
        self.km_label = Label(text="0", font=MY_FONT)
        self.km_label.grid(column=c+1, row=r+1)

        if to_be_converted == "Miles":
            self.button = Button(text="Calculate", command=self.calculate_km)
            self.button.grid(column=c+1, row=r+2, pady=(0, 20))
        elif to_be_converted == "F":
            self.button = Button(text="Calculate", command=self.calculate_temp)
            self.button.grid(column=c + 1, row=r + 2, pady=(0, 20))
        elif to_be_converted == "lbs":
            self.button = Button(text="Calculate", command=self.calculate_kg)
            self.button.grid(column=c + 1, row=r + 2, pady=(0, 20))
        elif to_be_converted == "inch":
            self.button = Button(text="Calculate", command=self.calculate_cm)
            self.button.grid(column=c + 1, row=r + 2, pady=(0, 20))

        self.miles_label = Label(text=to_be_converted, font=MY_FONT)
        self.miles_label.grid(column=c+2, row=r+0)
        self.km_unit_label = Label(text=converted, font=MY_FONT)
        self.km_unit_label.grid(column=c+2, row=r+1)



    def calculate_km(self):
        miles = float(self.user_input.get())
        km = round(miles * 1.60934, 2)
        self.km_label.config(text=km)


    def calculate_temp(self):
        temp_F = float(self.user_input.get())
        temp_C = round((temp_F-32)*5/9, 2)
        self.km_label.config(text=temp_C)


    def calculate_kg(self):
        pounds = float(self.user_input.get())
        kg = round(pounds * 0.453592, 2)
        self.km_label.config(text=kg)


    def calculate_cm(self):
        inch = float(self.user_input.get())
        cm = round(inch * 2.54, 2)
        self.km_label.config(text=cm)



little_window_km = LittleWindow("Miles", "km")
little_window_temp = LittleWindow("F", "C", c=3)
little_window_kg = LittleWindow("lbs", "kg", r=3)
little_window_cm = LittleWindow("inch", "cm", c=3, r=3)


window.mainloop()

