from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    random_number = random.randint(1, 100)
    session['ran_num'] = random_number
    print(session['ran_num'])
    return render_template('index.html', ran_num=random_number)


@app.route('/guess')
def guess():
    guess_number = int(request.args['guess'])
    correct = False
    if guess_number == session['ran_num']:
        correct = True
    elif guess_number > session['ran_num']:
        correct = False
        print('Too high!')
    elif guess_number < session['ran_num']:
        correct = False
        print('Too low!')
    return render_template('guess.html', guess_num=guess_number, correct=correct)


if __name__ == '__main__':
    app.run(debug=True)
