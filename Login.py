import tkinter as tk

# Create the main window
window = tk.Tk()

# Add labels to the main window
label1 = tk.Label(window, text="UNAME:")
label1.pack()

label2 = tk.Label(window, text="PWD:")
label2.pack()

# Add text boxes to the main window
entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

# Add a button to the main window
button = tk.Button(window, text="Login", command=lambda: login(entry1,entry2))
button.pack()

# Start the main event loop
window.mainloop()

def login(entry1,entry2):
    # Get the username and password from the text boxes
    username = entry1.get()
    password = entry2.get()

    # Check if the username and password are valid
    if username == "admin" and password == "password":
        # If the username and password are valid, open the main window
        window.destroy()
        main()
    else:
        # If the username and password are not valid, display an error message
        label3 = tk.Label(window, text="Invalid username or password.")
        label3.pack()

def main():
    # Create the main window
    window = tk.Tk()

    # Add labels to the main window
    label1 = tk.Label(window, text="UNAME:")
    label1.pack()

    label2 = tk.Label(window, text="PWD:")
    label2.pack()

    # Add text boxes to the main window
    entry1 = tk.Entry(window)
    entry1.pack()

    entry2 = tk.Entry(window)
    entry2.pack()

    # Add a button to the main window
    button = tk.Button(window, text="Login", command=lambda: login(entry1,entry2))
    button.pack()

    # Start the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()
    window.mainloop()