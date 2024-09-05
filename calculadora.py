import tkinter as tk

def press(num):
    expressao.set(expressao.get() + str(num))

def igual():
    try:
        total = str(eval(expressao.get()))
        expressao.set(total)
    except:
        expressao.set("Erro")

def clear():
    expressao.set("")

root = tk.Tk()
root.title("Calculadora")
root.configure(bg="#2e2e2e")

expressao = tk.StringVar()
entry = tk.Entry(root, textvariable=expressao, font=('Poppins', 18, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4, bg="#e6e6e6", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def create_button(text, row, col, width=5, height=2, command=None, colspan=1):
    button = tk.Button(root, text=text, width=width, height=height, command=command, 
                       font=('Poppins', 18, 'bold'), fg='white', bg='#333333', 
                       activebackground='#666666', bd=5)
    button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")
    return button

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        create_button(text, row, col, command=clear)
    else:
        create_button(text, row, col, command=lambda b=text: press(b))

create_button('=', 4, 2, width=5, height=2, command=igual, colspan=1)

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()