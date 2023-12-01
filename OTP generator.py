import secrets
import string
import tkinter as tk

# otp generator

def otp_generator(lenght = 4):
    char = string.digits
    otp = "".join(secrets.choice(char) for _ in range(lenght))
    return otp

if __name__ == "__main__":
    otp = otp_generator()
    print("your otp is here : ",otp)

# password generator

# password = input("enter your password : ")

# if len(password) < 8 :
#     print("valid password")
# else:
#     print("wrong password")


# checkbox create

def on_checkbox_toggle():
    # This function will be called when the checkbox is toggled
    if checkbox_var.get():
        label.config(text="Checkbox is checked")
    else:
        label.config(text="Checkbox is unchecked")

# Create a Tkinter window
window = tk.Tk()
window.title("Checkbox Example")

# Create a checkbox variable
checkbox_var = tk.BooleanVar()

# Create a checkbox widget
checkbox = tk.Checkbutton(window, text="Check this box", variable=checkbox_var, command=on_checkbox_toggle)
checkbox.pack()

# Create a label to display the checkbox state
label = tk.Label(window, text="Checkbox is unchecked")
label.pack()

# Start the Tkinter main loop
window.mainloop()

# password = input("enter your password : ")

# if len(password) < 8 :
#     print("valid password")
# else:
#     print("wrong password")
