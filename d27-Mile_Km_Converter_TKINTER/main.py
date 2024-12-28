import tkinter as tk


def convert():
    converting = int(mile_input.get()) * 2
    converter_label["text"] = converting


screen = tk.Tk()

screen.config(width=500, height=500, background="white", padx=10, pady=10)
screen.title("Mile to Km Converter")

label = tk.Label(screen, text="is equal to", bg="white", fg="black")
label.grid(column=0, row=1)

mile_input = tk.Entry()
mile_input.grid(column=1, row=0)
mile_label = tk.Label(screen, text="Miles", bg="white", fg="black")
mile_label.grid(column=2, row=0)

converter_label = tk.Label(screen, text="0", bg="white", fg="black")
converter_label.grid(column=1, row=1)
km_label = tk.Label(screen, text="Km", bg="white", fg="black")
km_label.grid(column=2, row=1)

btn = tk.Button(screen, text="convert", command=convert, bg="white", fg="black")
btn.grid(column=1, row=3)
screen.mainloop()
