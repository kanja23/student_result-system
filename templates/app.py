from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data storage for users (in practice, you'd use a database)
users = []

@app.route('/')
def index():
    return "Welcome to Student Management System!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.append({'username': username, 'password': password})
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((user for user in users if user['username'] == username and user['password'] == password), None)
        if user:
            return "Logged in successfully!"
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
