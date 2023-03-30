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


if __name__ == '__main__':
    app.run(debug=True)
