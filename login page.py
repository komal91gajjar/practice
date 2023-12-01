from flask import Flask

app = Flask(__name__)

# In-memory user database for demonstration purposes
users = {
    'username': 'password',
}

@app.route('/')
def home():
    return 'Welcome to the Login Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return 'Login Successful'
        else:
            return 'Login Failed'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
