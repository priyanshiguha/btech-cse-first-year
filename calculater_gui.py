import tkinter as tk

# Create the main calculator window
root = tk.Tk()
root.title("Priyanshi's Calculator")
root.geometry("400x550")
root.resizable(False, False)

# Set window background
root.configure(bg="#1e1e1e")


# Calculator display
display = tk.Entry(
    root,
    font=("Arial", 24),
    bg= "#2d2d2d",
    fg="white",
    justify="right",
    bd=0
)

display.pack(padx=20, pady=30, ipady=15, fill="x")

# Frame for calculator buttons
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(padx=10, pady=10, expand=True, fill="both")


# Function for percentage
def apply_percent():
    current = display.get()

    if current:
        result = float(current) / 100
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))


# Function to change positive/negative sign
def toggle_sign():
    current = display.get()

    if current:
        result = float(current) * -1
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

# First number button
btn_7 = tk.Button(
    button_frame,
    text="7",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(7)
)

btn_7.grid(row=0, column=0, padx=5, pady=5)

# Number button 8
btn_8 = tk.Button(
    button_frame,
    text="8",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(8)
)

btn_8.grid(row=0, column=1, padx=5, pady=5)

# Number button 9
btn_9 = tk.Button(
    button_frame,
    text="9",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(9)
)

btn_9.grid(row=0, column=2, padx=5, pady=5)

# Number button 6
btn_6 = tk.Button(
    button_frame,
    text="6",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(6)
)

btn_6.grid(row=1, column=2, padx=5, pady=5)

# Number button 5
btn_5 = tk.Button(
    button_frame,
    text="5",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(5)
)                   
btn_5.grid(row=1, column=1, padx=5, pady=5)

# Number button 4
btn_4 = tk.Button(
    button_frame,
    text="4",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(4)
)
btn_4.grid(row=1, column=0, padx=5, pady=5)

# Number button 3
btn_3 = tk.Button(
    button_frame,
    text="3",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(3)
)

btn_3.grid(row=2, column=2, padx=5, pady=5)

# Number button 2
btn_2 = tk.Button(
    button_frame,
    text="2",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(2)
)

btn_2.grid(row=2, column=1, padx=5, pady=5)

# Number button 1
btn_1 = tk.Button(
    button_frame,
    text="1",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(1)
)

btn_1.grid(row=2, column=0, padx=5, pady=5)

# Number button 0
btn_0 = tk.Button(
    button_frame,
    text="0",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number(0) 
)

btn_0.grid(row=3, column=0, padx=5, pady=5)

# Decimal button
btn_decimal = tk.Button(
    button_frame,
    text=".",
    font=("Arial", 18),
    bg="#333333",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_number('.')
)

btn_decimal.grid(row=3, column=1, padx=5, pady=5)

# Addition button
btn_add = tk.Button(
    button_frame,
    text="+",
    font=("Arial", 18),
    bg="#ff9500",
    fg="white",
    width=5,
    height=2, 
    command=lambda: press_operator('+')
)       
btn_add.grid(row=0, column=3, padx=5, pady=5)

# Subtraction button
btn_subtract = tk.Button(
    button_frame,
    text="-",
    font=("Arial", 18),
    bg="#ff9500",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_operator('-')
)
btn_subtract.grid(row=1, column=3, padx=5, pady=5)

# Multiplication button
btn_multiply = tk.Button(
    button_frame,
    text="*",
    font=("Arial", 18),
    bg="#ff9500",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_operator('*')
)
btn_multiply.grid(row=2, column=3, padx=5, pady=5)

# Division button
btn_divide = tk.Button(
    button_frame,
    text="÷",
    font=("Arial", 18),
    bg="#ff9500",
    fg="white",
    width=5,
    height=2,
    command=lambda: press_operator('/')
)
btn_divide.grid(row=3, column=3, padx=5, pady=5)

# Equals button
btn_equal = tk.Button(
    button_frame,
    text="=",
    font=("Arial", 18),
    bg="#2196f3",
    fg="white",
    width=5,
    height=2,
    command=lambda: calculate()
)
btn_equal.grid(row=3, column=2, padx=5, pady=5)

# Function to clear the display
def clear_display():
    global first_number, selected_operator

    display.delete(0, tk.END)
    first_number = None
    selected_operator = None

# Clear button
btn_clear = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 18),
    bg="#e53935",
    fg="white",
    width=5,
    height=2,   
    command=clear_display   
)
btn_clear.grid(row=4, column=0, padx=5, pady=5)

# Function to delete the last character
def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current[:-1])

# Backspace button
btn_backspace = tk.Button(
    button_frame,
    text="⌫",
    font=("Arial", 18),
    bg="#555555",
    fg="white",
    width=5,
    height=2,
    command=backspace
)
btn_backspace.grid(row=4, column=1, padx=5, pady=5)

# Percentage button
btn_percent = tk.Button(
    button_frame,
    text="%",
    font=("Arial", 18),
    bg="#555555",
    fg="white",
    width=5,
    height=2,
    command=apply_percent        
)   
btn_percent.grid(row=4, column=2, padx=5, pady=5)

# Plus-minus button
btn_plus_minus = tk.Button(
    button_frame,
    text="±",
    font=("Arial", 18),
    bg="#555555",
    fg="white",
    width=5,
    height=2,
    command=toggle_sign
)
btn_plus_minus.grid(row=4, column=3, padx=5, pady=5)

# Store calculator values
first_number = None
selected_operator = None

# Function to enter numbers
def press_number(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

# Function to select an operator
def press_operator(operator):
    global first_number, selected_operator

    first_number = float(display.get())
    selected_operator = operator
    display.delete(0, tk.END)

# Function to calculate the result
def calculate():
    global first_number, selected_operator

    second_number = float(display.get())
    if selected_operator == "+":
        result = first_number + second_number
    elif selected_operator == "-":
        result = first_number - second_number
    elif selected_operator == "*":
        result = first_number * second_number
    elif selected_operator == "/":
        result = first_number / second_number
    else:
        return

    display.delete(0, tk.END)
    display.insert(tk.END, str(result)
)

# Start the application
root.mainloop()
