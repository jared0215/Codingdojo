from flask_app import app
from flask import render_template, redirect, request, session
from ..models.dojo import Dojo
from ..models.ninja import Ninja


@app.route('/')
@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', all_dojos=dojos)


# Route to create a new dojo using post method
@app.route('/create', methods=['POST'])
# Defines a function to create a new dojo
def create():

    # If the action of our form is create we will proceed to create a new dojp
    if request.form['action'] == 'create':

        # Stores the dojo information we want to grab from the form into a dictionary
        data = {
            'name': request.form['dojo_name'],
        }

    # Saves the dojo information into the database
    dojo_id = Dojo.save(data)
    print(f"THIS IS THE ID: {dojo_id}")

    # Stores the dojo id into the session
    session['dojo_id'] = dojo_id

    # Redirects to the dojos page
    return redirect('/dojos')


@app.route('/dojos/<int:dojo_id>')
def ninjas_from_dojos(dojo_id):
    ninjas = Ninja.get_ninjas_by_dojo(dojo_id)
    dojo = Dojo.get_one(dojo_id)
    return render_template('dojos.html', ninjas_dojos=ninjas, dojo_name=dojo.name)

# @app.route('/dojos/<int:dojo_id>')
# def show(dojo_id):
#     return render_template('dojo.html', dojo=Dojo.get_one(dojo_id))
