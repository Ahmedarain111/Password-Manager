from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def main():
    return render_template('login.html')