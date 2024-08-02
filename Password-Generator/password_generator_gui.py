import tkinter as tk
import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    all_characters = lower + upper + digits + special
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            result_label.config(text="Password length must be at least 1.")
        else:
            password = generate_password(length)
            result_label.config(text=f"Generated Password: {password}")
            global current_password
            current_password = password
    except ValueError:
        result_label.config(text="Invalid input. Please enter a numeric value.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(current_password)
    root.update() 
    result_label.config(text="Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")

current_password = ""

tk.Label(root, text="Enter length of password:", font=("Helvetica", 14)).grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_length = tk.Entry(root, font=("Helvetica", 14))
entry_length.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=on_generate, font=("Helvetica", 14)).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Copy", command=copy_to_clipboard, font=("Helvetica", 14)).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()


