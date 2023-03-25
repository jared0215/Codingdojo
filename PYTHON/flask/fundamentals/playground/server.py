from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play', defaults={'times': 3, 'color': 'lightblue'})
@app.route('/play/<int:times>', defaults={'color': 'lightblue'})
@app.route('/play/<int:times>/<string:color>')
@app.route('/play/<string:color>', defaults={'times': 3})
def index(times, color):
    return render_template('index.html', times=times, box_color=color)


if __name__ == '__main__':
    app.run(debug=True)
