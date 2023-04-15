# Imports
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.register import User
from flask_app.models.tree import Tree
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Routes to index page


@app.route('/')
def index():
    return render_template('index.html')


# Routes to dashboard page
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect("/")
    all_trees = Tree.get_all_trees_with_creator()
    return render_template('dash.html', all_trees=all_trees)


# Route to register a new user
@app.route('/register', methods=['POST'])
def register():

    # User Validation thats retains the info after error
    if not User.validate_user(request.form):
        session['first_name'] = request.form['f_name']
        session['last_name'] = request.form['l_name']
        session['email'] = request.form['email']
        return redirect("/")

    # Password Validation
    try:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
    except ValueError:
        flash('Password cannot be empty')
        return redirect('/')

    if request.form['action'] == 'register':
        data = {
            'first_name': request.form['f_name'],
            'last_name': request.form['l_name'],
            'email': request.form['email'],
            'password': pw_hash,
        }

    # Remove the data after submitting the form
    if 'first_name' in session:
        session.pop('first_name')
    if 'last_name' in session:
        session.pop('last_name')
    if 'email' in session:
        session.pop('email')

    # Save the new user to the database
    user_id = User.save(data)
    print(f"THIS IS THE USER ID: {user_id}")
    session['user_id'] = user_id

    # Saves the users full name to the session
    session['full_name'] = f"{data['first_name']} {data['last_name']}"

    return redirect("/dashboard")


# Route to login a user
@app.route('/login', methods=['POST'])
def login():

    # Hidden action for buttons
    if request.form['action'] == 'login':
        # see if the username provided exists in the database
        data = {
            "email": request.form["email"]
        }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login_error")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login_error")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['full_name'] = f"{user_in_db.first_name} {user_in_db.last_name}"
    # never render on a post!!!
    return redirect("/dashboard")


# Logout that clears the session
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


# ROUTES FOR USER ACCOUNT
@app.route('/user/account')
def account():
    if 'user_id' not in session:
        return redirect("/dashboard")
    # Calls a class method to get all the trees that the user has created
    all_trees = Tree.get_all_trees_with_creator()
    return render_template('account.html', all_trees=all_trees)
