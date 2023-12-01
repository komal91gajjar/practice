from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Get user input from the form
    username = request.form['username']
    password = request.form['password']
    

    # Here, you can add code to store the user information (e.g., in a database)

    # For simplicity, let's just print the user information
    print(f"New user signed up: Username - {username}, Password - {password}")

    # Redirect to the home page after sign up
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
