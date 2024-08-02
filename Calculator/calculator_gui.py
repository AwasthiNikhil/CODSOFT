import tkinter as tk

def click(button_text):
    current_text = entry.get()
    if button_text == '=':
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def enter_pressed(event):
    click('=')

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 18), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

root.bind('<Return>', enter_pressed)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == 'C':
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=lambda: click('C')).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button_text == '=':
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=lambda: click('=')).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=lambda b=button_text: click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
