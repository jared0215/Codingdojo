from flask import Flask, render_template, request, redirect, session
from users import User

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # print(request.form['action'])
    if request.form['action'] == 'register':
        data = {
            'first_name': request.form['f_name'],
            'last_name': request.form['l_name'],
            'email': request.form['email'],
            'password': request.form['password']
        }

        user_id = User.save(data)
        print(f"THIS IS THE ID: {user_id}")

        session['user_id'] = user_id

        return redirect('/dash')
    else:

        return redirect("/")

    return redirect('/')


@app.route('/dash')
def dash():
    users = User.get_all()
    return render_template('dash.html', users=users)


@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    return render_template('update.html', user=User.get_one(user_id))


@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data = {
        'first_name': request.form['f_name'],
        'last_name': request.form['l_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'id': user_id
    }
    User.update(data)
    return redirect('/dash')


@app.route('/users/<int:user_id>/destroy')
def destroy(user_id):
    User.delete(user_id)
    return redirect('/dash')


if __name__ == '__main__':
    app.run(debug=True)
