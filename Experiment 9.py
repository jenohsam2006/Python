#Jenoh Sam J B
#URK24CS1154
#To design a simple calculator
print("URK24CS1154")
import tkinter as tk
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "x":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error")
    except ValueError:
        result.set("Invalid Input")
root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")
tk.Label(root, text="Type Value 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Type Value 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=5)
result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result, state="readonly")
result_entry.grid(row=3, column=1, padx=10, pady=5)
btn_frame = tk.Frame(root)
btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
btn_add = tk.Button(btn_frame, text="+", width=5, command=lambda: calculate("+"), bg="green", fg="white")
btn_sub = tk.Button(btn_frame, text="-", width=5, command=lambda: calculate("-"), bg="green", fg="white")
btn_mul = tk.Button(btn_frame, text="x", width=5, command=lambda: calculate("x"), bg="green", fg="white")
btn_div = tk.Button(btn_frame, text="/", width=5, command=lambda: calculate("/"), bg="green", fg="white")
btn_add.grid(row=0, column=0, padx=5)
btn_sub.grid(row=0, column=1, padx=5)
btn_mul.grid(row=0, column=2, padx=5)
btn_div.grid(row=0, column=3, padx=5)
root.mainloop()



#Jenoh Sam J B
#URK24CS1154
#To design a Registration form
print("URK24CS1154")
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")
tk.Label(root, text="Registration Form", font=("Arial", 14, "bold")).grid(row=0, column=1, pady=10)
tk.Label(root, text="Full name").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)
tk.Label(root, text="Gender").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=1, sticky="e")
tk.Label(root, text="Country").grid(row=4, column=0, padx=10, pady=5)
country_var = tk.StringVar()
country_dropdown = ttk.Combobox(root, textvariable=country_var)
country_dropdown['values'] = ("Select your country", "USA", "UK", "India", "Canada", "Germany")
country_dropdown.current(0)
country_dropdown.grid(row=4, column=1, padx=10, pady=5)
tk.Label(root, text="Programming").grid(row=5, column=0, padx=10, pady=5)
java_var = tk.BooleanVar()
python_var = tk.BooleanVar()
tk.Checkbutton(root, text="Java", variable=java_var).grid(row=5, column=1, sticky="w")
tk.Checkbutton(root, text="Python", variable=python_var).grid(row=5, column=1, sticky="e")
submit_button = tk.Button(root, text="Submit", bg="red", fg="white")
submit_button.grid(row=6, column=1, pady=10)
root.mainloop()
