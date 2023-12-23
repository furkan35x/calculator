import tkinter as tk

def button_click(symbol):
    current_text = entry_var.get()
    entry_var.set(current_text + str(symbol))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Hesap Makinası")

# Giriş alanını oluştur
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Helvetica', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Butonları oluştur
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Helvetica', 14),
                       command=lambda t=text: button_click(t) if t != '=' else calculate_result() if t == '=' else clear_entry())
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
