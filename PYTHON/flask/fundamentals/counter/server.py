from flask import Flask, render_template, request, redirect, session, make_response

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    visits = request.cookies.get('visits')
    real = request.cookies.get('real')
    if visits is None:
        visits = 1
    else:
        visits = int(visits) + 1

    if real is None:
        real = 1
    else:
        real = int(real) + 1
    response = make_response(render_template(
        'index.html', visits=visits, real=real))
    response.set_cookie('visits', str(visits))
    response.set_cookie('real', str(real))
    return response


@app.route('/<int:num>')
def one(num):
    visits = num - 1
    response = make_response(redirect('/'))
    response.set_cookie('visits', str(visits))
    return response


@app.route('/plustwo', methods=['POST'])
def two():
    plustwo = 1
    visits = request.cookies.get('visits')
    if visits is None:
        visits = plustwo
    else:
        visits = int(visits) + plustwo
    response = make_response(redirect('/'))
    response.set_cookie('visits', str(visits))
    return response


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    response = make_response(redirect('/'))
    response.set_cookie('visits', '0')
    return response


if __name__ == '__main__':
    app.run(debug=True)
