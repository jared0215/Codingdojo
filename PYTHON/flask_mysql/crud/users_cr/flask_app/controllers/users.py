from flask_app import app
from flask import render_template, redirect, request, session
from ..models.user import User


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
    return redirect(f'/users/{user_id}')


# Route to a page that allows a user to update their information
@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    return render_template('update.html', user=User.get_one(user_id))


# Updates the user information using post method
@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data = {
        'first_name': request.form['f_name'],
        'last_name': request.form['l_name'],
        'email': request.form['email'],
        'id': user_id
    }
    User.update(data)
    return redirect(f'/users/{user_id}')


# Deletes a user using delete method
@app.route('/users/<int:user_id>/destroy')
def destroy(user_id):
    User.delete(user_id)
    return redirect('/users')


@app.route('/users/<int:user_id>')
def show(user_id):
    return render_template('show.html', user=User.get_one(user_id))
