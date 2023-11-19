import tkinter as tk
from tkinter import StringVar
import random
import string

class PasswordGenerator:
    def __init__(self,master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text= "Password Length:")
        self.length_entry = tk.Entry(master)
        self.include_letters_var = StringVar()
        self.include_numbers_var = StringVar()
        self.include_symbols_var = StringVar()

        self.include_letters_check = tk.Checkbutton(master,text= "Include Letters", variable=self.include_letters_var, onvalue="yes",offvalue="no")
        
        self.include_numbers_check = tk.Checkbutton(master,text= "Include Numbers", variable=self.include_numbers_var, onvalue="yes",offvalue="no")
        
        self.include_symbols_check = tk.Checkbutton(master,text= "Include Symbolss", variable=self.include_symbols_var, onvalue="yes",offvalue="no")

        self.generate_button = tk.Checkbutton(master,text="Generate Password", command= self.generate_password)
        self.result_label = tk.Label(master,text="Generate Password: ")

        self.label_weight.grid(row=0, column=0, padx=10, pady=10)
        self.label_height.grid(row=1, column=0, padx=10, pady=10)
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10)
        self.entry_height.grid(row=1, column=1, padx=10, pady=10)
        self.button_calculate.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_plot.grid(row=3, column=0, columnspan=2, pady=10)
        self.label_result.grid(row=4, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = int(self.length_entry.get())
        use_letters = self.include_letters_var.get() =="yes"
        use_numbers = self.include_numbers_var.get() =="yes"
        use_symbols = self.include_symbols_var.get() =="yes"

        characters = ""
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            self.result_label.config(text="Error: Please select at least one character type.")
            return

        password= ''.join(random.choice(characters) for _ in range(length))
        self.result_label.config(text=f"Generated Password:{Password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerato(root)
    root.mainloop()