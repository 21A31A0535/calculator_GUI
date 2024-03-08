import tkinter as tk

def button_click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Professional Calculator")
window.configure(bg='#000000')

# Create the entry widget to display input and output
entry = tk.Entry(window, width=30, borderwidth=5, font=('Helvetica', 14), bg='#ffffff')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', 'C'
]

# Create and place buttons
row = 1
col = 0
for label in button_labels:
    if label == '=':
        tk.Button(window, text=label, padx=40, pady=20, bg='#4CAF50', fg='white', font=('Helvetica', 14, 'bold'), command=calculate).grid(row=row, column=col, padx=5, pady=5, sticky='ew')
    elif label == 'C':
        tk.Button(window, text=label, padx=80, pady=20, bg='#F44336', fg='white', font=('Helvetica', 14, 'bold'), command=clear_entry).grid(row=row, column=col, padx=5, pady=5, sticky='ew', columnspan=2)
        col += 1
    else:
        tk.Button(window, text=label, padx=40, pady=20, bg='#2196F3', fg='white', font=('Helvetica', 14, 'bold'), command=lambda label=label: button_click(label)).grid(row=row, column=col, padx=5, pady=5, sticky='ew')
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
window.mainloop()
