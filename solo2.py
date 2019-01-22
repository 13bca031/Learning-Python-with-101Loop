import tkinter as tk

root = tk.Tk()

input_label = tk.Label(root, text="Enter temprature")
input_entry = tk.Entry(root, textvariable=numberinput)
input_label.grid(row=0)
input_entry.grid(row=0, column=1)

dropdownList = ["celsius", "fahrenheit", "kelvin"]
dropdown = tk.OptionMenu(root, var, *dropdownlist)
var.set(dropdownList[0])
dropdown.grid(row=0, column=2)

root.mainloop()
