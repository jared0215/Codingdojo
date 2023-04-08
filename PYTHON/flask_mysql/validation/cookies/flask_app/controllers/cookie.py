from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import cookie


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cookies')
def cookies():
    orders = cookie.Order.get_all()
    return render_template('index.html', orders=orders)


@app.route('/cookies/new')
def new_orders():
    return render_template('new-order.html')


@app.route('/cookies/edit')
def edit_orders():
    return render_template('update-order.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'GET':
        return render_template('new-order.html')
    else:
        if request.method == 'POST':
            data = {
                'name': request.form['full_name'],
                'cookie': request.form['cookie_type'],
                'boxes': request.form['num_of_boxes']
            }

            id = cookie.Order.save(data)
            print(f"THIS IS THE ORDER ID: {id}")
            session['order_id'] = id

            return redirect("/cookies")
