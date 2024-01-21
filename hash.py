import tkinter as tk
from tkinter import ttk
import pyperclip


def get_and_hash_entry_text(entry, hashed_text_var, copy_btn):
    entry_text = entry.get()
    hashed_text = hash(entry_text)
    hashed_text_var.set(hashed_text)
    copy_btn.pack()


def copy(hashed_text_var):
    pyperclip.copy(hashed_text_var.get())


root = tk.Tk()
root.title("jTools - Hash Generator")

text_input = ttk.Entry(root)
text_input.configure(width=25)
text_input.pack()

hashed_text_variable = tk.StringVar()

go = ttk.Button(root)
go.configure(text="hash")
copy_button = ttk.Button(root)
copy_button.configure(text="copy")
copy_button.pack_forget()
go.configure(
    command=lambda: get_and_hash_entry_text(
        text_input, hashed_text_variable, copy_button
    )
)
go.pack()

hashed_text_label = ttk.Label(root)
hashed_text_label.configure(textvariable=hashed_text_variable)
hashed_text_label.pack()

copy_button.configure(command=lambda: copy(hashed_text_variable))

root.mainloop()
