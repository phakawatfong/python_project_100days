# mile to km project
from tarfile import PAX_FIELDS
import tkinter as tk

FONT = ("Arial", 12, "normal")


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

window = tk.Tk()
window.title('Mile to Km Converter')
window.minsize(height=300, width=500)
window.config(padx=200, pady=100)

# Entry
entry = tk.Entry(width=10)
entry.grid(column=1, row=0)


# Label
convert_label = tk.Label(text='is equal to', font=FONT)
convert_label.grid(column=0, row=1)

miles_label = tk.Label(text='Miles', font=FONT)
miles_label.grid(column=2, row=0)

km_label = tk.Label(text='Km', font=FONT)
km_label.grid(column=2, row=1)

km_result_label = tk.Label(text="0")
km_result_label.grid(column=1, row=1)

# Button
button = tk.Button(text='Calculate', command=miles_to_km)
button.grid(column=1, row=2)




window.mainloop()