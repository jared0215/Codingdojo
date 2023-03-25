from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play', defaults={'times': 3})
@app.route('/play/<int:times>')
def index(times):
    return render_template('index.html', times=times)


if __name__ == '__main__':
    app.run(debug=True)
