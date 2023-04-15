# Imports
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.register import User
from flask_app.models.tree import Tree


# NEW TREE ROUTE
@app.route('/new/tree')
def new_tree():
    # Checks if the user is logged in
    if 'user_id' not in session:
        return redirect('/dashboard')
    return render_template('new_tree.html')


# CREATE TREE ROUTE
@app.route('/create/tree', methods=['POST'])
def new_tree_post():
    # Checks if the user is logged in
    if 'user_id' not in session:
        return redirect('/dashboard')
    # Data to save
    data = {
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'date_planted': request.form['date_planted'],
        'user_id': session['user_id']
    }

    # Validates the Tree form
    if not Tree.validate_tree(request.form):
        session['species'] = request.form['species']
        session['location'] = request.form['location']
        session['reason'] = request.form['reason']
        return redirect(f'/new/tree')

    # Removes the data after
    if 'species' in session:
        session.pop('species')
    if 'location' in session:
        session.pop('location')
    if 'reason' in session:
        session.pop('reason')

    # Class a classmthod to save the tree
    Tree.save_tree(data)

    return redirect('/dashboard')


# EDIT TREE ROUTE
@app.route('/edit/<tree_id>')
def edit_tree(tree_id):
    # Checks if the user is logged in
    if 'user_id' not in session:
        return redirect('/dashboard')
    data = {
        'id': tree_id
    }

    # Calls a classmthod to get the tree by its id
    one_tree = Tree.get_tree_by_id(data)

    # Check if the tree exists and the current user is the owner
    if one_tree and session['user_id'] == one_tree.users_id:
        return render_template('update.html', one_tree=one_tree)
    else:
        # Redirect to an appropriate page if the user is not the owner
        return redirect('/dashboard')


# POST ROUTE TO EDIT TREE DATA
@app.route('/update/<int:tree_id>', methods=['POST'])
def update(tree_id):
    # Checks if the user is logged in
    if 'user_id' not in session:
        return redirect('/dashboard')

    data = {
        'id': tree_id,
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'date_planted': request.form['date_planted'],
        'user_id': session['user_id']
    }

    # Validates the Tree form
    if not Tree.validate_tree(request.form):
        session['species'] = request.form['species']
        session['location'] = request.form['location']
        session['reason'] = request.form['reason']
        return redirect(f'/edit/{tree_id}')

    # Removes the data after
    if 'species' in session:
        session.pop('species')
    if 'location' in session:
        session.pop('location')
    if 'reason' in session:
        session.pop('reason')

    # Calls a classmthod to get the tree by its id
    tree = Tree.get_tree_by_id(data)

    if tree and session['user_id'] == tree.users_id:
        Tree.update_trees(data)

    return redirect('/dashboard')


# SHOW INDIVIDUAL TREE ROUTE
@app.route('/show/<tree_id>')
def show_tree(tree_id):
    # Checks if the user is logged in
    if 'user_id' not in session:
        return redirect('/dashboard')
    data = {
        'id': tree_id,
    }

    # Calls a classmthod to get the tree by its id
    one_tree = Tree.get_tree_by_id(data)

    return render_template('show.html', one_tree=one_tree)


# DELETE TREE ROUTE
@app.route('/delete/<tree_id>')
def delete_tree(tree_id):
    # Checks if the user is logged in
    if 'user_id' not in session:
        return redirect('/dashboard')
    data = {
        'id': tree_id,
    }

    # Calls a classmthod to get the tree by its id
    tree = Tree.get_tree_by_id(data)

    # Make sure the user is the creator of the Tree
    if tree and session['user_id'] == tree.users_id:
        Tree.delete_trees(data)
    else:
        return redirect('/dashboard')
    return redirect('/user/account')
