from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return