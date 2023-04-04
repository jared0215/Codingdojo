from flask_app import app
from flask import render_template, redirect, request, session
from ..models.ninja import Ninja
from ..models.dojo import Dojo


@app.route('/')
def index_ninja():
    redirect("/dojos")


@app.route('/ninjas')
def ninjas():
    ninjas = Ninja.get_all_ninja()
    dojos = Dojo.get_all()
    return render_template('ninjas.html', all_ninjas=ninjas, all_dojos=dojos)


# Route to create a new ninja using post method
@app.route('/new_ninjas', methods=['POST'])
# Defines a function to create a new ninja
def create_ninja():

    # If the action of our form is create we will proceed to create a new ninja
    if request.form['action'] == 'create':

        # Stores the Ninja information we want to grab from the form into a dictionary
        data = {
            'dojo_id': request.form['dojo_id'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'age': request.form['age'],
        }

    # Saves the Ninja information into the database
    ninja_id = Ninja.save_ninja(data)
    print(f"THIS IS THE ID: {ninja_id}")

    # Stores the ninja id into the session
    session['ninja_id'] = ninja_id

    # Redirects to the dojos page
    return redirect('/dojos')


# route to edit page
@app.route('/ninjas/edit/<int:ninja_id>')
def edit(ninja_id):
    return render_template('edit_ninja.html', ninja_one=Ninja.get_one_ninja(ninja_id))


# route to edit a ninja using post method
@app.route('/ninjas/edit/<int:ninja_id>', methods=['POST'])
def update_user(ninja_id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'id': ninja_id
    }
    Ninja.update(data)
    dojo_id = Ninja.get_dojo_id(ninja_id)
    return redirect(f'/dojos/{dojo_id}')


@app.route('/ninjas/destroy/<int:ninja_id>')
def destroy(ninja_id):
    dojo_id = Ninja.get_dojo_id(ninja_id)
    Ninja.delete(ninja_id)
    return redirect(f'/dojos/{dojo_id}')
