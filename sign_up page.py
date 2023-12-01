# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']

#         # Here, we would usually save the user data to a database

#         return redirect(url_for('index'))
#     else:
#         return render_template('sign up.html')

# @app.route('/')
# def index():
#     return render_template('sign up.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# users = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}  

# def login():
#     username = input("enter your username or mobile number: ")
#     password = input("enter your password: ")

#     if username in users and users[username] == password:
#         return ("login suceccesfull")
#     else:
#         return ("invalid username")

# login()

# import hashlib
# def signup():
#     email = input("Enter email address: ")
#     pwd = input("Enter password: ")
#     conf_pwd = input("Confirm password: ")
#     if conf_pwd == pwd:
#          enc = conf_pwd.encode()
#          hash1 = hashlib.md5(enc).hexdigest()
#     with open("credentials.txt", "w") as f:
#          f.write(email + "\n")
#          f.write(hash1)
#     f.close()
#     print("You have registered successfully!")
#     else:
#         print("Password is not same as above! \n")
# signup()


# import hashlib

# def signup():
#     email = input("Enter email address: ")
#     pwd = input("Enter password: ")
#     conf_pwd = input("Confirm password: ")

#     if conf_pwd == pwd:
#         enc = conf_pwd.encode()
#         hash1 = hashlib.md5(enc).hexdigest()

#         with open("credentials.txt", "w") as f:
#             f.write(email + "\n")
#             f.write(hash1)

#         print("You have registered successfully!")
#     else:
#         print("Password is not the same as above!")

# signup()


import hashlib

def create_user(username, password):
    with open("user_credentials.txt", "a") as f:
        # Hash the password before storing it
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        f.write(f"{username}:{hashed_password}\n")
    print("User created successfully!")

def login(username, password):
    with open("user_credentials.txt", "r") as f:
        for line in f:
            stored_username, stored_hashed_password = line.strip().split(":")
            if username == stored_username:
                # Hash the provided password and compare it with the stored hash
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == stored_hashed_password:
                    print("Login successful!")
                    return
                else:
                    print("Invalid password. Login failed.")
                    return
        print("User not found. Login failed.")

# Example: Creating a user
create_user("user1","12345")

# Example: Logging in
login("user1","12345")
