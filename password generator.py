password = input("enter your password : ")

if len(password) < 8 :
    print("valid password")
else:
    print("wrong password")



# import tkinter as tk

# def on_checkbox_toggle():
#     # This function will be called when the checkbox is toggled
#     if checkbox_var.get():
#         label.config(text="Checkbox is checked")
#     else:
#         label.config(text="Checkbox is unchecked")

# # Create a Tkinter window
# window = tk.Tk()
# window.title("Checkbox Example")

# # Create a checkbox variable
# checkbox_var = tk.BooleanVar()

# # Create a checkbox widget
# checkbox = tk.Checkbutton(window, text="Check this box", variable=checkbox_var, command=on_checkbox_toggle)
# checkbox.pack()

# # Create a label to display the checkbox state
# label = tk.Label(window, text="Checkbox is unchecked")
# label.pack()

# # Start the Tkinter main loop
# window.mainloop()
