import tkinter as tk

def add():
    result.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result.set("Error: Divide by 0")

# GUI Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Variables
entry1 = tk.Entry(root, width=15)
entry1.pack(pady=5)

entry2 = tk.Entry(root, width=15)
entry2.pack(pady=5)

# Result label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Buttons
btn_add = tk.Button(root, text="Add", width=10, command=add)
btn_add.pack(pady=2)

btn_sub = tk.Button(root, text="Subtract", width=10, command=subtract)
btn_sub.pack(pady=2)

btn_mul = tk.Button(root, text="Multiply", width=10, command=multiply)
btn_mul.pack(pady=2)

btn_div = tk.Button(root, text="Divide", width=10, command=divide)
btn_div.pack(pady=2)

# Run the app
root.mainloop()
