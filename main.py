import tkinter as tk


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")


def clear():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 16), command=clear).grid(row=row_val,
                                                                                               column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 16),
                  command=lambda b=button: entry.insert(tk.END, b) if b != '=' else calculate()).grid(row=row_val,
                                                                                                      column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
