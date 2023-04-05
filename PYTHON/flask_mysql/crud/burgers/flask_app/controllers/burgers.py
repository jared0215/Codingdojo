from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.burger import Burger
from ..models.topping import Topping


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create', methods=['POST'])
def create():
    data = {
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        "restaurants_id": 1
    }
    Burger.save(data)
    return redirect('/burgers')


@app.route('/burgers')
def burgers():
    return render_template("results.html", all_burgers=Burger.get_all())


@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("details_page.html", burger=Burger.get_one(data))


@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    # Make sure you have a get_all method in your Topping class.
    all_toppings = Topping.get_all()
    burger_with_toppings = Burger.get_burger_with_toppings(data)
    return render_template("edit_page.html", burger=burger_with_toppings, toppings=all_toppings)


# @app.route('/update/<int:burger_id>', methods=['POST'])
# def update(burger_id):
#     data = {
#         'id': burger_id,
#         "name": request.form['name'],
#         "bun": request.form['bun'],
#         "meat": request.form['meat'],
#         "calories": request.form['calories']
#     }
#     Burger.update(data)
#     return redirect(f"/show/{burger_id}")


@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')


@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)

    topping_data = {
        'burger_id': burger_id,
        'topping_ids': request.form.getlist('toppings')
    }
    Burger.update_toppings(topping_data)

    return redirect(f"/show/{burger_id}")
