import tkinter as tk

def button_click():
    user_input = entry.get()
    label.config(text=user_input)

# create the main window
window = tk.Tk()
window.title("My first GUI")
window.geometry("300x200")

# label to display text
label = tk.Label(window, width=30)
label.pack(pady=10)

# text field
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# create button and attatch func.
button = tk.Button(window,text="Submit", command=button_click)
button.pack(pady=10)


# start Tkinter event loop
window.mainloop()