import tkinter as tk

screen = tk.Tk()
screen.minsize( 800, 600)
screen.title("Test Widget")

# Label
label = tk.Label(screen, text="Hello world")
label.pack()
def click():
    print("clicked")
# Button
btn = tk.Button(screen, text="Click Me", command=click)
btn.pack(side="left")

# Entry
text_entry = tk.Entry(screen, width=50)
text_entry.insert(tk.END, string="Exemple de text")
text_entry.focus()
text_entry.pack()

# Gros text
text = tk.Text(screen, width=50, height=10)
text.insert(tk.END, chars="BLABLABLA")
print(text.get("1.0", tk.END))
text.pack()

# SpinBox

def display_nb():
    print(spin.get())
spin = tk.Spinbox(screen, from_=0, to=100, command=display_nb)
spin.pack()

# Scale
def display_nb2(value):
    print(value)
spin2 = tk.Scale(screen, from_=0, to=100, command=display_nb2)
spin2.pack()

# CheckedButton
def dd():
    print(checked.get())
checked = tk.IntVar()
check = tk.Checkbutton(screen, text="Hello world", variable=checked, command=dd)
check.pack()

#Radio
def dd_radio():
    print(is_radio.get())

is_radio = tk.IntVar()
op1 = tk.Radiobutton(screen, text="Hello world", variable=is_radio, value=1, command=dd_radio)
op2 = tk.Radiobutton(screen, text="Hello world2", variable=is_radio, value=0, command=dd_radio)
op1.pack()
op2.pack()

# List
def dd_l(event):
    print(l.get(l.curselection()))
x = list(range(1,10))

l = tk.Listbox(screen, height=len(x))
for i in x:
    l.insert(tk.END, i)
l.bind("<<ListboxSelect>>", func=dd_l)
l.pack()
screen.mainloop()