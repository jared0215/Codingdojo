from flask import Flask, render_template, request, redirect, session


# Import the class from users.py
from users import User
app = Flask(__name__)
app.secret_key = 'super secret key'


# Index Route
@app.route("/")
def index():
    return redirect("/users/new")


# Routes to page that shows all users in a table
@app.route("/users")
def users():
    # Calls the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("read_all.html", all_users=users)


# Route to a page that allows a us to create a new user
@app.route("/users/new")
def new_user():
    return render_template("create.html")


# Route to create a new user using post method
@app.route('/create', methods=['POST'])
# Defines a function to create a new user
def create():

    # If the action of our form is create we will proceed to create a new user
    if request.form['action'] == 'create':

        # Stores the user information we want to grab from the form into a dictionary
        data = {
            'first_name': request.form['f_name'],
            'last_name': request.form['l_name'],
            'email': request.form['email'],
        }

    # Saves the user information into the database
    user_id = User.save(data)
    print(f"THIS IS THE ID: {user_id}")

    # Stores the user id into the session
    session['user_id'] = user_id

    # Redirects to the users page
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
