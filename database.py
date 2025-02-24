from flask import Flask, render_template, request, redirect, url_for
from database import add_password, get_passwords

app = Flask(__name__)

@app.route('/')
def home():
    passwords = get_passwords()
    return render_template('index.html', passwords=passwords)

@app.route('/add', methods=['POST'])
def add():
    site = request.form['site']
    username = request.form['username']
    password = request.form['password']
    add_password(site, username, password)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
