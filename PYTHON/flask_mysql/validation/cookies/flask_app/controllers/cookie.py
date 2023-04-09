from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import cookie


@app.route('/')
def index():
    return render_template('index.html')


# Takes us to the orders page that shows all of the orders in a table
@app.route('/cookies')
def cookies():

    # calls the get_all method and stores all of the orders in a variable
    orders = cookie.Order.get_all()
    return render_template('index.html', orders=orders)


# Takes us to the new order page
@app.route('/cookies/new')
def new_orders():
    return render_template('new-order.html')


# Route that takes us to the update page
@app.route('/cookies/edit/<int:id>', methods=['GET', 'POST'])
def update_orders(id):
    if request.method == 'GET':
        # Retrieve the order data
        order = cookie.Order.get_by_id(id)

        if order is None:
            # Handle the case when the order doesn't exist
            return redirect('/cookies')

        # Render the update form
        return render_template('update-order.html', order=order)

    elif request.method == 'POST':
        # Validates the form and saves it into the session
        if not cookie.Order.validate_order(request.form):
            return redirect(f'/cookies/edit/{id}')

        data = {
            'name': request.form['full_name'],
            'cookie': request.form['cookie_type'],
            'boxes': request.form['num_of_boxes'],
            'id': id
        }

        cookie.Order.update(data)
        return redirect("/cookies")


# Route to make a new order
@app.route('/order', methods=['POST'])
def order():

    # Validates the form and saves it into the session
    if not cookie.Order.validate_order(request.form):
        session['name'] = request.form['full_name']
        session['cookie'] = request.form['cookie_type']
        session['boxes'] = request.form['num_of_boxes']
        return redirect('/cookies/new')

    # stores the form data into the database if the method is POST
    if request.method == 'POST':
        data = {
            'name': request.form['full_name'],
            'cookie': request.form['cookie_type'],
            'boxes': request.form['num_of_boxes']
        }

    # Remove the data after submitting the form
    if 'name' in session:
        session.pop('name')
    if 'cookie' in session:
        session.pop('cookie')
    if 'boxes' in session:
        session.pop('boxes')

    # Saves data
    id = cookie.Order.save(data)
    print(f"THIS IS THE ORDER ID: {id}")
    session['order_id'] = id

    return redirect("/cookies")


# Deletes the data from the database
@app.route('/cookies/delete/<int:id>')
def delete_orders(id):
    if 'order_id' not in session:
        return redirect('/cookies')
    cookie.Order.delete(id)
    return redirect("/cookies")
