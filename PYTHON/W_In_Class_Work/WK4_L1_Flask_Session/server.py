from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

users = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # print(request.form['action'])
    if request.form['action'] == 'submit':
        data = {
            'id': len(users) + 1,
            'f_name': request.form['f_name'],
            'l_name': request.form['l_name'],
            'email': request.form['email'],
            'password': request.form['password']
        }

        users.append(data)
        session['user_id'] = data['id']
        session['f_name'] = data['f_name']

        return redirect('/dash')
    else:
        for user in users:
            if request.form['email'] == user["email"]:

                if request.form['password'] == user["password"]:
                    session["user"] = user
                    return redirect("/dashboard")

        return redirect("/")

    return redirect('/')


@app.route('/dash')
def dash():
    return render_template('dash.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
