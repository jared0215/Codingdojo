from flask import render_template, request, redirect, session, flash
from flask_app.models.register import User
from flask_app.models.recipes import Recipe
from flask_app import app


# Routes to render the recipes page
@app.route('/recipes')
def recipe():
    if 'user_id' not in session:
        return redirect('/dashboard')
    all_recipes = Recipe.get_all_recipes_with_creator()
    return render_template('recipes.html', all_recipes=all_recipes)


# Route renders the recipe page
@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/dashboard')
    return render_template('new_recipe.html')


# Route for adding a new recipe
@app.route('/recipes/create', methods=['POST'])
def create_recipe():

    if 'user_id' not in session:
        return redirect('/dashboard')

    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'cooked_date': request.form['cooked_date'],
        'cooked_in_30': request.form['cooked_in_30'],
        'user_id': session['user_id']
    }

    # Validate the recipe data
    if not Recipe.validate_recipe(request.form):
        session['name'] = request.form['name']
        session['description'] = request.form['description']
        session['instructions'] = request.form['instructions']
        return redirect('/recipes/new')

    # Remove the data after submitting the form
    if 'name' in session:
        session.pop('name')
    if 'description' in session:
        session.pop('description')
    if 'instructions' in session:
        session.pop('instructions')

    Recipe.save_recipe(data)
    return redirect('/recipes')


# Route for deleting a recipe
@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/dashboard')

    data = {
        'id': recipe_id
    }

    recipe = Recipe.get_recipe_by_id(data)

    # Make sure the user is the creator of the recipe
    if recipe and session['user_id'] == recipe.users_id:
        Recipe.delete_recipe(data)

    return redirect('/recipes')


# Route to render update recipe page
@app.route('/recipes/edit/<int:recipe_id>')
def edit(recipe_id):
    if 'user_id' not in session:
        return redirect('/dashboard')

    data = {
        'id': recipe_id
    }

    one_recipe = Recipe.get_recipe_by_id(data)

    # Check if the recipe exists and the current user is the owner
    if one_recipe and session['user_id'] == one_recipe.users_id:
        return render_template('update.html', one_recipe=one_recipe)
    else:
        # Redirect to an appropriate page if the user is not the owner
        return redirect('/recipes')


# Route for editing a recipe
@app.route('/recipes/update/<int:recipe_id>', methods=['POST'])
def update(recipe_id):
    if 'user_id' not in session:
        return redirect('/dashboard')

    data = {
        'id': recipe_id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'cooked_date': request.form['cooked_date'],
        'cooked_in_30': request.form['cooked_in_30'],
        'user_id': session['user_id']
    }

    # Validate the recipe data
    if not Recipe.validate_recipe(request.form):
        session['name'] = request.form['name']
        session['description'] = request.form['description']
        session['instructions'] = request.form['instructions']
        return redirect(f'/recipes/edit/{recipe_id}')

    # Remove the data after submitting the form
    if 'name' in session:
        session.pop('name')
    if 'description' in session:
        session.pop('description')
    if 'instructions' in session:
        session.pop('instructions')

    recipe = Recipe.get_recipe_by_id(data)

    if recipe and session['user_id'] == recipe.users_id:
        Recipe.update_recipe(data)

    return redirect('/recipes')


# Route for viewing a specific recipe
@app.route('/recipes/<int:recipe_id>')
def view(recipe_id):
    if 'user_id' not in session:
        return redirect('/dashboard')

    data = {
        'id': recipe_id
    }

    recipe = Recipe.get_recipe_by_id(data)

    return render_template('view.html', one_recipe=recipe)
