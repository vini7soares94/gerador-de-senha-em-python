import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create GUI window
window = tk.Tk()
window.title("Password Generator")

# Length label and entry
length_label = tk.Label(window, text="Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=5)
length_entry.insert(0, "12")

# Checkboxes for character types
lowercase_var = tk.BooleanVar()
lowercase_var.set(True)
lowercase_check = tk.Checkbutton(window, text="Lowercase", variable=lowercase_var)
lowercase_check.grid(row=1, column=0, padx=10, pady=5)

uppercase_var = tk.BooleanVar()
uppercase_var.set(True)
uppercase_check = tk.Checkbutton(window, text="Uppercase", variable=uppercase_var)
uppercase_check.grid(row=1, column=1, padx=10, pady=5)

digits_var = tk.BooleanVar()
digits_var.set(True)
digits_check = tk.Checkbutton(window, text="Digits", variable=digits_var)
digits_check.grid(row=2, column=0, padx=10, pady=5)

symbols_var = tk.BooleanVar()
symbols_var.set(False)
symbols_check = tk.Checkbutton(window, text="Symbols", variable=symbols_var)
symbols_check.grid(row=2, column=1, padx=10, pady=5)

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=3, columnspan=2, padx=10, pady=5)

# Generated password entry
password_entry = tk.Entry(window, width=30)
password_entry.grid(row=4, columnspan=2, padx=10, pady=5)

window.mainloop()
