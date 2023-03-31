from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

# Created a list to store all the users
users = []


@app.route('/')
def index():
    return render_template('index.html')

# App route for process


@app.route('/process', methods=['POST'])
def process():

    # Created a new user
    if request.form['action'] == 'process':
        data = {
            'id': len(users) + 1,
            'full_name': request.form['full_name'],
            'location': request.form['location'],
            'lang': request.form['lang'],
            'comments': request.form['comments']
        }

    # Appends the data to the users list
    users.append(data)
    session['full_name'] = data['full_name']
    session['location'] = data['location']
    session['lang'] = data['lang']
    session['comments'] = data['comments']

    return redirect('/result')


# Displays the results page
@app.route('/result')
def result():
    return render_template('/result.html')


if __name__ == '__main__':
    app.run(debug=True)
