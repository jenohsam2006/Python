#Jenoh Sam J B
#URK24CS1154
#To design a simple calculator
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
            result.set("Cannot divide by zero" if num2 == 0 else num1 / num2)
    except ValueError:
        result.set("Invalid Input")
root = tk.Tk()
root.title("URK24CS1154")
root.geometry("900x600")
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")
tk.Label(frame, text="Simple Calculator", font=("Arial", 18, "bold"), anchor="center").grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(frame, text="Enter Value 1:", font=("Arial", 16, "bold"), anchor="center").grid(row=1, column=0, columnspan=2, pady=10)
entry1 = tk.Entry(frame, font=("Arial", 14), justify="center")
entry1.grid(row=2, column=0, columnspan=2, pady=10)
tk.Label(frame, text="Enter Value 2:", font=("Arial", 16, "bold"), anchor="center").grid(row=3, column=0, columnspan=2, pady=10)
entry2 = tk.Entry(frame, font=("Arial", 14), justify="center")
entry2.grid(row=4, column=0, columnspan=2, pady=10)
tk.Label(frame, text="Result:", font=("Arial", 16, "bold"), anchor="center").grid(row=5, column=0, columnspan=2, pady=10)
result = tk.StringVar()
result_entry = tk.Entry(frame, textvariable=result, state="readonly", font=("Arial", 14), justify="center")
result_entry.grid(row=6, column=0, columnspan=2, pady=10)
btn_frame = tk.Frame(frame)
btn_frame.grid(row=7, column=0, columnspan=2, pady=15)
btn_add = tk.Button(btn_frame, text="+", width=5, font=("Arial", 14), command=lambda: calculate("+"), bg="green", fg="white")
btn_sub = tk.Button(btn_frame, text="-", width=5, font=("Arial", 14), command=lambda: calculate("-"), bg="blue", fg="white")
btn_mul = tk.Button(btn_frame, text="x", width=5, font=("Arial", 14), command=lambda: calculate("x"), bg="red", fg="white")
btn_div = tk.Button(btn_frame, text="/", width=5, font=("Arial", 14), command=lambda: calculate("/"), bg="purple", fg="white")
btn_add.grid(row=0, column=0, padx=5)
btn_sub.grid(row=0, column=1, padx=5)
btn_mul.grid(row=0, column=2, padx=5)
btn_div.grid(row=0, column=3, padx=5)
root.mainloop()




#Jenoh Sam J B
#URK24CS1154
#To design a Registration form
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("URK24CS1154")
root.geometry("900x600")
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center") 
tk.Label(frame, text="Registration Form", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(frame, text="Full Name:", font=("Arial", 14)).grid(row=1, column=0, columnspan=2, pady=5)
name_entry = tk.Entry(frame, font=("Arial", 14), justify="center")
name_entry.grid(row=2, column=0, columnspan=2, pady=5)
tk.Label(frame, text="Email:", font=("Arial", 14)).grid(row=3, column=0, columnspan=2, pady=5)
email_entry = tk.Entry(frame, font=("Arial", 14), justify="center")
email_entry.grid(row=4, column=0, columnspan=2, pady=5)
tk.Label(frame, text="Gender:", font=("Arial", 14)).grid(row=5, column=0, columnspan=2, pady=5)
gender_var = tk.StringVar()
gender_frame = tk.Frame(frame)
gender_frame.grid(row=6, column=0, columnspan=2, pady=5)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", font=("Arial", 12)).pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", font=("Arial", 12)).pack(side="left")
tk.Label(frame, text="Country:", font=("Arial", 14)).grid(row=7, column=0, columnspan=2, pady=5)
country_var = tk.StringVar()
country_dropdown = ttk.Combobox(frame, textvariable=country_var, font=("Arial", 14), justify="center")
country_dropdown['values'] = ("Select your country", "USA", "UK", "India", "Canada", "Germany")
country_dropdown.current(0)
country_dropdown.grid(row=8, column=0, columnspan=2, pady=5)
tk.Label(frame, text="Programming:", font=("Arial", 14)).grid(row=9, column=0, columnspan=2, pady=5)
programming_frame = tk.Frame(frame)
programming_frame.grid(row=10, column=0, columnspan=2, pady=5)
java_var = tk.BooleanVar()
python_var = tk.BooleanVar()
tk.Checkbutton(programming_frame, text="Java", variable=java_var, font=("Arial", 12)).pack(side="left", padx=10)
tk.Checkbutton(programming_frame, text="Python", variable=python_var, font=("Arial", 12)).pack(side="left")
submit_button = tk.Button(frame, text="Submit", font=("Arial", 14, "bold"), bg="red", fg="white")
submit_button.grid(row=11, column=0, columnspan=2, pady=10)
root.mainloop() 
