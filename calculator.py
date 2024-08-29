import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("600x700")  # Adjust the size as needed
root.configure(bg='#2b2b2b')  # Set background color

# Create a display for the calculator
display = tk.Entry(root, font=("Arial", 30), borderwidth=2, relief="solid", bg="#4a4a4a", fg="#ffffff", justify='right')
display.grid(row=0, column=0, columnspan=4, pady=20, padx=20)

# Function to update the display when a button is clicked
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        clear_display()

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

button_colors = {
    '/': '#ffad42',
    '*': '#ffad42',
    '-': '#ffad42',
    '+': '#ffad42',
    '=': '#42ff88',
    'C': '#ff4242'
}

# Loop through buttons and place them on the grid
row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: button_click(x) if x != "=" else evaluate()
    color = button_colors.get(button, '#4a4a4a')
    tk.Button(root, text=button, font=("Arial", 24), command=action, width=5, height=2, 
              bg=color, fg="#ffffff", activebackground="#5a5a5a", borderwidth=0).grid(row=row_val, column=col_val, padx=10, pady=10)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', font=("Arial", 24), command=clear_display, width=10, height=2, 
          bg=button_colors['C'], fg="#ffffff", activebackground="#ff6666", borderwidth=0).grid(row=row_val, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
