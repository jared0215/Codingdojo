from flask import render_template, request, redirect, session, flash
from flask_app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cookies')
def cookies():
    return render_template('index.html')
