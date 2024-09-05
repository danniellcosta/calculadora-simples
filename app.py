import tkinter as tk

def press(num):
    expression_field.set(expression_field.get() + str(num))

def equal_press():
    try:
        total = str(eval(expression_field.get()))
        expression_field.set(total)
    except:
        expression_field.set("Erro")

def clear():
    expression_field.set("")

root = tk.Tk()
root.title("Calculadora")

expression_field = tk.StringVar()
entry = tk.Entry(root, textvariable=expression_field, font=('Arial', 18), bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=10, height=3, command=equal_press).grid(row=row_val, column=col_val, columnspan=2)
        col_val += 2
    elif button == "C":
        tk.Button(root, text=button, width=5, height=3, command=clear).grid(row=row_val, column=col_val)
        col_val += 1
    else:
        tk.Button(root, text=button, width=5, height=3, command=lambda b=button: press(b)).grid(row=row_val, column=col_val)
        col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1
        
root.mainloop()
