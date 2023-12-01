from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Login Page")

def login_clicked():
    user = userentry.get()  # Get the username from the Entry widget
    password = passentry.get()  # Get the password from the Entry widget

    if user == "komal" and password == "123456":
        correct = Label(window, text="Thank you for logging in")
        correct.grid(column=1, row=2)
    else:
        wrong = Label(window, text="incorrect username and Wrong Password")
        wrong.grid(column=1, row=2)

user = Label(window,text="Username")
pass1 = Label(window,text="Password")
login = Button(window,text="Login", command=login_clicked)

# def forget_password():
#      number = 

userentry = Entry(window)
passentry = Entry(window)
userentry.grid(column=1, row=0)
passentry.grid(column=1, row=1)
user.grid(column=0, row=0)
pass1.grid(column=0, row=1)
login.grid(column=0, row=2)

window.mainloop()

# def main():
#     username = userentry()
#     password = passentry()

#     if username == "komal" and password == "123456":
#         correct = Label(window,text= "thank you for login")
#         correct.grid(column=1,row=2)
#         main()
#     else:
#         wrong = Label(window,text="Wrong Password")
#         wrong.grid(column=1,row=2)

if __name__ == "__main__":
    
    window.mainloop()

